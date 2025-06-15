# e-statからチーズの需給表
# エンドポイント：https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData


import requests
import pandas as pd

APP_ID = "77435cb40c39a246815b03bffba944bfea4f9ea3"
API_URL  = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {
    "appId": APP_ID,
    "statsDataId":"0003412314",  # 食料需給表
    "cdCat01": "0112",           # チーズ
    "metaGetFlg":"Y",
    "cntGetFlg":"N",
    "explanationGetFlg":"Y",
    "annotationGetFlg":"Y",
    "sectionHeaderFlg":"1",
    "replaceSpChars":"0",
    "lang": "J"
}

response = requests.get(API_URL, params=params)

data = response.json()

# 統計データからデータ部取得
values = data['GET_STATS_DATA']['STATISTICAL_DATA']['DATA_INF']['VALUE']

df = pd.DataFrame(values)

# メタ情報取得
meta_info = data['GET_STATS_DATA']['STATISTICAL_DATA']['CLASS_INF']['CLASS_OBJ']

print(df)