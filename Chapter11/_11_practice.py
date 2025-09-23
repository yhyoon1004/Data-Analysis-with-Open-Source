import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from _11_practice_data_proc import retail_data_clean

plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

## RFM (Recency, Frequency, Monetary) 지표 계산
## 최근성(Recency): 마지막 구매일로부터 경과한 일수
## 빈도(Frequency): 총 구매 횟수
## 총 지출액(Monetary): 총 지출 금액
max_date = retail_data_clean['InvoiceDate'].max() + pd.Timedelta(days=1)

rfm = retail_data_clean.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (max_date - x.max()).days,
    'InvoiceNo': 'nunique',
    'TotalPrice': 'sum'
}).reset_index()

rfm.columns = ['CustomerID', 'Recency', 'Frequency', 'Monetary']

## 3D 그래프 설정
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

## 3D 산점도로 RFM 데이터 시각화
# x: recency, y: frequency, z: monetary
# monetary 값에 따라 색상 변화
scatter = ax.scatter(rfm['Recency'], rfm['Frequency'], rfm['Monetary'], c=rfm['Monetary'], cmap='viridis')

## 각 점에 수직선 추가 (바닥면까지)
for i in range(len(rfm)):
    x = rfm['Recency'].iloc[i]
    y = rfm['Frequency'].iloc[i]
    z = rfm['Monetary'].iloc[i]
    ax.plot([x, x], [y, y], [0, z], color='gray', alpha=0.2)

## 축 레이블 설정
ax.set_xlabel('최근성 (일)', fontsize=12)
ax.set_ylabel('구매 빈도 (회)', fontsize=12)
ax.set_zlabel('총 지출액 (£)', fontsize=12)

## 컬러바 추가
plt.colorbar(scatter, ax=ax, pad=0.1, label='총 지출액 (£)')

## 그래프 제목 설정
plt.title('3D RFM 분석: 고객 세그먼트 시각화', fontsize=15)
plt.show()



# 4제품 가격과 판매량의 관계 (산점도 + 회귀선)


## 제품별 평균 단가 및 총 판매량 계산
product_price_quantity = retail_data_clean.groupby('StockCode').agg({
    'UnitPrice': 'mean',
    'Quantity': 'sum'
}).reset_index()

## 이상치 제거 (가격 100 미만, 판매량 10000 미만)
filtered_products = product_price_quantity[
  (product_price_quantity['UnitPrice'] < 100) &
  (product_price_quantity['Quantity'] < 10000)
]

## 가격과 판매량의 관계 시각화 (회귀선 포함 산점도)
plt.figure(figsize=(12, 8))
# seaborn의 regplot을 이용하여 회귀선 포함 산점도를 출력
sns.regplot(x='UnitPrice', y='Quantity', data=filtered_products)

## 그래프 제목 및 축 레이블 설정
plt.title('제품 가격과 판매량의 관계', fontsize=15)
plt.xlabel('평균 단가 (£)', fontsize=12)
plt.ylabel('총 판매량', fontsize=12)
plt.ylim(-1000, None) ## y축 시작점 설정
plt.grid(linestyle='--') ## 그리드 추가
plt.show()





# 5 월별 및 국가별 매출 추이 (스택 영역 그래프)


## 국가별 총 매출 계산 및 상위 5개국 추출
country_sales = retail_data_clean.groupby('Country')['TotalPrice'].sum().reset_index()
top5_countries = country_sales.sort_values('TotalPrice', ascending=False).head(5)['Country']

## 상위 5개국의 월별 매출 데이터 필터링 및 집계
monthly_country_sales = retail_data_clean[retail_data_clean['Country'].isin(top5_countries)]
monthly_country_sales = monthly_country_sales.groupby(['Year', 'Month', 'Country'])['TotalPrice'].sum().reset_index()
monthly_country_sales['YearMonth'] = monthly_country_sales['Year'].astype(str) + '-' + \
                                      monthly_country_sales['Month'].astype(str).str.zfill(2) ## 연월 문자열 생성

