# _*_ coding: utf-8 _*_
'''
@File  :   main.py
@Time  :   2020-07-13 22:17:05
@Author:   Zizle 
'''

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,  # 允许使用cookies
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index():
    return {"message": "欢迎使用黑马优购API", "meta": {"msg": "获取成功", "status": 200}}

from .routers import homepage_router

app.include_router(
    homepage_router.router,
    prefix="/home",
    tags=["首页"],
    responses={404:{"description": "Not Found"}},
    #dependencies=[Depends(get_token_header)],  # 依赖，类似于钩子函数
)