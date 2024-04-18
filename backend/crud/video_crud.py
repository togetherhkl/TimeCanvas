# '''
# Author: HKini 1778267485@qq.com
# Date: 2024-04-15 11:42:27
# LastEditTime: 2024-04-15 11:42:29
# LastEditors: HKini 1778267485@qq.com
# Description: 视频管理的相关数据库操作
# FilePath: \TimeCanvas\backend\crud\video_crud.py

# '''
from sqlalchemy.orm import Session
from models.orm_models import Album, AlbumType,Classmates,Travel,InterestingEvent,Video
from schemas import orm_schema

#添加视频数据
def video_create(db: Session, video: dict):
    db_video = Video(**video)
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video

#判断是否有重名的视频
def get_video_by_nickname(db: Session, video_name: str):
    return db.query(Video).filter(Video.video_name == video_name).first()

#获取特定用户,特定相册类型，特定相册，特定事件的视频
def get_video(db: Session, baidu_uk: str, album_type: int, album: int, event: int):
    return db.query(Video).filter(
        Video.video_owner == baidu_uk,
        Video.video_album_type == album_type,
        Video.video_album == album,
        Video.video_specifc_event == event
    ).all()

#删除视频
def video_delete(db: Session, baidu_uk: str, id: int):
    db_video = db.query(Video).filter(
        Video.id == id,
        Video.video_owner == baidu_uk
    ).first()
    db.delete(db_video)
    db.commit()
    return db_video

#由id获取视频
def get_video_by_id(db: Session, id: int):
    return db.query(Video).filter(Video.id == id).first()