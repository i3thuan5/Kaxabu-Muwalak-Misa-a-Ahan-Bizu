from unittest.case import TestCase

from bizu.切錄音檔 import 切錄音檔


class 切錄音檔試驗(TestCase):

    def test_句格式(self):
        句資料, _詞資料 = 切錄音檔._xls轉語句格式()
        self.assertIn([
            ('語詞編號', '01A-001'), ('臺語', 'thâu ê tsoân-pō•'),
            ('華語', '頭（整個）'), ('Kaxabu', 'punu')
        ], 句資料)

    def test_詞格式(self):
        _句資料, 詞資料 = 切錄音檔._xls轉語句格式()
        self.assertIn([
            ('語詞編號', '01A-001')
        ], 詞資料)
        self.assertIn([
            ('臺語', 'thâu ê tsoân-pō•')
        ], 詞資料)
        self.assertIn([
            ('華語', '頭（整個）')
        ], 詞資料)
        self.assertIn([
            ('Kaxabu', 'punu')
        ], 詞資料)
