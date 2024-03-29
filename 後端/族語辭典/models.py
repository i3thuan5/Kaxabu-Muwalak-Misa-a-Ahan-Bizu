# -*- coding: utf-8 -*-
import re
from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage


class NgaungawStorage(S3Boto3Storage):
    bucket_name = 'kaxabu-muwalak-misa-a-ahan-bizu'


class 分類辭典(models.Model):
    語詞編號 = models.CharField(max_length=200, unique=True)
    噶哈巫語教材標記法 = models.CharField(max_length=200, blank=True)
    噶哈巫語潘永歷標記法 = models.CharField(max_length=200, blank=True)
    中文譯解 = models.CharField(max_length=200, blank=True)
    臺語譯解 = models.CharField(max_length=200, blank=True)
    備註 = models.CharField(max_length=200, blank=True)
    出處 = models.CharField(max_length=200, blank=True)

    語詞編號音檔 = models.FileField(
        storage=NgaungawStorage(), editable=False, null=True
    )
    臺語音檔 = models.FileField(
        storage=NgaungawStorage(), editable=False, null=True
    )
    華語音檔 = models.FileField(
        storage=NgaungawStorage(), editable=False, null=True
    )
    噶哈巫音檔 = models.FileField(
        storage=NgaungawStorage(), editable=False, null=True
    )

    切語詞編號 = re.compile(r'(\d\d[A-Z]{0,1})-(\d\d\d)')

    def __str__(self):
        return self.語詞編號

    def 分類(self):
        分類, _編號 = self.分類kah編號()
        return 分類

    def 編號(self):
        _分類, 編號 = self.分類kah編號()
        return 編號

    def 分類kah編號(self):
        切 = self.切語詞編號.match(self.語詞編號)
        分類 = 切.group(1)
        編號 = int(切.group(2))
        return 分類, 編號
