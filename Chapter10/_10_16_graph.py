import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False # - 가 아스키표현 안되는문제 처리

## 데이터 생성
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

Z = np.sin(np.sqrt(X**2 + Y**2))

# 등고선 그래프 그리기
contour = plt.contourf(X, Y, Z, level=20)
plt.contour(X, Y, Z, level=20, colors='black')

# 색상 막대 추가 및 레이블 설정
cbar = plt.colorbar(contour)
cbar.set_label('높이 (Z값)')

## 제목 및 축 레이블 설정
plt.title("등고선 그래프 예제")
plt.xlabel("X 축")
plt.ylabel("Y 축")

plt.show()