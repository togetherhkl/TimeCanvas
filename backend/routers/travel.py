# '''
# Author: HKini 1778267485@qq.com
# Date: 2024-04-07 21:05:52
# LastEditTime: 2024-04-07 21:07:05
# LastEditors: HKini 1778267485@qq.com
# Description: 旅游相关的路由
# FilePath: \TimeCanvas\backend\routers\travel.py

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
from crud import travel_crud,user_crud
from services import baidufile_service
from utils import aes

router = APIRouter()
#获取旅游信息
@router.get("/travel",tags=["travel"])
async def get_travel(
    travel_album_name:str,
    db: Session = Depends(get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    #从数据库中提取旅游信息
    return travel_crud.get_travel(db, baidu_uk, travel_album_name)

#创建旅游信息
@router.post("/travel",tags=["travel"])
async def create_travel(
    travel: orm_schema.TravelCreate,
    db: Session = Depends(get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    userinfo = user_crud.get_user(db, baidu_uk)
    access_token = aes.decrypt(userinfo.access_token)
    #判断百度网盘是否存在对应文件夹，如果没有就创建
    if baidufile_service.is_folder_exist(access_token, "TimeGallery/旅游/"+travel.travel_album_name)==True:
        pass
    else:
        baidufile_service.create_project_folder(access_token, "/apps/TimeGallery/旅游/"+travel.travel_album_name
                                                +"/"+travel.travel_theme+"/pictures")
        baidufile_service.create_project_folder(access_token, "/apps/TimeGallery/旅游/"+travel.travel_album_name
                                                +"/"+travel.travel_theme+"/videos")

    #创建旅游信息
    return travel_crud.travel_create(db, travel, baidu_uk)

#修改旅游信息
@router.put("/travel",tags=["travel"])
async def update_travel(
    travel: orm_schema.TravelUpdate,
    id: int,
    db: Session = Depends(get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    #修改旅游信息
    return travel_crud.travel_update(db, travel, id, baidu_uk)

#删除旅游信息
@router.delete("/travel",tags=["travel"])
async def delete_travel(
    id: int,
    db: Session = Depends(get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    #删除旅游信息
    return travel_crud.travel_delete(db, baidu_uk, id)


