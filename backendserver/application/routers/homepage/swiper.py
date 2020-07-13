# _*_ coding: utf-8 _*_
'''
@File  :   swiper.py
@Time  :   2020-07-13 22:15:46
@Author:   Zizle 
'''

from fastapi import APIRouter

router = APIRouter()

@router.get("/swiperdata/", summary="获取轮播图")  # 首页轮播图-GET
async def swiper_data():
    
    return {"meta":{"msg":"获取成功!", "status_code":200}}

@router.post("/swiperdata/", summary="设置轮播图")  # 首页轮播图-POST
async def swiper_data():
    return {"meta":{"msg":"设置成功!", "status_code":200}}
