# '''
# Author: HKini 1778267485@qq.com
# Date: 2024-04-07 21:09:22
# LastEditTime: 2024-04-07 21:09:25
# LastEditors: HKini 1778267485@qq.com
# Description: 有趣的事件相关的crud
# FilePath: \TimeCanvas\backend\crud\interestingevent_crud.py

# '''
from sqlalchemy.orm import Session
from models.orm_models import InterestingEvent
from schemas import orm_schema

#创建有趣的事件
def interesting_event_create(db: Session, interesting_event: orm_schema.Interesting, baidu_uk: str):
    db_interesting_event = InterestingEvent(
        **interesting_event.model_dump(),
        baidu_uk=baidu_uk
    )
    db.add(db_interesting_event)
    db.commit()
    db.refresh(db_interesting_event)
    return db_interesting_event
#更新有趣的事件
def interesting_event_update(db: Session, interesting_event: orm_schema.Interesting, id: int, baidu_uk: str):
    db_interesting_event = db.query(InterestingEvent).filter(
        InterestingEvent.id == id,
        InterestingEvent.baidu_uk == baidu_uk
    ).first()
    db_interesting_event.event_album_name= interesting_event.event_album_name
    db_interesting_event.event_name = interesting_event.event_name
    db_interesting_event.event_description = interesting_event.event_description
    db_interesting_event.event_participant = interesting_event.event_participant
    db_interesting_event.event_date = interesting_event.event_date
    db_interesting_event.event_album_image = interesting_event.event_album_image
    db.commit()
    db.refresh(db_interesting_event)
    return db_interesting_event
#删除有趣的事件
def interesting_event_delete(db: Session, baidu_uk: str, id: int):
    db_interesting_event = db.query(InterestingEvent).filter(
        InterestingEvent.id == id,
        InterestingEvent.baidu_uk == baidu_uk
    ).first()
    db.delete(db_interesting_event)
    db.commit()
    return db_interesting_event
#获取具体相册下的有趣的事件
def get_interesting_event(db: Session, baidu_uk: str,event_album_name:str):
    return db.query(InterestingEvent).filter(
        InterestingEvent.baidu_uk == baidu_uk,
        InterestingEvent.event_album_name == event_album_name
    ).all()
