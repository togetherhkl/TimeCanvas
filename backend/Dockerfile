# 使用官方 Python 镜像作为基础镜像
FROM python:3.10

# 设置工作目录
WORKDIR /backend



# 复制 requirements.txt 文件到工作目录
COPY requirements.txt .

#安装依赖
# 更改 pip 镜像源为阿里云的镜像源
RUN pip install --no-cache-dir -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt
# RUN pip install --no-cache-dir fastapi uvicorn

# 复制当前目录中的所有文件到工作目录中
COPY . .

# 暴露 FastAPI 的默认端口
EXPOSE 8000

# 启动 FastAPI 服务器
CMD ["python3.10","main.py"]
