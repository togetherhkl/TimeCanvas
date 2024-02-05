# '''
# Author: HKini 1778267485@qq.com
# Date: 2024-01-29 13:32:23
# LastEditTime: 2024-01-29 13:32:32
# LastEditors: HKini 1778267485@qq.com
# Description: 用户增删改查的pydantic模型
# FilePath: \TimeCanvas\backend\schemas\user_schema.py

# '''
from pydantic import BaseModel

class User(BaseModel):
    id: int
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
    id: int
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
    classmates_avatar_name: str
    baidu_uk: str
    class Config:
        orm_mode = True