from django.core.management.base import BaseCommand
from django.db import transaction
from os.path import basename, dirname, join

from 族語辭典.models import 分類辭典


class Command(BaseCommand):
    ngawngaw_list = join(
        dirname(__file__), '..',
        'ngawngaw.txt'
    )

    @transaction.atomic
    def handle(self, *args, **options):
        hunlui = {}
        with open(self.ngawngaw_list, 'rt') as tong:
            for tsua in tong.readlines():
                tsua = tsua.strip()
                if not tsua:
                    continue
                phooamia = basename(dirname(tsua))
                try:
                    hunlui[phooamia].append(tsua)
                except KeyError:
                    hunlui[phooamia] = [tsua]
        for 詞 in 分類辭典.objects.all():
            lui = hunlui[詞.分類()]
            ho = (詞.編號() - 1) * 4
            詞.語詞編號音檔 = lui[ho+0]
            詞.臺語音檔 = lui[ho+1]
            詞.華語音檔 = lui[ho+2]
            詞.噶哈巫音檔 = lui[ho+3]
            詞.save()
