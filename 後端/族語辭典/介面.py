from django.core import serializers
from django.http.response import JsonResponse
from 族語辭典.models import 分類辭典


def 顯示全部資料(request):
    全部資料 = list(分類辭典.objects.all().order_by('語詞編號').values()[:100])
    return JsonResponse({
        '全部資料': 全部資料
    })


def 查關鍵字(request):
    try:
        關鍵字 = request.GET['關鍵字']
    except:
        return 顯示全部資料(request)
    關鍵字
    return JsonResponse({'22': '@@'})
