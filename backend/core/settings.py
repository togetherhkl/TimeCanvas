'''
Author: HKini 1778267485@qq.com
Date: 2024-01-14 21:02:26
LastEditTime: 2024-01-30 12:24:26
LastEditors: HKini 1778267485@qq.com
Description: 
FilePath: \TimeCanvas\backend\core\settings.py

'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

#加载.env文件
load_dotenv('.env')
#数据库连接
SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")
#数据库引擎
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
#数据库会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
