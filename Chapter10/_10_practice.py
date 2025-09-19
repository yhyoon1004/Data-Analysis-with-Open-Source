import matplotlib.pyplot as plt
import tabulate
import seaborn as sns
import pandas as pd
import openpyxl

plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

## 데이터셋 URL 정의
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx"

## 데이터셋 로드
retail_data = pd.read_excel(url)
# retail_data = pd.read_excel('./OnlineRetail.xlsx', sheet_name='Sheet1', index_col=0, parse_dates=True, engine='openpyxl')

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

## 월별 총 매출 계산
# retail_data_clean을 Year와 Month 단위로 그룹화 한 후 TotalPrice의 합을 구함
monthly_sales = retail_data_clean.groupby(['Year', 'Month'])['TotalPrice'].sum().reset_index()
monthly_sales['YearMonth'] = monthly_sales['Year'].astype(str) + '-' + monthly_sales['Month'].astype(str)

# YearMonth 칼럼에 label을 설정
monthly_sales['YearMonth'] = monthly_sales['Year'].astype(str) + '-' + monthly_sales['Month'].astype(str)

## 월별 총 매출 추이 시각화
plt.figure(figsize=(12, 6))
plt.plot(monthly_sales['YearMonth'], monthly_sales['TotalPrice'])

## 그래프 제목 및 축 레이블 설정
plt.title('월별 총 매출 추이', fontsize=15)
plt.xlabel('연월', fontsize=12)
plt.ylabel('총 매출(£)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

## 국가별 총 매출 계산 및 상위 10개국 추출
# retail_data_clean을 Country 단위로 그룹화 한 후 TotalPrice의 합을 구함
country_sales = retail_data_clean.groupby('Country')['TotalPrice'].sum().reset_index()
# 역순으로 정렬한 다음 상위 10개 선택
total_countries = country_sales.sort_values('TotalPrice', ascending=False).head(10)

## 국가별 총 매출 시각화 (막대 그래프)
plt.figure(figsize=(12, 6))
plt.bar(total_countries['Country'], total_countries['TotalPrice'])

## 그래프 제목 및 축 레이블 설정
plt.title('국가별 총 매출 (상위 10개국)', fontsize=15)
plt.xlabel('국가', fontsize=12)
plt.ylabel('총 매출(£)', fontsize=12)
plt.grid(True, axis='y')  ## Y축 그리드만 표시
plt.show()

## 요일 및 시간대별 주문 횟수 계산
# 일, 시간으로 그룹화 한 후 횟수(size)를 측정
hourly_orders = retail_data_clean.groupby(['DayOfWeek', 'Hour'])['InvoiceNo'].size().unstack(fill_value=0)

## 요일 인덱스 한글명으로 변경
day_names = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
hourly_orders.index = [day_names[i] for i in hourly_orders.index]

## 히트맵 시각화
plt.figure(figsize=(12, 6))
sns.heatmap(hourly_orders, annot=True, cmap='Reds', fmt='d')

## 그래프 제목 및 축 레이블 설정
plt.title('요일 및 시간대별 주문 횟수', fontsize=15)
plt.xlabel('시간', fontsize=12)
plt.ylabel('요일', fontsize=12)
plt.show()
