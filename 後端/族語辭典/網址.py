# -*- coding: utf-8 -*-
from django.urls import path
from 族語辭典.介面 import 顯示全部資料
from 族語辭典.介面 import 查關鍵字
from 族語辭典.介面 import 聽音檔


urlpatterns = [
    path('', 顯示全部資料),
    path('查', 查關鍵字),
    path('聽', 聽音檔),
]
