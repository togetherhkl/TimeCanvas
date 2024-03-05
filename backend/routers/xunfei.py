# '''
# Author: HKini 1778267485@qq.com
# Date: 2024-02-25 12:15:23
# LastEditTime: 2024-02-25 12:16:11
# LastEditors: HKini 1778267485@qq.com
# Description: 讯飞星火模型相关的路由
# FilePath: \TimeCanvas\backend\routers\xunfei.py

# '''

from fastapi import APIRouter,Depends
from dependencies import auth_depend, db_depend
from sqlalchemy.orm import Session
from services import xunfei_service
#加载环境变量
from dotenv import load_dotenv
import os
load_dotenv(".env")
appid = os.getenv("APPID")
api_secret = os.getenv("APISecret")
api_key = os.getenv("APIKey")
domain = os.getenv("DOMAIN")
Spark_url = os.getenv("Spark_url")


router = APIRouter()
#讯飞星火认知模型，文本分析接口
@router.get("/xunfei/semantic/textanl",tags=["xunfei"], description="文本分析接口，输入文本，返回文本的语义分析结果")
async def textanl(
    text: str,
    db: Session = Depends(db_depend.get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    text = xunfei_service.text_analytics_prompt+text#提示词与文本组合
    # print(question)
    text = xunfei_service.checklen(xunfei_service.getText("user",text))
    xunfei_service.answer =""
    xunfei_service.main(appid,api_key,api_secret,Spark_url,domain,text)
    response = xunfei_service.getText("assistant",xunfei_service.answer)
    # print(text)
    answer = response[-1]["content"]
    return answer
#讯飞星火认知模型，文本创作接口
@router.get("/xunfei/semantic/textcreat",tags=["xunfei"], description="文本创作接口，输入文本，返回文本的创作结果")
async def textcreat(
    text: str,
    db: Session = Depends(db_depend.get_db),
    baidu_uk: str = Depends(auth_depend.verify_jwt_token),
):
    text = xunfei_service.text_creat_prompt+text#提示词与文本组合
    text = xunfei_service.checklen(xunfei_service.getText("user",text))
    xunfei_service.answer =""
    xunfei_service.main(appid,api_key,api_secret,Spark_url,domain,text)
    response = xunfei_service.getText("assistant",xunfei_service.answer)
    answer = response[-1]["content"]
    return answer

    

