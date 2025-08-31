import pandas as pd
import requests


url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMinuDustFrcstDspth"
api_key = ''

params = {
    'serviceKey': api_key,
    'returnType': 'json',
    'numOfRows': '100',
    'pageNo': '1',
    'sidoName': '서울',
    'ver': '1.0'
}

## 데이터 수집
response = requests.get(url, params=params)

## requests로부터 response, body, item 항목 읽기
data = response.json()['response']['body']['items']
print(type(data))
# <class 'list'>

print(len(data))
print(data[0])
# 100
# {'informCode': 'PM25', 'dataTime': '2025-08-31'}

df = pd.DataFrame(data)
html = df.to_html()
print(html)

with open("openAPI_data.html", "w") as f:
    f.write(html)

print(df['informCode'])
