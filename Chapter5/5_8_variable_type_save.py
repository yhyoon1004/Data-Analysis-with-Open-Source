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

data = response.json()['response']['body']['items']
df = pd.DataFrame(data)

df.to_csv('air_pollution.csv', index=False, encoding='utf-8')

## JSON 형식 데이터 저장
df.to_json("data.json",indent=4, force_ascii=False)

## EXCEL 형식 데이터 저장

print(df)
df.to_excel("data.xlsx",index=False)

## HTML 형식 데이터 저장
df.to_html("data.html")