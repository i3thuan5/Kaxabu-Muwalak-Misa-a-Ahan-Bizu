from collections import OrderedDict
from itertools import chain
import json
from os import makedirs
from os.path import dirname, abspath, join
from posix import listdir
import re

from praatinterface import PraatLoader
from sklearn import svm
import xlrd


from bizu.參數 import xls所在
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.轉物件音家私 import 轉物件音家私
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音
from 臺灣言語工具.解析整理.字物件篩仔 import 字物件篩仔
from 臺灣言語工具.音標系統.閩南語.教會羅馬字音標 import 教會羅馬字音標
from bizu.參數 import 教育部重編國語辭典json所在
from 臺灣言語工具.辭典.型音辭典 import 型音辭典
from 臺灣言語工具.語言模型.實際語言模型 import 實際語言模型
from 臺灣言語工具.基本元素.詞 import 詞
from 臺灣言語工具.音標系統.官話.官話注音符號 import 官話注音符號
from 臺灣言語工具.系統整合.程式腳本 import 程式腳本
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.斷詞.拄好長度辭典揣詞 import 拄好長度辭典揣詞
from 臺灣言語工具.解析整理.集內組照排 import 集內組照排
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.解析整理.揀集內組 import 揀集內組
from 臺灣言語工具.語音辨識.HTK工具.HTK辨識模型訓練 import HTK辨識模型訓練
from bizu.參數 import wav音檔目錄
from 臺灣言語工具.基本元素.公用變數 import 標點符號
from bizu.標題對應 import 標題對應
from 臺灣言語工具.語音辨識.HTK工具.HTK辨識模型 import HTK辨識模型
from 臺灣言語工具.語音辨識.聲音檔 import 聲音檔
from 臺灣言語工具.語音辨識.恬音判斷 import 恬音判斷

a = 0


class 切錄音檔(程式腳本):
    華語辭典 = None
    華語解釋 = re.compile('[（(].*[）)]')
    專案目錄 = join(dirname(abspath(__file__)), '..')
    查某查甫音懸門檻 = 185.0
    上短秒數 = 0.3

    @classmethod
    def 切音檔(cls, 暫存目錄=join(專案目錄, '暫存')):
        句資料, 詞資料 = cls._xls轉語句格式()
        makedirs(暫存目錄, exist_ok=True)
        cls._辨識(句資料, join(暫存目錄, '句'))
        cls._辨識(詞資料, join(暫存目錄, '詞'))
        cls._訓練HTK(暫存目錄)

    @classmethod
    def _訓練恬音模型(cls):
        訓練目錄 = join(cls.專案目錄, '訓練音檔')
        題目 = []
        答案 = []
        for 類型 in sorted(listdir(訓練目錄)):
            類型目錄 = join(訓練目錄, 類型)
            for 音檔 in sorted(listdir(類型目錄)):
                音檔所在 = join(類型目錄, 音檔)
                音檔 = 聲音檔.對檔案讀(音檔所在)
                for 音框 in 音檔.全部音框():
                    特徵 = 恬音判斷.算特徵參數(音框)
                    題目.append(cls._特徵轉陣列(特徵))
                    答案.append(類型)
        cls.恬音模型 = svm.SVC()
        cls.恬音模型.fit(題目, 答案)

    @classmethod
    def _特徵轉陣列(cls, 特徵):
        if 特徵['相關係數'] is not None:
            return [特徵['平方平均'], 特徵['過零機率'], 特徵['相關係數']]
        return [特徵['平方平均'], 特徵['過零機率'], 100.0]

    @classmethod
    def _無音切全部細音檔(cls):
        cls._訓練恬音模型()
        for 編號 in range(1, 25):
            cls._無音切一個細音檔(編號)
            cls._照性別合一組音檔(編號)

    @classmethod
    def _無音切一個細音檔(cls, 編號):
        音檔 = 聲音檔.對檔案讀(join(wav音檔目錄, '{:02}.wav'.format(編號)))

        def 有音無(音框):
            #             print(音框)
            特徵 = 恬音判斷.算特徵參數(音框)
# 結果=特徵['平方平均'] >= 2000.0 and 特徵['過零機率'] < 0.25 # and 特徵['相關係數'] > 0.70
            標仔 = cls.恬音模型.predict([cls._特徵轉陣列(特徵)])[0]
            結果 = (標仔 == '有')
            global a
