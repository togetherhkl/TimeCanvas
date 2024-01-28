# from core.settings import Base
from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Text
from typing import Optional, List
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

#用户表
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, index=True, autoincrement=True)
    baidu_uk = Column(String(15), nullable=False, index=True,primary_key=True)#百度网盘用户uk，用户ID
    baidu_name = Column(String(50), unique=True, nullable=False, unique=True)
    avatar_url = Column(String(200), nullable=False)
    access_token = Column(String(500), nullable=False)
    baidu_vip_type = Column(Integer, nullable=False)#百度网盘用户会员类型
    nickname = Column(String(50), nullable=True)
#同学录
class Classmates(Base):
    __tablename__ = "classmates"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), nullable=False)  #姓名
    nickname = Column(String(50), nullable=True)#昵称
    birthday = Column(DateTime, nullable=True)#生日
    hometown = Column(String(100), nullable=True)#家乡
    hobby = Column(String(200), nullable=True)#爱好
    qq_number = Column(String(20), nullable=True)#QQ号
    wx_number = Column(String(20), nullable=True)#微信号
    phone_number = Column(String(20), nullable=True)#手机号
    email = Column(String(50), nullable=True)#邮箱
    constellation = Column(String(5), nullable=True)#星座
    dream = Column(String(200), nullable=True)#梦想
    graduation_message = Column(Text, nullable=True)#毕业寄语
    classmates_album_name = Column(String(50), nullable=True)#同学录相册名称
    classmates_avatar_name = Column(String(50), nullable=True)#同学录头像名称

    baidu_uk = Column(String(15), ForeignKey("user.baidu_uk"))#外键，关联百度网盘用户
    user = relationship("User", back_populates="classmates")
#有趣的事件
class InterestingEvent(Base):
    __tablename__ = "interesting_event"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    event_name = Column(String(50), nullable=False)#事件名称
    event_date = Column(DateTime, nullable=False)#事件日期
    event_description = Column(Text, nullable=True)#事件描述
    event_participant = Column(Text, nullable=True)#事件参与者
    event_album_image = Column(String(50), nullable=True)#事件相册封面
    event_album_name = Column(String(50), nullable=True)#事件相册名称

    baidu_uk = Column(String(15), ForeignKey("user.baidu_uk"))#外键，关联百度网盘用户
    user = relationship("User", back_populates="interesting_event")
#旅游
class Travel(Base):
    __tablename__ = "travel"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    travel_album_name = Column(String(50), nullable=True,unique=True)#旅游相册名称
    travel_theme = Column(String(50), nullable=False)#旅游主题
    travel_date = Column(DateTime, nullable=False)#旅游日期
    travel_description = Column(Text, nullable=True)#旅游描述
    travel_participant = Column(Text, nullable=True)#旅游参与者
    travel_place = Column(String(300), nullable=False)#旅游地点
    travel_album_image = Column(String(50), nullable=True)#旅游相册封面

    baidu_uk = Column(String(15), ForeignKey("user.baidu_uk"))#外键，关联百度网盘用户
    user = relationship("User", back_populates="travel")
