# import requests

# # 文件路径
# file_path = './backend/media/temp/test01.jpeg'

# # 请求URL
# url = 'https://d.pcs.baidu.com/rest/2.0/pcs/file'

# # 请求参数
# params = {
#     'method': 'upload',
#     'access_token': '121.05eae9a0af2296c1de1a50fbe42910f9.Y_9GJMwkT--3PMCpz95ReHhsIuImYyWIvlUwUML.ozB2Iw',
#     'path': '/apps/TimeGallery/同学录/test01.jpeg',
# }

# # 发送请求上传文件
# with open(file_path, 'rb') as file:
#     response = requests.post(url, params=params, files={'file': file})

# # 检查请求是否成功
# if response.ok:
#     print("File uploaded successfully.")
# else:
#     print("Failed to upload file.")
#     print(response.text)
#百度网盘删除文件的测试
import requests
# cURL 命令中的 URL
url = "http://pan.baidu.com/rest/2.0/xpan/file?method=filemanager&access_token=121.05eae9a0af2296c1de1a50fbe42910f9.Y_9GJMwkT--3PMCpz95ReHhsIuImYyWIvlUwUML.ozB2Iw&opera=delete"
# cURL 命令中的 POST 数据
data = {
    'async': 1,
    # 'filelist': '["/apps/TimeGallery/同学录/test02.jpeg","/apps/TimeGallery/同学录/test04.jpeg"]'
    'filelist': '["/apps/TimeGallery/同学录/test04.jpeg"]'
    # apps/TimeGallery/%E5%90%8C%E5%AD%A6%E5%BD%95/test02.jpeg",
    # '\'["/apps/TimeGallery/同学录/test04.jpeg"]\''
}
# 发送 POST 请求
response = requests.post(url, data=data)
# 打印响应内容
print(response.text)