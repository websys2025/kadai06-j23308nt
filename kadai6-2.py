import requests
import pandas as pd

APP_ID = "77435cb40c39a246815b03bffba944bfea4f9ea3"
API_URL = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"
params = {
    "appId": APP_ID,
    "statsDataId": "0003412314",
    "cdCat01": "0112",
    "lang": "J"
}

data = requests.get(API_URL, params=params).json()
df = pd.DataFrame(data['GET_STATS_DATA']['STATISTICAL_DATA']['DATA_INF']['VALUE'])
print(df)