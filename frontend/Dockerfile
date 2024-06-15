# 使用官方的node基础镜像
FROM node:18-alpine

# 设置工作目录
WORKDIR /frontend

# 将package.json和yarn.lock文件复制到工作目录
#COPY package.json yarn.lock ./

# 安装项目依赖
#RUN yarn install

# 将项目源码复制到工作目录
COPY . .


# 暴露5173端口
EXPOSE 5173

# 启动服务器
CMD ["yarn", "dev"]