## 피벗 테이블 생성 (월별 국가별 매출)
pivot_data = monthly_country_sales.pivot_table(
    index='YearMonth',
    columns='Country',
    values='TotalPrice',
    fill_value=0 ## 값이 없는 경우 0으로 채움
)

## 스택 영역 그래프 시각화
plt.figure(figsize=(14, 8))
# pivot_data를 이용하여 영역 그래프를 시각화
pivot_data.plot.area(stacked=True)

## 그래프 제목 및 축 레이블 설정
plt.title('월별 및 국가별 매출 추이 (상위 5개국)', fontsize=15)
plt.xlabel('연월', fontsize=12)
plt.ylabel('총 매출(£)', fontsize=12)
plt.legend(title='국가') ## 범례 제목 설정
plt.grid(linestyle='--') ## 그리드 추가
plt.show()





# 6 종합 대시보드 구성

## 월별 총 매출 데이터 준비
monthly_sales = retail_data_clean.groupby(['Year', 'Month'])['TotalPrice'].sum().reset_index()
monthly_sales['YearMonth'] = monthly_sales['Year'].astype(str) + '-' + monthly_sales['Month'].astype(str)

## 국가별 매출 상위 5개국 데이터 준비
country_sales = retail_data_clean.groupby('Country')['TotalPrice'].sum().reset_index()
top_countries = country_sales.sort_values('TotalPrice', ascending=False).head(5)

## 전체 대시보드 figure 설정
fig = plt.figure(figsize=(15, 12))
plt.subplots_adjust(hspace=0.4, wspace=0.4) ## 서브플롯 간 간격 조정

day_names = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']

## 첫 번째 서브플롯: 월별 총 매출 추이 (선 그래프)
ax1 = plt.subplot2grid((2, 2), (0, 0))
ax1.plot(monthly_sales['YearMonth'], monthly_sales['TotalPrice'],
         marker='o', linestyle='-')
ax1.set_title('월별 총 매출 추이', fontsize=12)
ax1.set_xlabel('연월', fontsize=10)
ax1.set_ylabel('총 매출(£)', fontsize=10)
ax1.tick_params(axis='x', rotation=45)
ax1.grid(True, linestyle='--', alpha=0.7)

## 두 번째 서브플롯: 국가별 매출 비중 (파이 차트)
ax2 = plt.subplot2grid((2, 2), (0, 1))
ax2.pie(top_countries['TotalPrice'], labels=top_countries['Country'].head(5), autopct='%1.1f%%')
ax2.set_title('국가별 매출 비중 (상위 5개국)', fontsize=12)
ax2.axis('equal') ## 원형 파이 차트를 위해 비율을 같게 설정

## 세 번째 서브플롯: 요일별 주문 수 (막대 그래프)
ax3 = plt.subplot2grid((2, 2), (1, 0))
day_orders = retail_data_clean.groupby('DayOfWeek').size()
day_orders.index = [day_names[i] for i in day_orders.index]
ax3.bar(day_orders.index, day_orders.values, color='#2ecc71')
ax3.set_title('요일별 주문 수', fontsize=12)
ax3.set_xlabel('요일', fontsize=10)
ax3.set_ylabel('주문 수', fontsize=10)
ax3.tick_params(axis='x', rotation=45)

## 네 번째 서브플롯: 제품 가격 분포 (히스토그램)
ax4 = plt.subplot2grid((2, 2), (1, 1))
ax4.hist(retail_data_clean['UnitPrice'], bins=30, color='#9b59b6', alpha=0.7)
ax4.set_title('제품 가격 분포', fontsize=12)
ax4.set_xlabel('단가(£)', fontsize=10)
ax4.set_ylabel('빈도', fontsize=10)

## 전체 대시보드 제목
plt.suptitle('온라인 쇼핑몰 판매 데이터 대시보드', fontsize=16)
plt.show()
