from django.db.models.query_utils import Q
from django.http.response import JsonResponse
from 族語辭典.models import 分類辭典


def _整理詞條(詞條要求):
    return list(詞條要求.values()[:200])


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
