# -*- coding: utf-8 -*-
from django.conf.urls import url
from 族語辭典.介面 import 顯示全部資料
from 族語辭典.介面 import 查關鍵字
from 族語辭典.介面 import 聽音檔


urlpatterns = [
    url(r'^$', 顯示全部資料),
    url(r'^查$', 查關鍵字),
    url(r'^聽$', 聽音檔),
]
