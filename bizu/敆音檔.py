from 臺灣言語工具.語音辨識.聲音檔 import 聲音檔
from os import makedirs
from os.path import join, isdir, abspath, dirname
from posix import listdir


def 接檔案(原本音檔, 目錄音檔):
    makedirs(目錄音檔, exist_ok=True)
    for 資料夾 in sorted(listdir(原本音檔)):
        所在 = join(原本音檔, 資料夾)
        if isdir(所在):
            全部音檔合起來 = None
            for 第幾個 in range(4):
                for 檔案 in sorted(listdir(所在))[第幾個::4]:
                    這個音檔 = 聲音檔.對檔案讀(join(所在, 檔案))
                    try:
                        全部音檔合起來 = 全部音檔合起來.接(這個音檔)
                    except:
                        全部音檔合起來 = 這個音檔
                結果檔案 = join(目錄音檔, '{}-{}.wav'.format(資料夾, 第幾個))
                with open(結果檔案, 'wb') as 檔案:
                    檔案.write(全部音檔合起來.wav格式資料())

if __name__ == '__main__':
    接檔案(
        '/home/pigu/Dropbox/Kaxabu Muwalak Misa A Ahan Bizu/好的',
        join(abspath(dirname(__file__)), '..', '檢查音檔有切好無')
    )