#             print(a * 0.02, 結果, 特徵)
            a += 1
            return 結果

        細音檔陣列 = 音檔.照函式切音(有音無)
        音檔目錄 = cls._編號分割音檔目錄(編號)
        makedirs(音檔目錄, exist_ok=True)
        號碼 = 0
        合音檔 = 音檔.產生仝參數空聲音檔()
        for 細音檔 in 細音檔陣列:
            if 細音檔.時間長度() >= cls.上短秒數 and len(合音檔.wav音值資料()) > 0:
                with open(join(音檔目錄, '{:04}.wav'.format(號碼)), 'wb') as 檔案:
                    檔案.write(合音檔.wav格式資料())
                合音檔 = 合音檔.產生仝參數空聲音檔()
                號碼 += 1
            合音檔 = 合音檔.接(細音檔)
        if 合音檔.時間長度() >= cls.上短秒數:
            with open(join(音檔目錄, '{:04}.wav'.format(號碼)), 'wb') as 檔案:
                檔案.write(合音檔.wav格式資料())
            號碼 += 1
        print(編號, '到', 號碼 - 1)

    @classmethod
    def _編號分割音檔目錄(cls, 編號):
        return join(cls.專案目錄, '音檔分割', '{:02}'.format(編號))

    @classmethod
    def _照性別合一組音檔(cls, 編號):
        編號音檔目錄 = cls._編號分割音檔目錄(編號)
        合做伙目錄 = join(cls.專案目錄, '音檔合做伙')
        makedirs(合做伙目錄, exist_ok=True)
        頂一個查甫查某 = None
        號碼 = 0
        合音檔 = 聲音檔.對檔案讀(join(編號音檔目錄, '0000.wav')).產生仝參數空聲音檔()
        for 檔名 in sorted(listdir(編號音檔目錄)):
            if re.match('\d+.wav\Z', 檔名):
                這馬查甫查某 = cls._檢查查甫查某(join(編號音檔目錄, 檔名))
                if 頂一個查甫查某 != 這馬查甫查某:
                    if 頂一個查甫查某 is not None:
                        with open(join(
                                合做伙目錄, '{:02}-{:04}-{}.wav'.format(編號, 號碼, 頂一個查甫查某)), 'wb'
                        ) as 檔案:
                            檔案.write(合音檔.wav格式資料())
                        合音檔 = 合音檔.產生仝參數空聲音檔()
                        號碼 += 1
                    頂一個查甫查某 = 這馬查甫查某
                音檔 = 聲音檔.對檔案讀(join(編號音檔目錄, 檔名))
                合音檔 = 合音檔.接(音檔)
        with open(join(
                合做伙目錄, '{:02}-{:04}-{}.wav'.format(編號, 號碼, 頂一個查甫查某)), 'wb'
        ) as 檔案:
            檔案.write(合音檔.wav格式資料())

    @classmethod
    def _檢查查甫查某(cls, 檔名):
        pl = PraatLoader()
        音懸結果 = pl.run_script('pitch.praat', 檔名)
        查某 = 0
        查甫 = 0
