from django.test import TestCase
from django.core.management import call_command
from urllib.parse import urlencode

class TshiThiann(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        call_command('hue_xls')
        call_command('hue_imtong')

    def test_聽音檔(self):
        self.client.get('聽?{}'.format(
            urlencode({
                '語詞編號': '01H-005',
                '內容': '噶哈巫',
            })
        ))
    def test_顯示全部資料(self):
        顯示全部資料
        self.client.get('聽?{}'.format(
            urlencode({
                '語詞編號': '01H-005',
                '內容': '噶哈巫',
            })
        ))
    def test_查(self):
        查
        self.client.get('聽?{}'.format(
            urlencode({
                '語詞編號': '01H-005',
                '內容': '噶哈巫',
            })
        ))