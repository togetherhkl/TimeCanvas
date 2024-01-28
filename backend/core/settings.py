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
#数据库基类
Base = declarative_base(engine)
