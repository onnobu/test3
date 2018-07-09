import urllib.request, urllib.parse

## 初期化
url = "https://api.fcoin.com/v2/public/currencies"

## 初期化後の変数の中身
print(url)

with urllib.request.urlopen(url) as res:
         html = res.read().decode("utf-8")
         print(html)