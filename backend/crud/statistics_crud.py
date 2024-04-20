# '''
# Author: HKini 1778267485@qq.com
# Date: 2024-04-06 15:38:31
# LastEditTime: 2024-04-06 15:38:42
# LastEditors: HKini 1778267485@qq.com
# Description: 统计数据的CRUD操作
# FilePath: \TimeCanvas\backend\crud\statistics_crud.py

# '''
from sqlalchemy.orm import Session
from sqlalchemy import func,desc,extract,case
from models.orm_models import User,Classmates
from datetime import datetime
import re#正则表达式

#统计不同地区的同学数量
def get_classmate_location(db: Session, baidu_uk: str,stage:str):
    '''
    返回的数据格式为：
    {
        categories: ['北京', '上海', '广州', '深圳', '杭州', '成都', '武汉', '西安', '南京', '厦门'],
        series: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    }
    '''
    classmates_count = db.query(Classmates).filter(Classmates.baidu_uk == baidu_uk,Classmates.classmates_album_name==stage).count()
    locations = []
    series = []
    #聚合查询
    data = (db.query(Classmates.hometown,func.count(Classmates.hometown).label('count'),
                     func.substring_index(Classmates.hometown, '/', 1).label('province'))
            .filter(Classmates.baidu_uk == baidu_uk,Classmates.classmates_album_name==stage)
            .group_by('province')
            .order_by(desc('count'))#按照count降序排列
            .limit(5)#只取前5个
            .all())
    tmp = 0
    for item in data:
        locations.append(item.province)
        series.append(item.count)
        tmp += item.count
    locations.append('其他')
    series.append(classmates_count - tmp)
    return {'categories':locations,'series':series}
#统计不同年龄阶段的同学数量
def get_classmate_age(db: Session, baidu_uk: str,stage:str):
    '''
    返回的数据格式为：
    {
        categories: ['18岁以下', '18-30岁', '30-40岁', '40-50岁', '50-60岁', '60岁以上'],
        series: [10, 20, 30, 40, 50, 60]
    }
    '''
    age_stage = ['18岁以下', '18-30岁', '30-40岁', '40-50岁', '50-60岁', '60岁以上']
    age_count = [0,0,0,0,0,0]
    classmates_birthday = db.query(Classmates.birthday).filter(Classmates.baidu_uk == baidu_uk,Classmates.classmates_album_name==stage).all()
    for item in classmates_birthday:
        age = datetime.now().year - item[0].year
        if age < 18:
            age_count[0] += 1
        elif age < 30:
            age_count[1] += 1
        elif age < 40:
            age_count[2] += 1
        elif age < 50:
            age_count[3] += 1
        elif age < 60:
            age_count[4] += 1
        else:
            age_count[5] += 1
    return {'categories':age_stage,'series':age_count}
#统计同学录爱好词云
def get_classmate_hobby_wordcloud(db: Session, baidu_uk: str,stage:str):
    '''
    返回的数据格式为：
    {
        data: [{ name: '篮球', value: 100 },{ name: '足球', value: 80 },{ name: '美食', value: 20 }]
    }
    '''
    classmates_hobby = db.query(Classmates.hobby).filter(Classmates.baidu_uk == baidu_uk,Classmates.classmates_album_name==stage).all()
    hobby_dict = {}
    separators = r'[ ,、， ]'#正则表达式分隔符
    for item in classmates_hobby:
        hobby = re.split(separators,item[0])
        for h in hobby:
            if h in hobby_dict:
                hobby_dict[h] += 1
            else:
                hobby_dict[h] = 1
    data = [{'name':k,'value':v} for k,v in hobby_dict.items()]
    return {'wordcloud':data}
#星座雷达图数据
def get_classmate_constellation_radar(db: Session, baidu_uk: str,stage:str):
    '''
    返回的数据格式为：
    {
        indicator: [{ name: '白羊座', max: 100 },]
        value: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    }
    '''
    constellation_stage = ['白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座', '摩羯座', '水瓶座', '双鱼座']
    value = [0,0,0,0,0,0,0,0,0,0,0,0]
    constellation = (db.query(Classmates.constellation,func.count(Classmates.constellation).label('count'))
                     .filter(Classmates.baidu_uk == baidu_uk,Classmates.classmates_album_name==stage)
                     .group_by(Classmates.constellation)
                     .all())
    for item in constellation_stage:
        i=0
        for c in constellation:
            if item == c[0]:
                value[i] = c[1]
                break
            i += 1
    indicator = [{'name':k,'max':30} for k in constellation_stage]
    return {'indicator':indicator,'value':value}
    
    