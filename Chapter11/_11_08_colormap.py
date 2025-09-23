import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

## 데이터 생성
x = np.random.rand(100)
y = np.random.rand(100)
temperature = np.random.rand(100) * 30

## 산점도 그리기
# cmap 설정
plt.scatter(x, y, c=temperature)
# 컬러 바 추가
plt.colorbar()

plt.title("위치별 온도 분포")
plt.xlabel("x 좌표")
plt.ylabel("y 좌표")
plt.show()