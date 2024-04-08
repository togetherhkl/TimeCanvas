# '''
# Author: HKini 1778267485@qq.com
# Date: 2024-04-07 21:08:35
# LastEditTime: 2024-04-07 21:08:38
# LastEditors: HKini 1778267485@qq.com
# Description: 旅游相关的crud
# FilePath: \TimeCanvas\backend\crud\travel_crud.py

# '''
from sqlalchemy.orm import Session
from models.orm_models import Travel
from schemas import orm_schema

#创建旅游
def travel_create(db: Session, travel: orm_schema.TravelCreate, baidu_uk: str):
    db_travel = Travel(
        **travel.model_dump(),
        baidu_uk=baidu_uk
    )
    db.add(db_travel)
    db.commit()
    db.refresh(db_travel)
    return db_travel
#更新旅游信息
def travel_update(db: Session, travel: orm_schema.TravelUpdate, id: int, baidu_uk: str):
    db_travel = db.query(Travel).filter(
        Travel.id == id,
        Travel.baidu_uk == baidu_uk
    ).first()
    db_travel.travel_theme = travel.travel_theme
    db_travel.travel_date = travel.travel_date
    db_travel.travel_description = travel.travel_description
    db_travel.travel_participant = travel.travel_participant
    db_travel.travel_place = travel.travel_place
    db_travel.travel_province = travel.travel_province
    db.commit()
    db.refresh(db_travel)
    return db_travel
#删除旅游信息
def travel_delete(db: Session, baidu_uk: str, id: int):
    db_travel = db.query(Travel).filter(
        Travel.id == id,
        Travel.baidu_uk == baidu_uk
    ).first()
    db.delete(db_travel)
    db.commit()
    return db_travel
#获取具体相册下的旅游信息
def get_travel(db: Session, baidu_uk: str,travel_album_name:str):
    return db.query(Travel).filter(
        Travel.baidu_uk == baidu_uk,
        Travel.travel_album_name == travel_album_name
    ).all()