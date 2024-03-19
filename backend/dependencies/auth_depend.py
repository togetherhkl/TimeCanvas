# '''
# Author: HKini 1778267485@qq.com
# Date: 2024-02-18 08:34:40
# LastEditTime: 2024-02-18 08:36:26
# LastEditors: HKini 1778267485@qq.com
# Description: 全局token验证依赖
# FilePath: \TimeCanvas\backend\dependencies\auth_depend.py

# '''
from fastapi import HTTPException,Depends,Header
from services import auth_service

async def verify_jwt_token(timecanvas_token: str = Header(...)):
    result = auth_service.verify_token(timecanvas_token)
    return result['uk']
#获取cookie中的timecanvas_token来进行验证

