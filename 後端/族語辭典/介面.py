from django.db.models.query_utils import Q
from django.http import JsonResponse, HttpResponseBadRequest
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from 族語辭典.models import 分類辭典


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
    except KeyError:
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
    except KeyError:
        return HttpResponseBadRequest('參數ài「語詞編號」kah「內容」')
    詞 = get_object_or_404(分類辭典, 語詞編號=語詞編號)
    if 內容 == '語詞編號':
        音檔 = 詞.語詞編號音檔
    elif 內容 == '臺語':
        音檔 = 詞.臺語音檔
    elif 內容 == '華語':
        音檔 = 詞.華語音檔
    elif 內容 == '噶哈巫':
        音檔 = 詞.噶哈巫音檔
    else:
        return HttpResponseBadRequest('無這內容～')
    return HttpResponseRedirect(音檔.url)
