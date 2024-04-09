# '''
# Author: HKini 1778267485@qq.com
# Date: 2024-02-18 13:37:36
# LastEditTime: 2024-02-18 13:37:40
# LastEditors: HKini 1778267485@qq.com
# Description: 同学录的相关路由
# FilePath: \TimeCanvas\backend\routers\classmate.py

# '''
from fastapi import APIRouter,Depends
#加载依赖项
from sqlalchemy.orm import Session
from dependencies.db_depend import get_db
from dependencies import auth_depend
#加载模型
from schemas import orm_schema
from models import orm_models
#加载数据库操作
from crud import classmates_crud,user_crud
from services import baidufile_service
from utils import aes

router = APIRouter()
#获取同学录信息
@router.get("/classmate/{classmates_album_name}",tags=["classmate"])
async def get_classmate(
    classmates_album_name:str,
    db: Session = Depends(get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    #从数据库user中提取用户的百度网盘access_token
    access_token = db.query(orm_models.User).filter(orm_models.User.baidu_uk == baidu_uk).first().access_token
    #从数据库classmates中提取同学录信息
    classmates = classmates_crud.get_classmates(db, baidu_uk, classmates_album_name)
    #返回同学录信息
    return {"classmates":classmates}

#创建同学录信息
@router.post("/classmate/",tags=["classmate"])
async def create_classmate(
    classmates: orm_schema.Classmates,
    db: Session = Depends(get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    #从数据库user中提取用户的百度网盘access_token
    userinfo = user_crud.get_user(db, baidu_uk)
    access_token = aes.decrypt(userinfo.access_token)
    #判断百度网盘是否有项目的总文件夹，如果没有就创建
    if baidufile_service.is_folder_exist(access_token, "TimeGallery/同学录/"+classmates.name)==True:
        pass
    else:
        baidufile_service.create_project_folder(access_token, "/apps/TimeGallery/同学录/"
                                                +classmates.classmates_album_name+'/'+classmates.name)
        baidufile_service.create_project_folder(access_token, "/apps/TimeGallery/同学录/"
                                                +classmates.classmates_album_name+'/'+classmates.name+"/pictures")
        baidufile_service.create_project_folder(access_token, "/apps/TimeGallery/同学录/"
                                                +classmates.classmates_album_name+'/'+classmates.name+"/videos")
    #创建同学录信息
    return classmates_crud.create_classmate(db, classmates, baidu_uk)
#修改同学录信息
@router.put("/classmate/",tags=["classmate"])
async def update_classmate(
    classmates: orm_schema.Classmates,
    id: int,
    db: Session = Depends(get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    #修改同学录信息
    return classmates_crud.update_classmate(db, classmates, id, baidu_uk)
    
#删除同学录信息
@router.delete("/classmate/",tags=["classmate"])
async def delete_classmate(
    id: int,
    db: Session = Depends(get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    #删除同学录信息
    classmates_crud.delete_classmate(db, baidu_uk, id)
    return {"message":"delete success"}