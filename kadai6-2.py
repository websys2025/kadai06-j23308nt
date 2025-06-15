# e-Statからチーズの需給表を取得し、表示するプログラム
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

# カテゴリIDを日本語名称に変換
for class_obj in meta_info:
    column_name = '@' + class_obj['@id']
    id_to_name_dict = {}
    if isinstance(class_obj['CLASS'], list):
        for obj in class_obj['CLASS']:
            id_to_name_dict[obj['@code']] = obj['@name']
    else:
        id_to_name_dict[class_obj['CLASS']['@code']] = class_obj['CLASS']['@name']
    df[column_name] = df[column_name].replace(id_to_name_dict)

# 列名を日本語に変換
col_replace_dict = {'@unit': '単位', '$': '値'}
for class_obj in meta_info:
    org_col = '@' + class_obj['@id']
    new_col = class_obj['@name']
    col_replace_dict[org_col] = new_col

new_columns = []
for col in df.columns:
    if col in col_replace_dict:
        new_columns.append(col_replace_dict[col])
    else:
        new_columns.append(col)
df.columns = new_columns

# 全行表示
pd.set_option('display.max_rows', None)
print(df)