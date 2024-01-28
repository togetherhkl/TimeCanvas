from fastapi import APIRouter, Query, Request
from fastapi.responses import RedirectResponse
from services import auth_service
from datetime import timedelta
import json
from jose import jwt,JWTError
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
    response = auth_service.get_auth_token(code)
    taken = response["access_token"]
    #获取用户信息
    userinfo = auth_service.get_user_info(taken)
    #把令牌存入数据库
    # print(userinfo)
    #生成jwt令牌
    expires_delta = timedelta(days=auth_service.ACCESS_TOKEN_EXPIRE_DAYS)
    access_token = auth_service.create_access_token(data=userinfo, expires_delta=expires_delta)
    userinfo["access_token"] = access_token
    print(userinfo)
    #前端重定向到主页，并把用户信息传送到前端
    url = "http://localhost:5173/#/" 
    avatar_url = userinfo["avatar_url"]
    baidu_name = userinfo["baidu_name"]
    url = url + "?avatar_url=" + avatar_url + "&baidu_name=" + baidu_name + "&access_token=" + access_token
    return RedirectResponse(url=url)

    return userinfo
    