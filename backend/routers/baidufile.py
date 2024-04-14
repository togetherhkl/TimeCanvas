# '''
# Author: HKini 1778267485@qq.com
# Date: 2024-02-20 12:35:33
# LastEditTime: 2024-02-20 12:35:56
# LastEditors: HKini 1778267485@qq.com
# Description: 获取百度网盘的图片与视频文件
# FilePath: \TimeCanvas\backend\routers\baidufile.py

# '''
from fastapi import APIRouter,Depends
from dependencies import auth_depend, db_depend
from sqlalchemy.orm import Session
from services import baidufile_service, auth_service
from models import orm_models
from fastapi.responses import StreamingResponse, FileResponse, Response
from utils import aes
import io
router = APIRouter()
#获取特定文件下的图片访问链接
@router.get("/baidufile/image",tags=["baidufile"])
async def get_image(
    folder_name:str,
    db: Session = Depends(db_depend.get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    access_token = db.query(orm_models.User).filter(orm_models.User.baidu_uk == baidu_uk).first().access_token
    access_token=aes.decrypt(access_token)#对access_token进行解密
    return baidufile_service.get_image(access_token, folder_name)
#获取特定文件下的视频列表
@router.get("/baidufile/video/{folder_name}",tags=["baidufile"])
async def get_video(
    folder_name:str,
    db: Session = Depends(db_depend.get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    access_token = db.query(orm_models.User).filter(orm_models.User.baidu_uk == baidu_uk).first().access_token
    access_token = aes.decrypt(access_token)#对access_token进行解密
    return baidufile_service.get_video(access_token, folder_name)
#获取特定视频的m3u8文件
@router.get("/baidufile/m3u8/",tags=["baidufile"])
async def get_m3u8(
    path:str,
    db: Session = Depends(db_depend.get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    access_token = db.query(orm_models.User).filter(orm_models.User.baidu_uk == baidu_uk).first().access_token
    access_token = aes.decrypt(access_token)#对access_token进行解密
    userinfo = auth_service.get_user_info(access_token)
    vip_type = userinfo["vip_type"]
    m3u8 = baidufile_service.get_video_m3u8(access_token, path, vip_type)
    m3u8+=".m3u8"
    # return FileResponse('./tests/test.m3u8', media_type="application/x-mpegURL")
    return Response(m3u8,
                    media_type="application/x-mpegURL",
                    # headers={"Content-Disposition": "attachment; filename=file.m3u8"}
                    )
