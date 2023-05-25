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
        huein = self.client.get('聽?{}'.format(
            urlencode({
                '語詞編號': '01H-005',
                '內容': '噶哈巫',
            })
        ))
        self.assertEqual(huein.status_code, 302)

    def test_聽音檔編號毋著(self):
        huein = self.client.get('聽?{}'.format(
            urlencode({
                '語詞編號': '01H-10005',
                '內容': '噶哈巫',
            })
        ))
        self.assertEqual(huein.status_code, 404)

    def test_顯示全部資料(self):
        huein = self.client.get('')
        self.assertEqual(huein.status_code, 200)

    def test_查(self):
        huein = self.client.get('聽?{}'.format(
            urlencode({
                '關鍵字': '聲',
            })
        ))
        self.assertEqual(huein.status_code, 200)
