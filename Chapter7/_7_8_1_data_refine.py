### 시각화 라이브러리 임포트
import matplotlib.pyplot as plt
import seaborn as sns # matplotlib의 기능 확장한 라이브러리
import missingno as msno # 결측치 시각화 특화 라이브러리

from _6_5_kaggle_data_modify import train

plt.rc('font', family='AppleGothic')

plt.figure(figsize=(10, 6))
sns.histplot(train['sales'], bins=50)
plt.title("판매량 분포")
plt.xlabel("판매량")
plt.ylabel("빈도")
plt.xlim(0, 5000)
plt.show()

store_sales = train.groupby('store_nbr')['sales'].mean().reset_index()
plt.figure(figsize=(12, 6))
sns.barplot(x='store_nbr', y='sales', data=store_sales)
plt.title("매장별 평균 판매량")
plt.xlabel("매장 번호")
plt.ylabel("평균 판매량")
plt.xticks(rotation=90)
plt.show()


