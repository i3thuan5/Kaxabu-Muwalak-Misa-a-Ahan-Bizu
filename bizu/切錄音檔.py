import xlrd
from bizu.參數 import xls所在


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
