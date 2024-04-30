# '''
# Author: HKini 1778267485@qq.com
# Date: 2024-02-20 12:35:33
# LastEditTime: 2024-02-20 12:35:56
# LastEditors: HKini 1778267485@qq.com
# Description: 获取百度网盘的图片与视频文件
# FilePath: \TimeCanvas\backend\routers\baidufile.py

# '''
from fastapi import APIRouter,Depends,File,UploadFile,Form,HTTPException
from dependencies import auth_depend, db_depend
from sqlalchemy.orm import Session
from services import baidufile_service, auth_service
from models import orm_models
from schemas import orm_schema
from urllib.parse import quote
from fastapi.responses import StreamingResponse, FileResponse, Response,JSONResponse
from utils import aes
from typing import List
import requests
import io,os,hashlib
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
#上传图片
@router.post("/baidufile/uploadimage",tags=["baidufile"])
async def upload_image(
    files: list[UploadFile],
    db: Session = Depends(db_depend.get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
    folder_name:str=Form(...),
):
    access_token = db.query(orm_models.User).filter(orm_models.User.baidu_uk == baidu_uk).first().access_token
    access_token = aes.decrypt(access_token)
    #先把文件存入本地
    for file in files:
        with open(f"media/temp/{file.filename}", "wb") as buffer:
            buffer.write(file.file.read())
    #上传文件
    for file in files:
        path = f"/apps/TimeGallery/{folder_name}/{file.filename}"
        response = baidufile_service.upload_image(access_token, f"media/temp/{file.filename}",path)
        if (response):
            os.remove(f"media/temp/{file.filename}")
        else:
            HTTPException(status_code=400, detail="上传失败")
            return JSONResponse(content={"msg":f"{file.filename}上传失败"},status_code=400)
    return {"msg":"上传成功"}
#获取某个文件夹下的所有图片
@router.get("/baidufile/imageslist",tags=["baidufile"],response_model=list[orm_schema.BaiduImageList])
async def get_images_list(
    folder_name:str,
    db: Session = Depends(db_depend.get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    access_token = db.query(orm_models.User).filter(orm_models.User.baidu_uk == baidu_uk).first().access_token
    access_token = aes.decrypt(access_token)
    path = f"/apps/TimeGallery/{folder_name}"
    return baidufile_service.get_images_list(access_token, path)
#删除指定文件
@router.delete("/baidufile/deletefile",tags=["baidufile"])
async def delete_file(
    filelist:List[str],
    db: Session = Depends(db_depend.get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    #对filelist中的内容进行urlencode
    deletefiles="["
    for i in range(len(filelist)):
        # print(filelist[i])
        filelist[i] = filelist[i]
        if i == len(filelist)-1:
            deletefiles +='"'+filelist[i]+'"'
        else:
            deletefiles +='"'+filelist[i]+'",'
    deletefiles = deletefiles+"]"
    access_token = db.query(orm_models.User).filter(orm_models.User.baidu_uk == baidu_uk).first().access_token
    access_token = aes.decrypt(access_token)
    return baidufile_service.delete_file(access_token, deletefiles)