#         print(檔名, 音懸結果)
        for 資料 in pl.read_praat_out(音懸結果).values():
            音懸 = 資料['Pitch']
            if 音懸 != 0:
                if 音懸 > cls.查某查甫音懸門檻:
                    查某 += 1
                else:
                    查甫 += 1
        if 查某 >= 查甫:
            return '查某'
        return '查甫'

    @classmethod
    def _訓練HTK(cls, 源頭):
        音檔目錄 = wav音檔目錄
        標仔目錄 = join(源頭, '句', '標仔')
        音節聲韻對照檔 = join(源頭, '句', '辭典.dict')
        資料目錄 = join(源頭, 'HTK訓練')
        辨識模型 = HTK辨識模型訓練.訓練原本標音辨識模型(音檔目錄, 標仔目錄, 音節聲韻對照檔, 資料目錄)
        辨識模型.存資料佇(join(源頭, 'HTK模型'))

    @classmethod
    def _HTK對齊(cls):
        源頭 = join(dirname(abspath(__file__)), '暫存')
        模型 = HTK辨識模型(
            音節聲韻對照檔=join(源頭, '句', '辭典.dict'),
            聲韻類檔=join(源頭, '句/HTK訓練/原始標音目錄/原來聲韻類檔.list'),
            模型參數檔=join(源頭, '句/HTK訓練/原始標音目錄/初步模型檔-重估/05/初步模型檔.macro')
        )
        模型.對齊音節(
            join(源頭, '句/HTK訓練/原始標音目錄/原來音節檔.mlf'),
            join(源頭, '句/HTK訓練/全部特徵檔.scp'),
            join(源頭, '對齊音節1mix-05')
        )

    @classmethod
    def _辨識(cls, 資料, 暫存目錄):
        標仔, 辭典 = cls._轉標仔佮辭典(資料)
        標仔目錄 = cls._細項目錄(暫存目錄, '標仔')
        for 編號, 資料 in 標仔.items():
            cls._陣列寫入檔案(join(標仔目錄, '{}.lab'.format(編號)), 資料)
        cls._陣列寫入檔案(join(暫存目錄, '辭典.dict'), sorted(辭典))

    @classmethod
    def _xls轉語句格式(cls):
        表格檔 = xlrd.open_workbook(xls所在)
        表格 = 表格檔.sheet_by_name('工作表1')
        表格欄位 = {}
        for 第幾個, 資料 in enumerate(表格.row_values(0)):
            表格欄位[資料] = 第幾個
        句資料 = OrderedDict()
        for 編號 in range(1, 25):
            編號字串 = '{:02}'.format(編號)
            句資料[編號字串] = []
        無編號資料 = []
        for 第幾逝 in range(1, 表格.nrows):
            逝 = 表格.row_values(第幾逝)
            語詞編號 = 逝[表格欄位['語詞編號']].strip()
            Kaxabu = 逝[表格欄位['噶哈巫語教材標記法']]
            if Kaxabu != '':
                華語 = 逝[表格欄位['中文譯解']]
                臺語 = 逝[表格欄位['臺語譯解']]
                這筆資料 = [
                    ('語詞編號', 語詞編號), ('臺語', 臺語),
                    ('華語', 華語), ('Kaxabu', Kaxabu)
                ]
            else:
                try:
                    無編號資料.append(標題對應[語詞編號])
                except:
                    pass
                continue
            編號字串 = 語詞編號[:2]
            句資料[編號字串].extend(無編號資料)
            無編號資料 = []
            句資料[編號字串].append(這筆資料)

        詞資料 = OrderedDict()
        for 編號字串, 內容 in 句資料.items():
            詞資料[編號字串] = []
            for 這筆資料 in 內容:
                for 詞 in 這筆資料:
                    詞資料[編號字串].append([詞])

        return 句資料, 詞資料

    @classmethod
    def _轉標仔佮辭典(cls, 語句格式):
        標仔資料, 辭典資料 = {}, {'sil sil'}
        for 編號, 語句陣列 in 語句格式.items():
            標仔資料[編號] = ['sil']
            for 語句資料 in 語句陣列:
                語句標仔陣列 = []
                辨識單位 = []
                for 語言, 語句 in 語句資料:
                    語句標仔陣列.append(語句.replace(' ', '_'))
                    if 語言 == '語詞編號':
                        辨識單位.append(語句.replace('-', ''))
                    elif 語言 == '臺語':
                        try:
                            處理語句 = 文章粗胚.建立物件語句前處理減號(教會羅馬字音標, 語句)
                            句物件 = 拆文分析器.產生對齊句(處理語句, 處理語句)
                            預設音物件 = 轉物件音家私.轉音(教會羅馬字音標, 句物件)
                            音值物件 = 轉物件音家私.轉音(臺灣閩南語羅馬字拼音, 預設音物件, 函式='音值')
                            音值陣列 = []
                            for 字物件 in 字物件篩仔.篩出字物件(音值物件):
                                try:
                                    音值陣列.extend(字物件.音[:2])
                                except:
                                    pass
                            辨識單位.append(音值陣列)
                        except Exception as 錯誤:
                            print(錯誤)
                            print(語句)
                            辨識單位.append('X' * (len(語句) // 3 + 1))
                    elif 語言 == '華語':
                        辨識單位.append(cls._華語漢字轉注音(文章粗胚.建立物件語句前減號變標點符號(語句)))
                    else:
                        辨識單位.append(語句)
                    辨識單位.append(['sil'])
                標仔 = '，'.join(語句標仔陣列)
                標仔資料[編號].append(cls._處理孤雙引號(標仔))
                標仔資料[編號].append('sil')
                辨識單位.pop()
                辭典資料.add(
                    cls._處理孤雙引號(
                        '{} {}'.format(
                            標仔,
                            ' '.join(
                                cls._處理音素(
                                    chain.from_iterable(辨識單位))
                            )
                        )
                    )
                )
        return 標仔資料, 辭典資料

    @classmethod
    def _處理孤雙引號(cls, 語句):
        return 語句.replace("'", "hʔ").replace('"', "")

    @classmethod
    def _處理音素(cls, 音素陣列):
        for 音素 in 音素陣列:
            if re.search(r'^[0-9]', 音素):
                yield '音' + 音素
            elif 音素 != '' and 音素 not in 標點符號:
                yield 音素

    @classmethod
    def _華語漢字轉注音(cls, 語句):
        cls.準備教育部重編國語辭典的辭典佮語言模型()
        揣詞結果, _分數, _詞數 = 拄好長度辭典揣詞.揣詞(
            cls.華語辭典, 拆文分析器.建立組物件(cls.華語解釋.sub('', 語句)))
        揀好結果 = 揀集內組.揀(
            集內組照排.排好(lambda 組物件: 物件譀鏡.看型(組物件), 揣詞結果)
        )
        for 字物件 in 字物件篩仔.篩出字物件(揀好結果):
            注音符號 = 官話注音符號(字物件.音)
            if 注音符號.聲 is not None:
                yield 注音符號.聲
            if 注音符號.韻 is not None:
                yield 注音符號.韻

    @classmethod
    def 準備教育部重編國語辭典的辭典佮語言模型(cls):
        if cls.華語辭典 is None:
            cls.華語辭典 = 型音辭典(1)
            cls.華語語言模型 = 實際語言模型(1)
            for 資料 in cls._提教育部重編國語辭典的注音():
                漢字 = 資料['漢字'].replace('，', '')
                注音 = 資料['注音']
                try:
                    組物件 = 拆文分析器.產生對齊組(漢字, 注音)
                    for 字物件 in 字物件篩仔.篩出字物件(組物件):
                        cls.華語辭典.加詞(詞([字物件]))
                        cls.華語語言模型.看(字物件)
                except:
                    pass

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
        return 全部資料
