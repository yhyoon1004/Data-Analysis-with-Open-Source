import matplotlib.pyplot as plt
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False # - 가 아스키표현 안되는문제 처리

## 데이터 정의
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

## 막대 그래프 그리기
# plt.bar(categories, values, width=0.5, color='green')

# 가로 막대 그래프
plt.barh(categories, values)

plt.show()