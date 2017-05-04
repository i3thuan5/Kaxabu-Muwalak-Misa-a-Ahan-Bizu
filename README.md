# Kaxabu Muwalak Misa A Ahan Bizu
本網站內容取自《噶哈巫語分類辭典》一書，謹此致謝。

書籍資訊：

* 原著：潘永歷
* 總編輯：董忠司
* 主編：陳嬿庄
* 編輯：潘正浩、林鴻瑞、涂文欽、朱恩成
* 出版單位：南投縣埔里鎮守城社區發展協會
* 出版年：2015年
* ISBN：9789869248808

## 辭典資料
* 文本：`《噶哈巫語分類辭典》EXCEL版本.xls`
* 聲音：[下載](https://www.dropbox.com/sh/8iqtr7eayb93lws/AAANlE-qleOKHIibQKnCBgVNa?dl=0)

## 相關連結
* 2015/11/29在守城新公廳的[新書發表會](https://www.facebook.com/events/1662129040716123/)
* 有語音功能的[線上辭典](http://kaxabu.意傳.台灣/)

## 資料整理
調整原始檔音量
```
sudo apt-get install normalize-audio -y
find . -type f -exec normalize-audio {} \;
```


## 切錄音檔（原本的失敗構想）
希望會使逐句分開，逐詞嘛分開，所以愛做兩擺。

1. xls檔
2. 語句格式檔。照講的順序排，辨識單位放仝一個陣列
  * 一句
    * [('語詞編號','01A-001'),('臺語','thâu ê tsoân-pō•'),('華語','頭（整個）'),('Kaxabu','punu')]
  * 一詞
	* [('語詞編號','01A-001')]
	* [('臺語譯解','thâu ê tsoân-pō•')]
	* [('中文譯解','頭（整個）')]
	* [('噶哈巫語教材標記法','punu')]
3. 語料label標仔檔，佮dict辭典檔。逐個內容用逗號隔開，空白換做底線
  * 一句
    * 01A-001，thâu_ê_tsoân-pō•，頭（整個），punu 0 1 A 0 0 1 tʰ au e ts uan p o ㄊ ㄡ p u n u
  * 一詞
	* 01A-001 0 1 A 0 0 1
	* thâu_ê_tsoân-pō• tʰ au e ts uan p o
	* 頭（整個） ㄊ ㄡ
	* punu p u n u
4. HTK的mlf檔

## 做法
### 音標轉wav
到音檔目錄執行以下`bash`
```bash
mkdir wav ; find . -name '*mp3' | egrep -v "25|26" | awk '{print "avconv -i "$0" "$0}'| sed 's/3 \./3 wav/g' | sed 's/\.[^ 1-9]*mp3$/.wav/g' | bash
```

### 下載相關資料
華語辭典
```
git clone https://github.com/g0v/moedict-data.git
```

### 設定python環境
```
sudo apt-get install -y liblapack-dev libblas-dev gfortran praat
virtualenv venv --python=python3 ; . venv/bin/activate ; pip install --upgrade pip
pip install -r requirements.txt 
```

### 設定參數
改`bizu/參數.py`，填上面`轉wav`和`git clone`的路徑
```
xls所在 = '路徑/《噶哈巫語分類辭典》EXCEL版本.xls'
教育部重編國語辭典json所在 = 'moedict-data路徑/dict-revised.json'
wav音檔目錄= '路徑/wav/'
```

### 執行
```
python 走.py
```

### 人工檢查音檔有切著無
```
python bizu/敆音檔.py
```
才去`檢查音檔有切好無`照分類聽
* 聽編號佮華語是毋是學姐的聲
* 臺語佮kaxabu是長老的聲

