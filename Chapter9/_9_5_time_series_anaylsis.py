import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

## seaborn에서 flights 데이터셋 로드
flights = sns.load_dataset('flights')

## 날짜 형식 변환 및 인덱스 설정
## 'year'와 'month' 컬럼을 이용하여 'date' 컬럼 생성 후 인덱스로 설정
flights['date'] = pd.to_datetime(
    flights['year'].astype(str) + '-' +
    flights['month'].astype(str) + '-01'
)
flights = flights.set_index('date').sort_index()

## 시계열 시각화
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False # - 가 아스키표현 안되는문제 처리
plt.figure(figsize=(10, 6))
plt.plot(flights['passengers'])
plt.title('월별 항공 승객 수 (1949-1960)')
plt.xlabel('연도')
plt.ylabel('승객 수')
plt.grid(True)
plt.show()

## 시계열 분해 (추세, 계절성, 잔차)
## 시계열 데이터를 추세(Trend), 계절성(Seasonal), 잔차(Residual)로 분해
decomposition = seasonal_decompose(flights['passengers'], model='multiplicative', period=12)

fig = decomposition.plot()
fig.set_size_inches(12, 8)
plt.tight_layout()
plt.show()