from fastapi import FastAPI,Depends
import uvicorn
from routers import users,classmate, baidufile, xunfei, album, statistics, interestingevent, travel
from starlette.middleware.cors import CORSMiddleware#解决跨域问题
#引入全局token验证依赖
from dependencies import auth_depend

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
app.include_router(users.router)#将users.py中的路由添加到app中
app.include_router(classmate.router)#将classmate.py中的路由添加到app中
app.include_router(baidufile.router)#将users.py中的路由添加到app中
app.include_router(xunfei.router)#将xunfei.py中的路由添加到app中
app.include_router(album.router)#将album.py中的路由添加到app中
app.include_router(statistics.router)#将statistics.py中的路由添加到app中
app.include_router(travel.router)#将travel.py中的路由添加到app中

@app.get("/")
def read_root():
    return {"Hello": "World"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)