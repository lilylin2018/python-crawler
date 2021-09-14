#抓取網頁原始碼(HTML)

import urllib.request as req
url = "https://tw.stock.yahoo.com/_td-stock/api/resource/StockServices.stockList;autoRefresh=1630751429221;fields=avgPrice%2Corderbook;symbols=2330.TW?bkt=tw-qsp-exp-no2-1&device=desktop&ecma=modern&feature=ecmaModern%2CuseNewQuoteTabColor&intl=tw&lang=zh-Hant-TW&partner=none&prid=559itmdgj6ik8&region=TW&site=finance&tz=Asia%2FTaipei&ver=1.2.1103&returnMeta=true"
#建立一個Request物件，附加Headers的資訊
request = req.Request(url,headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
# print(data)

#解析原始碼
import json
data = json.loads(data)
high = data["data"][0]["regularMarketDayHigh"]
low = data["data"][0]["regularMarketDayLow"]
open = data["data"][0]["regularMarketOpen"]
preclose = data["data"][0]["regularMarketPreviousClose"]
time = data["data"][0]["regularMarketTime"]
name = data["data"][0]["symbolName"]
price = data["data"][0]["price"]

print("名稱:",name)
print("時間:",time)
print("成交:",price)
print("開盤:",open)
print("最高:",high)
print("最低:",low)
print("昨收:",preclose)

