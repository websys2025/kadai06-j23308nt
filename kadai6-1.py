import requests

APP_ID = "77435cb40c39a246815b03bffba944bfea4f9ea3"
API_URL  = "http://api.e-stat.go.jp/rest/3.0/app/json/getStatsData?appId=&lang=J&statsDataId=0002119864&metaGetFlg=Y&cntGetFlg=N&explanationGetFlg=Y&annotationGetFlg=Y&sectionHeaderFlg=1&replaceSpChars=0"

params = {
    "appId": APP_ID,
    "statsDataId":"00500509",
    "lang": "J"  # 日本語を指定
}



#response = requests.get(API_URL, params=params)
response = requests.get(API_URL, params=params)
# Process the response
data = response.json()
print(data)