# '''
# Author: HKini 1778267485@qq.com
# Date: 2024-04-07 21:07:46
# LastEditTime: 2024-04-07 21:07:49
# LastEditors: HKini 1778267485@qq.com
# Description: 有趣的事件相关的路由
# FilePath: \TimeCanvas\backend\routers\interestingevent.py

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
from crud import interestingevent_crud,user_crud
from services import baidufile_service
from utils import aes

router = APIRouter()
#获取有趣的事件信息
@router.get("/interestingevent",tags=["interestingevent"])
async def get_interesting_event(
    event_album_name:str,
    db: Session = Depends(get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    #从数据库中提取有趣的事件信息
    return interestingevent_crud.get_interesting_event(db, baidu_uk, event_album_name)

#创建有趣事件
@router.post("/interestingevent",tags=["interestingevent"])
async def create_interesting_event(
    interesting_event: orm_schema.Interesting,
    db: Session = Depends(get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    #判断百度网盘是否对应的文件夹，如果没有就创建
    userinfo = user_crud.get_user(db, baidu_uk)
    access_token = aes.decrypt(userinfo.access_token)
    if baidufile_service.is_folder_exist(access_token, "TimeGallery/趣事录/"+interesting_event.event_album_name)==True:
        pass
    else:
        baidufile_service.create_project_folder(access_token, "/apps/TimeGallery/趣事录/"+interesting_event.event_album_name)
        baidufile_service.create_project_folder(access_token, "/apps/TimeGallery/趣事录/"+interesting_event.event_album_name
                                                +"/pictures")
        baidufile_service.create_project_folder(access_token, "/apps/TimeGallery/趣事录/"+interesting_event.event_album_name
                                                +"/videos")
    #创建有趣事件
    return interestingevent_crud.interesting_event_create(db, interesting_event, baidu_uk)

#更新有趣事件
@router.put("/interestingevent",tags=["interestingevent"])
async def update_interesting_event(
    interesting_event: orm_schema.Interesting,
    id: int,
    db: Session = Depends(get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    #更新有趣事件
    return interestingevent_crud.interesting_event_update(db, interesting_event, id, baidu_uk)

#删除有趣事件
@router.delete("/interestingevent",tags=["interestingevent"])
async def delete_interesting_event(
    id: int,
    db: Session = Depends(get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    #删除有趣事件
    return interestingevent_crud.interesting_event_delete(db, baidu_uk, id)