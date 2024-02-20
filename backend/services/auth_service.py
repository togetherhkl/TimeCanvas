import requests
from dotenv import load_dotenv
from datetime import datetime,timedelta,timezone
from typing import Union
from jose import jwt,JWTError
from schemas import taken
import os

#加载.env文件
load_dotenv('.env')
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")
#返回获取授权码的url
def get_auth_code():
    payload = {}
    headers = {"User-Agent": "pan.baidu.com"}
    url = "https://openapi.baidu.com/oauth/2.0/authorize"
    params = {
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "scope": "basic,netdisk",
        "display": "page",
        # "force_login": "1",#强制登录
        "qrcode": "1",
    }
    response = requests.get(url, params=params,headers=headers, data=payload)
    return response.url
#获取百度网盘的访问令牌
def get_auth_token(code):
    payload = {}
    headers = {"User-Agent": "pan.baidu.com"}
    url = (
        "https://openapi.baidu.com/oauth/2.0/token?"
        "grant_type=authorization_code&"
        "code=" + code + "&client_id="+client_id+"&"
        "client_secret="+client_secret+
        "&redirect_uri="+redirect_uri
    )
    response = requests.request("GET", url, headers=headers, data=payload)
    response = response.json()
    return response
#刷新百度网盘的访问令牌

#获取百度网盘用户信息
def get_user_info(taken):
    url=(
        "https://pan.baidu.com/rest/2.0/xpan/nas?"
        "access_token="+taken+
        "&method=uinfo"
    )
    response = requests.request("GET", url)
    return response.json()

#生成jwt令牌
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_DAYS = int(os.getenv("ACCESS_TOKEN_EXPIRE_DAYS"))

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    #设置令牌过期时间
    if expires_delta:
        expire = datetime.utcnow() + expires_delta#设置过期时间
    else:
        expire = datetime.utcnow() + timedelta(days=7)#默认过期时间为7天
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

#验证jwt令牌，返回用户信息
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(payload)
        return payload
    except JWTError:
        return None