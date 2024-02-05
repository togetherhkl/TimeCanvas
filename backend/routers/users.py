# '''
# Author: HKini 1778267485@qq.com
# Date: 2024-01-15 10:26:59
# LastEditTime: 2024-01-30 11:57:16
# LastEditors: HKini 1778267485@qq.com
# Description: 用户数据的路由处理
# FilePath: \TimeCanvas\backend\routers\users.py
# '''
from fastapi import APIRouter, Query, Request
from fastapi.responses import RedirectResponse
from services import auth_service
from datetime import timedelta
from dependencies.db_depend import get_db
from models.orm_models import User
from crud.user_crud import user_create,user_update

router = APIRouter()
#获取授权码路由
@router.get("/auth",tags=["users"])
async def auth():
    auth_url = auth_service.get_auth_code()
    print(auth_url)
    return {"auth_url": auth_url}  
#获取令牌路由，授权码回调路由
@router.get("/callback", tags=["users"])
async def callback(code: str = Query(...)):
    #获取令牌
    response = auth_service.get_auth_token(code)
    # print(response)
    #对令牌进行加密
    taken = response["access_token"]
    #获取用户信息
    userinfo = auth_service.get_user_info(taken)
    #把令牌和用户信息存入数据库
    user_data = {
            "baidu_name": userinfo["baidu_name"],
            "avatar_url": userinfo["avatar_url"],
            "access_token": response["access_token"],
            "refresh_token": response["refresh_token"],
            "baidu_vip_type": userinfo["vip_type"],
            "baidu_uk": userinfo["uk"],
            "nickname": ""
        }
    #判断数据库是否有用户信息
    db=get_db()
    with get_db() as db:
        if db.query(User).filter(User.baidu_uk == userinfo["baidu_uk"]).first() is None:
            #数据库没有用户信息，创建用户信息
            userinfo = user_create(db=db,user=user_data)
        else:
            #数据库有用户信息，更新用户信息
            userinfo = user_update(db=db,user=user_data)
    print(userinfo)
    #生成jwt令牌
    expires_delta = timedelta(days=auth_service.ACCESS_TOKEN_EXPIRE_DAYS)
    access_token = auth_service.create_access_token(data=userinfo, expires_delta=expires_delta)
    userinfo["access_token"] = access_token
    #前端重定向到主页，并把用户信息传送到前端
    url = "http://localhost:5173/#/" 
    avatar_url = userinfo["avatar_url"]
    baidu_name = userinfo["baidu_name"]
    url = url + "?avatar_url=" + avatar_url + "&baidu_name=" + baidu_name + "&access_token=" + access_token
    return RedirectResponse(url=url)

    return userinfo
    