# '''
# Author: HKini 1778267485@qq.com
# Date: 2024-02-18 11:49:49
# LastEditTime: 2024-02-18 11:50:02
# LastEditors: HKini 1778267485@qq.com
# Description: 百度网盘文件操作
# FilePath: \TimeCanvas\backend\services\baidufile_service.py
# '''

import requests
import time
import urllib.parse
from urllib.parse import quote, urlencode
from fastapi.responses import StreamingResponse,FileResponse
import http.client
import mimetypes

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
        "parent_path=/"+quote(folder_name)+
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
def get_video_m3u8(access_token: str, path: str, vip_type: int):
    if vip_type == 2:#超级会员
        url = ("https://pan.baidu.com/rest/2.0/xpan/file?method=streaming&"
           "access_token="+access_token+
           "&path="+quote(path)+
           "&type=M3U8_AUTO_480")
        headers = {
        'User-Agent': 'User-Agent: xpanvideo;TimeGallery;windows11;Windows;11;ts',
        'Host': 'pan.baidu.com',
        }
        return  requests.request("GET", url, headers=headers)
    else:
        #普通会员，加载广告
        url = ("https://pan.baidu.com/rest/2.0/xpan/file?method=streaming&"
           "access_token="+access_token+
           "&path="+quote(path)+
           "&type=M3U8_AUTO_480")
        headers = {
        'User-Agent': 'User-Agent: xpanvideo;TimeGallery;Windows11;Windows;11;ts',
        'Host': 'pan.baidu.com',
        }
        response = requests.request("GET", url, headers=headers)
        if response.json()["errno"] == 133:
            print("播放广告")
            time.sleep(15)#15秒的广告
            adTaken = response.json()["adToken"]
            # print(adTaken)
            adTaken = quote(adTaken)
            # print(adTaken)
            url2 = ("https://pan.baidu.com/rest/2.0/xpan/file?method=streaming&"
                   "access_token="+access_token+
                   "&path="+quote(path)+"&type=M3U8_AUTO_480&"
                   "adToken="+adTaken)
            response = requests.request("GET", url2, headers=headers)
            print("m3u8内容：")
            print(type(response))
            # print(type(response.text))
            # print(response.url)
            print(response.headers)
            return response.content
            # conn = http.client.HTTPSConnection("pan.baidu.com")
            # payload = ''
            # headers = {
            #   'User-Agent': 'pan.baidu.com',
            # }
            # conn.request("GET", url2, payload, headers)
            # res = conn.getresponse()
            # print(type(res))
            # print("文件类型")
            # data = res.read()
            # print(data.decode("utf-8"))
            # return data       
        else:
            print("出错")
        
