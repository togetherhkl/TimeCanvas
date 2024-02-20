# '''
# Author: HKini 1778267485@qq.com
# Date: 2024-01-15 10:26:59
# LastEditTime: 2024-01-30 11:57:16
# LastEditors: HKini 1778267485@qq.com
# Description: 用户数据的路由处理
# FilePath: \TimeCanvas\backend\routers\users.py
# '''
from fastapi import APIRouter, Query, Request, Depends
from fastapi.responses import RedirectResponse
#加载第三方服务
from services import auth_service, baidufile_service
from datetime import timedelta
#加载模型
from models import orm_models
from crud.user_crud import user_create,user_update,get_user
#加载依赖项
from sqlalchemy.orm import Session
from dependencies.db_depend import get_db
from dependencies import auth_depend
#加载环境变量
from dotenv import load_dotenv
import os
load_dotenv('.env')
frontend_url = os.getenv("FRONTEND_URL")

router = APIRouter()
#获取授权码路由
@router.get("/auth",tags=["users"])
async def auth():
    auth_url = auth_service.get_auth_code()
    print(auth_url)
    return {"auth_url": auth_url}  
#获取令牌路由，授权码回调路由
@router.get("/callback", tags=["users"])
async def callback(code: str = Query(...),db: Session = Depends(get_db)):
    #获取令牌
    response = auth_service.get_auth_token(code)
    # print(response)
    #对令牌进行加密
    token = response["access_token"]
    #判断百度网盘是否有项目的总文件夹，如果没有就创建
    if baidufile_service.is_folder_exist(token, "/apps/TimeGallery")==True:
        pass
    else:
        baidufile_service.create_project_folder(token, "/apps/TimeGallery")
    #获取用户信息
    userinfo = auth_service.get_user_info(token)
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
    user = get_user(db, userinfo["uk"])
    if user is None:
        #创建用户信息
        user_create(db, user_data)
    else:
        #创建用户信息
        user_update(db, user_data)
    #生成jwt令牌
    expires_delta = timedelta(days=auth_service.ACCESS_TOKEN_EXPIRE_DAYS)
    access_token = auth_service.create_access_token(data=userinfo, expires_delta=expires_delta)
    userinfo["access_token"] = access_token
    #前端重定向到主页，并把用户信息传送到前端
    avatar_url = userinfo["avatar_url"]
    baidu_name = userinfo["baidu_name"]
    url = frontend_url + "?avatar_url=" + avatar_url + "&baidu_name=" + baidu_name + "&access_token=" + access_token
    return RedirectResponse(url=url)
#获取百度access_token以及用户的vip_type
@router.get("/userinfo",tags=["users"])
async def userinfo(db: Session = Depends(get_db),baidu_uk: str = Depends(auth_depend.verify_jwt_token)):
    access_token = db.query(orm_models.User).filter(orm_models.User.baidu_uk == baidu_uk).first().access_token
    userinfo = auth_service.get_user_info(access_token)
    userinfo["access_token"] = access_token
    #会员类型，0普通用户、1普通会员、2超级会员
    return userinfo

    