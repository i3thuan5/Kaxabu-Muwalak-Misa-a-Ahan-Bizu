from django.core import serializers
from django.http.response import JsonResponse
from 族語辭典.models import 分類辭典
from django.views.decorators.csrf import csrf_exempt


def 顯示全部資料(request):
    全部資料 = list(分類辭典.objects.all().order_by('語詞編號').values()[:1])
    return JsonResponse({
        '符合資料': 全部資料
    })


def 查關鍵字(request):
    try:
        關鍵字 = request.GET['關鍵字'].strip()
    except:
        return 顯示全部資料(request)
    if 關鍵字=='':
        return 顯示全部資料(request)
    
    全部資料 = list(分類辭典.objects.filter(語詞編號__contains=關鍵字).order_by('語詞編號').values()[:10])
    return JsonResponse({
        '符合資料': 全部資料
    })