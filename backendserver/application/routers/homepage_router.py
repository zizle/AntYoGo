# _*_ coding: utf-8 _*_
'''
@File  :   homepage_router.py
@Time  :   2020-07-13 22:16:32
@Author:   Zizle 
'''

from fastapi import APIRouter
from .homepage import swiper

router = APIRouter()

router.include_router(swiper.router)
