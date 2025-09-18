import seaborn as sns

## 요일 및 시간대별 주문 횟수 계산
# 일, 시간으로 그룹화 한 후 횟수(size)를 측정


## 요일 인덱스 한글명으로 변경
day_names = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
hourly_orders.index = [day_names[i] for i in hourly_orders.index]

## 히트맵 시각화


## 그래프 제목 및 축 레이블 설정
plt.title('요일 및 시간대별 주문 횟수', fontsize=15)
plt.xlabel('시간', fontsize=12)
plt.ylabel('요일', fontsize=12)
plt.show()