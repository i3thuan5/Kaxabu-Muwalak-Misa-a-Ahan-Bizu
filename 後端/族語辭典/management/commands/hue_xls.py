from django.core.management.base import BaseCommand
import xlrd
import re
from django.core.exceptions import ValidationError
from os.path import dirname, join

from 族語辭典.models import 分類辭典


class Command(BaseCommand):
    xls所在 = join(
        dirname(__file__), '..', '..', '..', '..',
        '《噶哈巫語分類辭典》EXCEL版本.xls'
    )

    def handle(self, *args, **options):
        表格檔 = xlrd.open_workbook(self.xls所在)
        表格 = 表格檔.sheet_by_name('工作表1')
        表格欄位 = 表格.row_values(0)
        for 第幾逝 in range(1, 表格.nrows):
            資料 = dict(zip(表格欄位, 表格.row_values(第幾逝)))
            資料.pop('')
            if re.match(r'\d\d[A-Z]{0,1}-\d{3}\Z', 資料['語詞編號']):
                詞條 = 分類辭典.objects.create(**資料)
                try:
                    詞條.full_clean()
                except ValidationError:
                    print(資料)
                else:
                    詞條.save()
