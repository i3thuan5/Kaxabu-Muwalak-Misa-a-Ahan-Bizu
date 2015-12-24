from unittest.case import TestCase

from bizu.切錄音檔 import 切錄音檔


class 切錄音檔試驗(TestCase):

    @classmethod
    def setUpClass(cls):
        super(cls, cls).setUpClass()
        切錄音檔.準備教育部重編國語辭典的辭典佮語言模型()

    def test_句格式有照編號(self):
        句資料, _詞資料 = 切錄音檔._xls轉語句格式()
        self.assertIn('01', 句資料)

    def test_句格式(self):
        句資料, _詞資料 = 切錄音檔._xls轉語句格式()
        self.assertIn([
            ('語詞編號', '01A-001'), ('臺語', 'thâu ê tsoân-pō•'),
            ('華語', '頭（整個）'), ('Kaxabu', 'punu')
        ], 句資料['01'])

    def test_詞格式有照編號(self):
        _句資料, 詞資料 = 切錄音檔._xls轉語句格式()
        self.assertIn('01', 詞資料)

    def test_詞格式(self):
        _句資料, 詞資料 = 切錄音檔._xls轉語句格式()
        詞01 = 詞資料['01']
        self.assertIn([
            ('語詞編號', '01A-001')
        ], 詞01)
        self.assertIn([
            ('臺語', 'thâu ê tsoân-pō•')
        ], 詞01)
        self.assertIn([
            ('華語', '頭（整個）')
        ], 詞01)
        self.assertIn([
            ('Kaxabu', 'punu')
        ], 詞01)

    def test_檢查標仔資料(self):
        標仔資料, _辭典資料 = 切錄音檔._轉標仔佮辭典({
            '01': [
                [
                    ('語詞編號', '01A-001'), ('臺語', 'thâu ê tsoân-pō•'),
                    ('華語', '頭（整個）'), ('Kaxabu', 'punu')
                ]
            ]
        })
        self.assertEqual(
            標仔資料,
            {'01': ['01A-001，thâu_ê_tsoân-pō•，頭（整個），punu']}
        )

    def test_檢查辭典語詞編號(self):
        _標仔資料, 辭典資料 = 切錄音檔._轉標仔佮辭典({
            '01': [
                [('語詞編號', '01A-001')]
            ]
        })
        self.assertEqual(
            辭典資料,
            set(['01A-001 0 1 A 0 0 1'])
        )

    def test_檢查辭典臺語(self):
        _標仔資料, 辭典資料 = 切錄音檔._轉標仔佮辭典({
            '01': [
                [('臺語', 'thâu ê tsoân-pō•')]
            ]
        })
        self.assertEqual(
            辭典資料,
            set(['thâu_ê_tsoân-pō• tʰ au ʔ e ts uan p o'])
        )

    def test_檢查辭典Kaxabu(self):
        _標仔資料, 辭典資料 = 切錄音檔._轉標仔佮辭典({
            '01': [
                [('Kaxabu', 'punu')]
            ]
        })
        self.assertEqual(
            辭典資料,
            set(['punu p u n u'])
        )

    def test_檢查辭典華語(self):
        _標仔資料, 辭典資料 = 切錄音檔._轉標仔佮辭典({
            '01': [
                [('華語', '頭（整個）')]
            ]
        })
        self.assertEqual(
            辭典資料,
            set(['頭（整個） ㄊ ㄡ'])
        )

    def test_檢查辭典資料(self):
        _標仔資料, 辭典資料 = 切錄音檔._轉標仔佮辭典({
            '01': [
                [
                    ('語詞編號', '01A-001'), ('臺語', 'thâu ê tsoân-pō•'),
                    ('華語', '頭（整個）'), ('Kaxabu', 'punu')
                ]
            ]
        })
        self.assertEqual(
            辭典資料,
            set([
                '01A-001，thâu_ê_tsoân-pō•，頭（整個），punu 0 1 A 0 0 1 tʰ au ʔ e ts uan p o ㄊ ㄡ p u n u'
            ])
        )

    def test_仝款資料辭典出現一擺(self):
        _標仔資料, 辭典資料 = 切錄音檔._轉標仔佮辭典({
            '01': [
                [
                    ('語詞編號', '01A-001'), ('臺語', 'thâu ê tsoân-pō•'),
                    ('華語', '頭（整個）'), ('Kaxabu', 'punu')
                ],
                [
                    ('語詞編號', '01A-001'), ('臺語', 'thâu ê tsoân-pō•'),
                    ('華語', '頭（整個）'), ('Kaxabu', 'punu')
                ]
            ]
        })
        self.assertEqual(len(辭典資料), 1)
