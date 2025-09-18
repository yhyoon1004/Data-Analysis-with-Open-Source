import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

plt.rc('font', family='AppleGothic')

## 데이터 정의
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 3, 4, 5])
z = np.zeros(5) ## 막대 바닥의 Z 좌표
heights = np.array([5, 7, 3, 8, 6]) ## 각 막대의 높이

## 3D 그래프 설정
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

## 3D 막대 그래프 그리기
## x, y, z: 각 막대의 시작 위치 (바닥)
## 0.5, 0.5: 각 막대의 너비와 깊이
## heights: 각 막대의 높이
ax.bar3d(x, y, z, 0.5, 0.5, heights)

## 축 레이블 및 제목 설정
ax.set_xlabel("X 축")
ax.set_ylabel("Y 축")
ax.set_zlabel("높이")
ax.set_title("3D 막대 그래프")

plt.show()