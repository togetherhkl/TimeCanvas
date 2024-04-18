# '''
# Author: HKini 1778267485@qq.com
# Date: 2024-03-06 15:20:29
# LastEditTime: 2024-03-06 15:20:32
# LastEditors: HKini 1778267485@qq.com
# Description: 相册相关的增删查改
# FilePath: \TimeCanvas\backend\crud\album_crud.py

# '''
from sqlalchemy.orm import Session
from models.orm_models import Album, AlbumType,Classmates,Travel,InterestingEvent
from schemas import orm_schema
from services.baidufile_service import get_image


# 查询特定用户创建的相册类型
def get_album_type(db: Session, baidu_uk: str):
    return db.query(AlbumType).filter(AlbumType.albumtype_owner == baidu_uk).all()


# 创建相册类型
def album_type_create(db: Session, album_type: orm_schema.AlbumType, baidu_uk: str):
    db_album_type = AlbumType(**album_type.model_dump(), albumtype_owner=baidu_uk)
    print(db_album_type)
    db.add(db_album_type)
    db.commit()
    db.refresh(db_album_type)
    return db_album_type


# 删除相册类型
def album_type_delete(db: Session, album_type_id: int, baidu_uk: str):
    db_album_type = (
        db.query(AlbumType)
        .filter(AlbumType.id == album_type_id, AlbumType.albumtype_owner == baidu_uk)
        .first()
    )
    db.delete(db_album_type)
    db.commit()
    return db_album_type


# 修改相册类型
def album_type_update(
    db: Session, album_type: orm_schema.AlbumTypeUpdate, id: int, baidu_uk: str
):
    db_album_type = (
        db.query(AlbumType)
        .filter(AlbumType.id == id, AlbumType.albumtype_owner == baidu_uk)
        .first()
    )
    db_album_type.albumtype_name = album_type.albumtype_name
    db_album_type.albumtype_description = album_type.albumtype_description
    db.commit()
    db.refresh(db_album_type)
    return db_album_type


# 获取相册类型下的相册
def get_album(db: Session, album_type_id: int, baidu_uk: str):
    return (
        db.query(Album)
        .filter(Album.album_type == album_type_id, Album.album_owner == baidu_uk)
        .all()
    )


# 创建相册
def album_create(db: Session, album: orm_schema.AlbumCreate, baidu_uk: str):
    db_album = Album(**album.model_dump(), album_owner=baidu_uk)
    db.add(db_album)
    db.commit()
    db.refresh(db_album)
    return db_album


# 删除相册
def album_delete(db: Session, album_id: int, baidu_uk: str):
    db_album = (
        db.query(Album)
        .filter(Album.id == album_id, Album.album_owner == baidu_uk)
        .first()
    )
    db.delete(db_album)
    db.commit()
    return db_album


# 修改相册
def album_update(db: Session, album: orm_schema.AlbumUpdate, id: int, baidu_uk: str):
    db_album = (
        db.query(Album).filter(Album.id == id, Album.album_owner == baidu_uk).first()
    )
    db_album.album_name = album.album_name
    db_album.album_description = album.album_description
    db.commit()
    db.refresh(db_album)
    return db_album


