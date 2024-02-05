# '''
# Author: HKini 1778267485@qq.com
# Date: 2024-01-30 12:04:55
# LastEditTime: 2024-01-30 12:33:32
# LastEditors: HKini 1778267485@qq.com
# Description: 数据库信息
# FilePath: \TimeCanvas\backend\dependencies\db_depend.py

# '''

from core.settings import SessionLocal, engine
from models import orm_models

orm_models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()