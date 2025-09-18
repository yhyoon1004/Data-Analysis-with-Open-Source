import matplotlib.pyplot as plt
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False # - 가 아스키표현 안되는문제 처리

## 데이터 정의
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 12, 18]

## 선 그래프 그리기
plt.plot(x,y, marker='o')

# 제목 설정
plt.title("선 그래프")

plt.show()