# 获取每个相册类型下的相册，并从百度网盘提取相册类型封面以及相册封面
def get_album_with_cover(db: Session, baidu_uk: str, access_token: str):
    album_type_list = (
        db.query(AlbumType).filter(AlbumType.albumtype_owner == baidu_uk).all()
    )
    album_list = []
    for album_type in album_type_list:
        temp = {}
        temp["albumtype_id"] = album_type.id
        temp["albumtype_name"] = album_type.albumtype_name
        temp["albumtype_description"] = album_type.albumtype_description
        image_path = "apps/TimeGallery/" + album_type.albumtype_name
        img_url = get_image(access_token, image_path)
        if len(img_url) == 0:
            temp["albumtype_cover"] = (
                "https://th.bing.com/th/id/R.ca9a3b02ee64c3efd35dc6e215877551?rik=a6%2bUESGNlAFEpg&riu=http%3a%2f%2fimg02.tuke88.com%2fpreview%2f00%2f03%2f13%2f59c749e249d02.jpg-0.jpg!%2ffw%2f800%2fquality%2f90%2funsharp%2ftrue%2fcompress%2ftrue&ehk=ECy4SkabpMrAtAWZ7m1ogcSClw2T5r3zsuIjLXTvTck%3d&risl=&pid=ImgRaw&r=0"
            )
        else:
            temp["albumtype_cover"] = img_url[0]
        temp["album_list"] = []
        album_all = (
            db.query(Album)
            .filter(Album.album_type == album_type.id, Album.album_owner == baidu_uk)
            .all()
        )
        for album in album_all:
            temp_album = {}
            temp_album["album_id"] = album.id
            temp_album["album_name"] = album.album_name
            temp_album["album_description"] = album.album_description
            image_path = (
                "apps/TimeGallery/" + album_type.albumtype_name + "/" + album.album_name
            )
            img_url = get_image(access_token, image_path)
            if len(img_url) == 0:
                temp_album["album_cover"] = "https://th.bing.com/th/id/R.1d017ffb70008d02f20dec9e2230568f?rik=R5uApoWs3nv9dg&riu=http%3a%2f%2fimg02.tuke88.com%2fpreview%2f00%2f07%2f84%2f5c52e65a1551f.jpg-0.jpg!%2ffw%2f800%2fquality%2f90%2funsharp%2ftrue%2fcompress%2ftrue&ehk=3b6wjOHxQLe4XjRpyW32pDheUolKWtDekO%2b8jdgo49g%3d&risl=&pid=ImgRaw&r=0"
            else:
                temp_album["album_cover"] = img_url[0]
            temp["album_list"].append(temp_album)
        album_list.append(temp)
    return album_list
#级联选择器的数据
def get_album_cascade(db: Session, baidu_uk: str):
    album_type_list = (
        db.query(AlbumType).filter(AlbumType.albumtype_owner == baidu_uk).all()
    )
    album_type_cascade = []
    for album_type in album_type_list:
        temp = {}
        temp["value"] = album_type.id
        temp["label"] = album_type.albumtype_name
        temp["children"] = []
        album_all = (
            db.query(Album)
            .filter(Album.album_type == album_type.id, Album.album_owner == baidu_uk)
            .all()
        )
        for album in album_all:
            temp_album = {}
            temp_album["value"] = album.id
            temp_album["label"] = album.album_name
            temp_album["children"] = []
            temp["children"].append(temp_album)
            if temp["label"] == "同学录":
                classmates = (db.query(Classmates).
                              filter(Classmates.baidu_uk==baidu_uk,
                                     Classmates.classmates_album_name==album.album_name).all())
                for classmate in classmates:
                    temp_classmate = {}
                    temp_classmate["value"] = classmate.id
                    temp_classmate["label"] = classmate.name
                    temp_album["children"].append(temp_classmate)
            if temp["label"] == "趣事录":
                interestingevent = (db.query(InterestingEvent).
                              filter(InterestingEvent.baidu_uk==baidu_uk,
                                     InterestingEvent.event_album_name==album.album_name).all())
                for event in interestingevent:
                    temp_event = {}
                    temp_event["value"] = event.id
                    temp_event["label"] = event.event_name
                    temp_album["children"].append(temp_event)
            if temp["label"] == "旅游":
                travel = (db.query(Travel).
                              filter(Travel.baidu_uk==baidu_uk,
                                     Travel.travel_album_name==album.album_name).all())
                for travel in travel:
                    temp_travel = {}
                    temp_travel["value"] = travel.id
                    temp_travel["label"] = travel.travel_theme
                    temp_album["children"].append(temp_travel)
        album_type_cascade.append(temp)
    return album_type_cascade