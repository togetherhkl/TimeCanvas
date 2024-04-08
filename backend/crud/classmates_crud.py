# '''
# Author: HKini 1778267485@qq.com
# Date: 2024-02-18 18:32:27
# LastEditTime: 2024-02-18 18:39:27
# LastEditors: HKini 1778267485@qq.com
# Description: 同学录的数据库操作
# FilePath: \TimeCanvas\backend\crud\classmates_crud.py

# '''
from sqlalchemy.orm import Session
from models.orm_models import Classmates
from schemas import orm_schema
#获取特定阶段的同学录信息
def get_classmates(db: Session, baidu_uk: str, classmates_album_name:str):
    return db.query(Classmates).filter(
        Classmates.classmates_album_name == classmates_album_name,
        Classmates.baidu_uk == baidu_uk
    ).all()
#创建同学录信息
def create_classmates(db: Session, classmates: dict):
    db_classmate = Classmates(**classmates)
    db.add(db_classmate)
    db.commit()
    db.refresh(db_classmate)
    return db_classmate
def create_classmate(db: Session, classmates: orm_schema.Classmates, baidu_uk: str):
    db_classmate = Classmates(**classmates.model_dump(),baidu_uk=baidu_uk)
    # print(db_classmate)
    db.add(db_classmate)
    db.commit()
    db.refresh(db_classmate)
    return db_classmate
#修改同学录信息
def update_classmate(db: Session, classmates: orm_schema.Classmates, id: int, baidu_uk: str):
    db_classmate = db.query(Classmates).filter(
        Classmates.id == id,
        Classmates.baidu_uk == baidu_uk
    ).first()
    db_classmate.name = classmates.name
    db_classmate.nickname = classmates.nickname
    db_classmate.birthday = classmates.birthday
    db_classmate.hometown = classmates.hometown
    db_classmate.hobby = classmates.hobby
    db_classmate.qq_number = classmates.qq_number
    db_classmate.wx_number = classmates.wx_number
    db_classmate.phone_number = classmates.phone_number
    db_classmate.email = classmates.email
    db_classmate.constellation = classmates.constellation
    db_classmate.dream = classmates.dream
    db_classmate.graduation_message = classmates.graduation_message
    db.commit()
    db.refresh(db_classmate)
    return db_classmate
#删除同学录信息
def delete_classmate(db: Session, baidu_uk: str, id: int):
    db_classmate = db.query(Classmates).filter(
        Classmates.id == id,
        Classmates.baidu_uk == baidu_uk
    ).first()
    db.delete(db_classmate)
    db.commit()
    return db_classmate