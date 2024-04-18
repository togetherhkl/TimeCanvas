# from core.settings import Base
import uuid
from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Text, UUID
from typing import Optional, List
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

#用户表
class User(Base):
    __tablename__ = "user"
    id = Column(Integer, index=True, autoincrement=True)
    baidu_uk = Column(String(15), nullable=False, index=True,primary_key=True)#百度网盘用户uk，用户ID
    baidu_name = Column(String(50), unique=True, nullable=False)
    avatar_url = Column(String(200), nullable=False)
    access_token = Column(String(500), nullable=False)
    refresh_token = Column(String(500), nullable=False)
    baidu_vip_type = Column(Integer, nullable=False)#百度网盘用户会员类型
    nickname = Column(String(50), nullable=True)

    classmates = relationship("Classmates", back_populates="user")
    interesting_event = relationship("InterestingEvent", back_populates="user")
    travel = relationship("Travel", back_populates="user")
    album_type = relationship("AlbumType", back_populates="user")
    album = relationship("Album", back_populates="user")
    video = relationship("Video", back_populates="user")
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
    classmates_avatar_name = Column(String(50), nullable=True)#同学录头像路劲

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
    travel_album_name = Column(String(50), nullable=True)#旅游相册名称
    travel_theme = Column(String(50), nullable=False)#旅游主题
    travel_date = Column(DateTime, nullable=False)#旅游日期
    travel_description = Column(Text, nullable=True)#旅游描述
    travel_participant = Column(Text, nullable=True)#旅游参与者
    travel_place = Column(String(30), nullable=False)#旅游地点
    travel_province = Column(String(30), nullable=False)#旅游省份
    travel_album_image = Column(String(50), nullable=True)#旅游相册封面

    baidu_uk = Column(String(15), ForeignKey("user.baidu_uk"))#外键，关联百度网盘用户
    user = relationship("User", back_populates="travel")

#相册类型
class AlbumType(Base):
    __tablename__ = "album_type"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    albumtype_name = Column(String(50), nullable=False)#相册类型名称
    albumtype_description = Column(Text, nullable=True)#相册类型描述
    albumtype_data = Column(DateTime, nullable=False,default=datetime.now)#相册类型创建日期
    albumtype_owner = Column(String(15), ForeignKey("user.baidu_uk"))#相册类型所有者

    user = relationship("User", back_populates="album_type")
    album = relationship("Album", back_populates="albumtype")
    video = relationship("Video", back_populates="albumtype")
#相册
class Album(Base):
    __tablename__ = "album"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    album_name = Column(String(50), nullable=False,unique=True)#相册名称
    album_description = Column(Text, nullable=True)#相册描述
    album_date = Column(DateTime, nullable=False, default=datetime.now)#相册创建日期
    album_type = Column(Integer, ForeignKey("album_type.id"))#相册类型
    album_owner = Column(String(15), ForeignKey("user.baidu_uk"))#相册所有者

    user = relationship("User", back_populates="album")
    albumtype = relationship("AlbumType", back_populates="album")
    video = relationship("Video", back_populates="album")
#视频数据记录模型
class Video(Base):
    __tablename__ = "video"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    video_name = Column(String(50), nullable=False,unique=True)#视频名称
    video_date = Column(DateTime, nullable=False, default=datetime.now)#视频创建日期
    video_size = Column(String(20), nullable=False)#视频大小
    video_nickname = Column(String(50), nullable=True)#视频昵称
    video_specifc_event = Column(Integer, nullable=False)#视频所属具体事件

    video_owner = Column(String(15), ForeignKey("user.baidu_uk"))#视频所有者
    video_album_type = Column(Integer,ForeignKey("album_type.id"))#视频所属相册类型
    video_album = Column(Integer, ForeignKey("album.id"))#视频所属相册
    
    user = relationship("User", back_populates="video")
    albumtype = relationship("AlbumType", back_populates="video")
    album = relationship("Album", back_populates="video")