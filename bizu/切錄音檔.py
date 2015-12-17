from itertools import chain
import json
import re

import xlrd


from bizu.參數 import xls所在
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.轉物件音家私 import 轉物件音家私
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.解析整理.字物件篩仔 import 字物件篩仔
from 臺灣言語工具.音標系統.閩南語.教會羅馬字音標 import 教會羅馬字音標
from bizu.參數 import 教育部重編國語辭典json所在


class 切錄音檔:

    @classmethod
    def _xls轉語句格式(cls):
        表格檔 = xlrd.open_workbook(xls所在)
        表格 = 表格檔.sheet_by_name('工作表1')
        表格欄位 = {}
        for 第幾個, 資料 in enumerate(表格.row_values(0)):
            表格欄位[資料] = 第幾個
        句資料 = []
        詞資料 = []
#         for 第幾逝 in range(1, 表格.nrows):
        for 第幾逝 in range(1, 10):
            逝 = 表格.row_values(第幾逝)
            語詞編號 = 逝[表格欄位['語詞編號']]
            Kaxabu = 逝[表格欄位['噶哈巫語教材標記法']]
            華語 = 逝[表格欄位['中文譯解']]
            臺語 = 逝[表格欄位['臺語譯解']]
            這筆資料 = [
                ('語詞編號', 語詞編號), ('臺語', 臺語),
                ('華語', 華語), ('Kaxabu',  Kaxabu)
            ]
            句資料.append(這筆資料)
            for 詞 in 這筆資料:
                詞資料.append([詞])
        return 句資料, 詞資料

    @classmethod
    def _轉標仔佮辭典(cls, 語句格式):
        標仔資料, 辭典資料 = [], set()
        for 語句資料 in 語句格式:
            語句陣列 = []
            辨識單位 = []
            for 語言, 語句 in 語句資料:
                語句陣列.append(語句.replace(' ', '_'))
                if 語言 == '語詞編號':
                    辨識單位.append(語句.replace('-', ''))
                elif 語言 == '臺語':
                    句物件 = 拆文分析器.產生對齊句(語句, 語句)
                    預設音物件 = 轉物件音家私.轉音(教會羅馬字音標, 句物件)
                    音值物件 = 轉物件音家私.轉音(臺灣閩南語羅馬字拼音, 預設音物件, 函式='音值')
                    音值陣列 = []
                    for 字物件 in 字物件篩仔.篩出字物件(音值物件):
                        try:
                            音值陣列.extend(字物件.音[:2])
                        except:
                            pass
                    辨識單位.append(音值陣列)
                else:
                    辨識單位.append(語句)
            標仔 = '，'.join(語句陣列)
            標仔資料.append(標仔)
            辭典資料.add(
                '{} {}'.format(標仔, ' '.join(chain.from_iterable(辨識單位)))
            )
        return 標仔資料, 辭典資料

    @classmethod
    def _提教育部重編國語辭典的注音(cls):
        全部資料 = []
        with open(教育部重編國語辭典json所在) as 檔案:
            for 一筆json in json.load(檔案):
                if re.search('[[{]', 一筆json['title']) is None:
                    for 解釋 in 一筆json['heteronyms']:
                        if 'bopomofo' in 解釋:
                            全部資料.append(
                                {'漢字': 一筆json['title'], '注音': 解釋['bopomofo']}
                            )
                            print(全部資料[-1])
        return 全部資料
