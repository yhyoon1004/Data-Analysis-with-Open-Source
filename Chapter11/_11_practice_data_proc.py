import pandas as pd

## 데이터셋 URL 정의
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx"

## 데이터셋 로드
retail_data = pd.read_excel(url)

## 데이터셋 크기 출력
print("데이터셋 크기:", retail_data.shape)

## 첫 5개 행 출력
print("\n첫 5개 행:")
print(retail_data.head())

## 데이터 정보 출력
print("\n데이터 정보:")
print(retail_data.info())

## 기술 통계 요약 출력
print(retail_data.describe().to_markdown())

## CustomerID가 없는 행 제거
retail_data_clean = retail_data.dropna(subset=['CustomerID'])
## 중복된 행 제거
retail_data_clean = retail_data_clean.drop_duplicates()
## 수량(Quantity)과 단가(UnitPrice)가 0보다 큰 유효한 데이터만 필터링
retail_data_clean = retail_data_clean[(retail_data_clean['Quantity'] > 0) &
                                      (retail_data_clean['UnitPrice'] > 0)]

## 총 가격(TotalPrice) 컬럼 생성
retail_data_clean['TotalPrice'] = retail_data_clean['Quantity'] * retail_data_clean['UnitPrice']

## InvoiceDate에서 시간 관련 특성 추출
retail_data_clean['Year'] = retail_data_clean['InvoiceDate'].dt.year
retail_data_clean['Month'] = retail_data_clean['InvoiceDate'].dt.month
retail_data_clean['Day'] = retail_data_clean['InvoiceDate'].dt.day
retail_data_clean['DayOfWeek'] = retail_data_clean['InvoiceDate'].dt.dayofweek
retail_data_clean['Hour'] = retail_data_clean['InvoiceDate'].dt.hour

## 전처리 후 데이터 크기 및 첫 5개 행 출력
print("\n전처리 후 데이터 크기:", retail_data_clean.shape)
print("\n전처리 후 첫 5개 행:")
print(retail_data_clean.head())