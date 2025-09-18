import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
plt.rc('font', family='AppleGothic')

## 데이터 생성
np.random.seed(0)
x = np.random.rand(20)
y = np.random.rand(20)
z = np.random.rand(20)

## 3D 그래프 설정
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

## 3D 산점도 그리기
ax.scatter(x, y, z)
ax.set_xlabel("X 축")
ax.set_ylabel("Y 축")
ax.set_zlabel("Z 축")
ax.set_title("3D 산점도")

plt.show()