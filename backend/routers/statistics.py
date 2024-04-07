# '''
# Author: HKini 1778267485@qq.com
# Date: 2024-04-06 15:32:48
# LastEditTime: 2024-04-06 15:33:08
# LastEditors: HKini 1778267485@qq.com
# Description: 统计数据的路由
# FilePath: \TimeCanvas\backend\routers\statistics.py

# '''
from fastapi import APIRouter,Depends
#加载依赖项
from sqlalchemy.orm import Session
from dependencies.db_depend import get_db
from dependencies import auth_depend
#加载数据库操作
from crud import statistics_crud

router = APIRouter()

#同学地区统计
@router.get("/classmate_statiscts/location_bar",tags=["statistics"])
async def get_interest_wordcloud(
    stage:str,
    db: Session = Depends(get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    return statistics_crud.get_classmate_location(db, baidu_uk,stage)
#同学年龄区间统计
@router.get("/classmate_statiscts/age_bar",tags=["statistics"])
async def get_interest_wordcloud(
    stage:str,
    db: Session = Depends(get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    return statistics_crud.get_classmate_age(db, baidu_uk,stage)
#同学爱好词云统计
@router.get("/classmate_statiscts/interest_wordcloud",tags=["statistics"])
async def get_interest_wordcloud(
    stage:str,
    db: Session = Depends(get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    return statistics_crud.get_classmate_hobby_wordcloud(db, baidu_uk,stage)