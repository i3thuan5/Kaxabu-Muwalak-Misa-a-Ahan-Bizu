# -*- coding: utf-8 -*-
from django.db import models


class 分類辭典(models.Model):
    語詞編號 = models.CharField(max_length=200, unique=True)
    噶哈巫語教材標記法 = models.CharField(max_length=200, blank=True)
    噶哈巫語潘永歷標記法 = models.CharField(max_length=200, blank=True)
    中文譯解 = models.CharField(max_length=200, blank=True)
    臺語譯解 = models.CharField(max_length=200, blank=True)
    備註 = models.CharField(max_length=200, blank=True)
    出處 = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.語詞編號
