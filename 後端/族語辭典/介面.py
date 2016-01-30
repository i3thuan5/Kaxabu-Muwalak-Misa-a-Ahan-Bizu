from os.path import join, getsize, basename, dirname
from posix import listdir
import re

from django.db.models.query_utils import Q
from django.http.response import JsonResponse, HttpResponse
from 族語辭典.models import 分類辭典

音檔目錄 = join(dirname(__file__), '..', '..', '好的')


def _整理詞條(詞條要求):
    return list(詞條要求.values()[:])


def 顯示全部資料(request):
    全部資料 = _整理詞條(分類辭典.objects.all().order_by('語詞編號'))
    return JsonResponse({
        '符合資料': 全部資料
    })


def 查關鍵字(request):
    try:
        關鍵字 = request.GET['關鍵字'].strip()
    except:
        return 顯示全部資料(request)
    if 關鍵字 == '':
        return 顯示全部資料(request)

    全部資料 = _整理詞條(
        分類辭典.objects.filter(
            Q(語詞編號__contains=關鍵字) |
            Q(噶哈巫語教材標記法__contains=關鍵字) |
            Q(噶哈巫語潘永歷標記法__contains=關鍵字) |
            Q(中文譯解__contains=關鍵字) |
            Q(臺語譯解__contains=關鍵字) |
            Q(備註__contains=關鍵字) |
            Q(出處__contains=關鍵字)
        ).order_by('語詞編號')
    )
    return JsonResponse({
        '符合資料': 全部資料
    })


def 聽音檔(request):
    try:
        語詞編號 = request.GET['語詞編號'].strip()
        內容 = request.GET['內容'].strip()
    except:
        return HttpResponse('參數無夠')
    切語詞編號 = re.match(r'(\d\d[A-Z]{0,1})-(\d\d\d)', 語詞編號)
    try:
        分類 = 切語詞編號.group(1)
        編號 = int(切語詞編號.group(2))
        第幾個 = (編號 - 1) * 4
    except:
        return HttpResponse('語詞編號格式有問題')
    if 內容 == '語詞編號':
        第幾個 += 0
    elif 內容 == '臺語':
        第幾個 += 1
    elif 內容 == '華語':
        第幾個 += 2
    elif 內容 == '噶哈巫':
        第幾個 += 3
    音檔所在 = _音檔所在(分類, 第幾個)
    print(分類, 編號, 第幾個, basename(音檔所在))
    try:
        with open(音檔所在, "rb") as 檔案:
            連線回應 = HttpResponse()
            連線回應.write(檔案.read())
            連線回應['Content-Type'] = 'audio/wav'
            連線回應['Content-Length'] = getsize(音檔所在)
            return 連線回應
    except:
        return HttpResponse(
            '音檔無存在！！分類：{}，編號：{}'.format(
                分類, 編號)
        )


def _音檔所在(分類, 第幾個):
    分類目錄 = join(音檔目錄, 分類)
    for 第幾個檔名, 檔名 in enumerate(sorted(listdir(分類目錄))):
        if 第幾個檔名 == 第幾個:
            return join(分類目錄, 檔名)
