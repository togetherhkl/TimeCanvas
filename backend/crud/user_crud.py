# '''
# Author: HKini 1778267485@qq.com
# Date: 2024-01-28 22:50:21
# LastEditTime: 2024-01-29 13:11:10
# LastEditors: HKini 1778267485@qq.com
# Description: 用户增删改查
# FilePath: \TimeCanvas\backend\crud\user_crud.py

# '''
from sqlalchemy.orm import Session
from models.orm_models import User,Classmates
from schemas import orm_schema
from utils import aes
#查询用户信息
def get_user(db: Session, baidu_uk: str):
    userinfo = db.query(User).filter(User.baidu_uk == baidu_uk).first()
    #对access_token解密
    if userinfo != None:
        # userinfo.access_token = aes.decrypt(userinfo.access_token)
        pass
    return userinfo
    
#创建用户信息
def user_create(db: Session, user: dict):
    db_user = User(**user)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)#刷新数据库
    return db_user
#修改用户信息
def user_update(db: Session, user: dict):
    db_user = db.query(User).filter(User.baidu_uk == user['baidu_uk']).first()
    db_user.baidu_name = user['baidu_name']
    db_user.avatar_url = user['avatar_url']
    db_user.access_token = user['access_token']
    db_user.refresh_token = user['refresh_token']
    db_user.baidu_vip_type = user['baidu_vip_type']
    db_user.nickname = user['nickname']
    db.commit()
    db.refresh(db_user)
    return db_user