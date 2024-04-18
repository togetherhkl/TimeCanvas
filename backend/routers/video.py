# '''
# Author: HKini 1778267485@qq.com
# Date: 2024-04-15 11:25:49
# LastEditTime: 2024-04-15 11:25:53
# LastEditors: HKini 1778267485@qq.com
# Description: 视频管理的相关路由
# FilePath: \TimeCanvas\backend\routers\video.py

# '''

from fastapi import APIRouter,Depends,HTTPException,File,UploadFile,Form
from fastapi.responses import StreamingResponse,FileResponse
import os
from dependencies import auth_depend, db_depend
from sqlalchemy.orm import Session
from models import orm_models
from schemas import orm_schema
from crud import album_crud, user_crud,video_crud
import datetime

router = APIRouter()
#格式化文件大小
def format_size(size: int, precision: int = 2) -> str:
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB']
    index = 0
    while size >= 1024 and index < len(suffixes) - 1:
        size /= 1024
        index += 1
    return f'{size:.{precision}f} {suffixes[index]}'
#添加视频
@router.post("/video",tags=["video"],description=
             "添加视频，支持多文件上传，视频文件将保存在media/video文件夹中")
async def video_create(
    files: list[UploadFile],
    db: Session = Depends(db_depend.get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
    video_specifc_event:int=Form(...),
    video_album_type: int=Form(...),
    video_album:int=Form(...),
):
    for file in files:
        video={}
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
        filename = f"{timestamp}_{baidu_uk}_{file.filename}"
        #检查数据库中是否有重名的文件，如果有重新命名
        while video_crud.get_video_by_nickname(db, filename):
            timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
            filename = f"{timestamp}_{baidu_uk}_{file.filename}"
        #保存文件
        with open(f"media/video/{filename}", "wb") as f:
            f.write(file.file.read())
        #计算文件字节大小
        file.file.seek(0)
        file_size = 0
        while True:
            chunk = file.file.read(10000)
            if not chunk:
                break
            file_size += len(chunk)
        size = format_size(file_size)
        video['video_name']=filename
        video['video_owner']=baidu_uk
        # video['video_data']=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        video['video_nickname']= file.filename
        video['video_specifc_event']=video_specifc_event
        video['video_album_type']=video_album_type
        video['video_album']=video_album
        video['video_size']=size
        video_crud.video_create(db, video)
    #返回HTTP 200状态码
    return {"msg":"success"}

#获取特定用户,特定相册类型，特定相册，特定事件的视频
@router.get("/video",tags=["video"],description=
    "获取特定用户,特定相册类型，特定相册，特定事件的视频")
async def get_video(
    video_album_type: int,
    video_album:int,
    video_specifc_event:int,
    db: Session = Depends(db_depend.get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    return video_crud.get_video(db, baidu_uk, video_album_type, video_album, video_specifc_event)

#视频播放的媒体数据流
@router.get("/videostream/{video_name}",tags=["video"],description=
    "视频播放的媒体数据流")
def video_stream(
    video_name,
):
    def iterfile():  # (1)
        with open("media/video/"+video_name, mode="rb") as file_like:  # (2)
            yield from file_like  # (3)
    return StreamingResponse(iterfile(), media_type="video/mp4")

#下载视频
@router.get("/videodownload/{video_name}",tags=["video"],description=
    "下载视频")
def video_download(
    video_name,
    video_nickname,
):
    def iterfile():
        with open("media/video/"+video_name, mode="rb") as file_like:
            yield from file_like
    return StreamingResponse(iterfile(), media_type="application/octet-stream", headers={"Content-Disposition": "attachment; filename="+video_nickname})

#删除视频
@router.delete("/video",tags=["video"],description=
    "删除视频")
async def video_delete(
    video_id: int,
    db: Session = Depends(db_depend.get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    video = video_crud.get_video_by_id(db, video_id)
    if not video:
        raise HTTPException(status_code=404, detail="视频不存在")
    if str(video.video_owner) != str(baidu_uk):
        raise HTTPException(status_code=403, detail="无权删除")
    if(os.path.exists("media/video/"+video.video_name)):
        os.remove("media/video/"+video.video_name)
    return video_crud.video_delete(db, baidu_uk, video_id)
    