# '''
# Author: HKini 1778267485@qq.com
# Date: 2024-01-29 13:32:23
# LastEditTime: 2024-01-29 13:32:32
# LastEditors: HKini 1778267485@qq.com
# Description: 用户增删改查的pydantic模型
# FilePath: \TimeCanvas\backend\schemas\user_schema.py

# '''
from pydantic import BaseModel,validator
from datetime import date
from sqlalchemy.orm import Session
from models.orm_models import AlbumType as AlbumTypeModel
from dependencies import db_depend

class User(BaseModel):  
    baidu_name: str
    avatar_url: str
    access_token: str
    refresh_token: str
    baidu_vip_type: int
    nickname: str
    baidu_uk: str
    class Config:
        orm_mode = True

class Classmates(BaseModel):
    name: str
    nickname: str | None
    birthday: str | None
    hometown: str | None
    hobby: str | None
    qq_number: str | None
    wx_number: str  | None
    phone_number: str | None
    email: str | None
    constellation: str  | None
    dream: str | None
    graduation_message: str | None
    classmates_album_name: str 
    classmates_avatar_name: str | None
    class Config:
        orm_mode = True
#相册类型
class AlbumType(BaseModel):
    albumtype_name: str
    albumtype_description: str | None
    class Config:
        orm_mode = True
class AlbumTypeUpdate(BaseModel):
    albumtype_name: str
    albumtype_description: str | None
    class Config:
        orm_mode = True
#相册
class Album(BaseModel):
    album_name: str
    album_description: str | None
    album_data: date | None
    album_type: int | None
    class Config:
        orm_mode = True
class AlbumCreate(BaseModel):
    album_name: str
    album_description: str | None
    album_type: int | None
    class Config:
        orm_mode = True
class AlbumUpdate(BaseModel):
    album_name: str
    album_description: str | None
    class Config:
        orm_mode = True

#旅游
class TravelCreate(BaseModel):
    travel_album_name: str
    travel_theme: str
    travel_date: date
    travel_province: str
    travel_place: str
    travel_description: str | None
    travel_participant: str | None
    class Config:
        orm_mode = True
class TravelUpdate(BaseModel):
    travel_theme: str
    travel_date: date
    travel_province: str
    travel_place: str
    travel_description: str | None
    travel_participant: str | None
    class Config:
        orm_mode = True
#有趣的事件
class Interesting(BaseModel):
    event_name: str
    event_date: date
    event_description: str | None
    event_participant: str | None
    event_album_image: str | None
    event_album_name: str | None
    class Config:
        orm_mode = True
#视频数据
class VideoCreate(BaseModel):
    video_nickname: str 
    video_specifc_event:int
    vide_album_type: int
    video_album:int
    class Config:
        orm_mode = True
