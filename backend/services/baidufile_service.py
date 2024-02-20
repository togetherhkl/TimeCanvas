# '''
# Author: HKini 1778267485@qq.com
# Date: 2024-02-18 11:49:49
# LastEditTime: 2024-02-18 11:50:02
# LastEditors: HKini 1778267485@qq.com
# Description: 百度网盘文件操作
# FilePath: \TimeCanvas\backend\services\baidufile_service.py
# '''

import requests
from urllib.parse import quote

#创建文件夹
def create_project_folder(access_token: str, folder_name: str):
    url = ("https://pan.baidu.com/rest/2.0/xpan/file?method=create&access_token=" + access_token)
    payload = {
        "path": quote(folder_name),
        "isdir": 1
    }
    response = requests.request("POST", url, data=payload)
    return response.json()

#判断某文件夹是否存在
def is_folder_exist(access_token: str, folder_name: str):
    url = ("https://pan.baidu.com/rest/2.0/xpan/file?method=list&access_token=" + access_token)
    payload = {
        "dir": "/",
        "web": 0
    }
    response = requests.request("GET", url, data=payload)
    response = response.json()
    for item in response["list"]:
        if item["isdir"] == 1 and item["server_filename"] == folder_name:
            return True
    return False
#获取特定文件下的图片访问链接
def get_image(access_token: str,folder_name: str, ):
    url=(
        "http://pan.baidu.com/rest/2.0/xpan/file?"
        "parent_path=/"+folder_name+
        "&access_token=" + access_token + 
        "&web=0&method=imagelist&order=name"
    )
    payload = {}
    files = {}
    headers = {"User-Agent": "pan.baidu.com"}
    response = requests.request("GET", url, headers=headers, data=payload, files=files).json()
    image_list = response["info"]
    image_url_list = []
    for image in image_list:
        image_url_list.append(image["thumbs"]["url3"])
    return image_url_list
#获取特定文件下的视频列表
def get_video(access_token: str,folder_name: str):
    url=("http://pan.baidu.com/rest/2.0/xpan/file?parent_path=/"+quote(folder_name)+
         "&access_token="+access_token+"&web=0&recursion=0&method=videolist"
    )
    payload = {}
    files = {}
    headers = {
    'User-Agent': 'pan.baidu.com'
    }
    response = requests.request("GET", url, headers=headers, data = payload, files = files).json()
    # return response
    video_list = response["info"]
    video_url_list = []
    for video in video_list:
        temp = {}
        temp['url3'] = video["thumbs"]["url3"]
        temp['path'] = video["path"]
        video_url_list.append(temp)
    return video_url_list
#媒体点播，获取视频的m3u8文件
def get_video_m3u8(access_token: str, path: str):
    url = ("http://pan.baidu.com/rest/2.0/xpan/media?method=streaming&access_token=" + access_token)
    payload = {
        "path": path
    }
    response = requests.request("GET", url, data=payload)
    return response.json()
