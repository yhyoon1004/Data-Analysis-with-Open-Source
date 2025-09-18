import matplotlib.pyplot as plt
import numpy as np

plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False # - 가 아스키표현 안되는문제 처리

## 데이터 생성
x = np.arange(0, 6, 1)
y1 = [10, 7, 8, 15, 20, 12]
y2 = [1, 2, 1, 1.5, 2, 1.2]

## 2개의 서브플롯 생성 (2행 1열)
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(6, 6))

## 첫 번째 서브플롯: 라인 플롯
axes[0].plot(x, y1, linestyle='-', marker='o', color='b', label="Line")
axes[0].set_title("Plot")
axes[0].set_ylabel("y value")
axes[0].grid(True)
axes[0].legend()

## 두 번째 서브플롯: 산점도
axes[1].scatter(x, y2, color='purple', label="Scatter", marker='o')
axes[1].set_xlabel("x value")
axes[1].set_ylabel("y value")
axes[1].grid(True)
axes[1].legend()

## x축 및 y축 눈금 설정
axes[1].set_xticks(np.arange(0, 6, 1))
axes[1].set_xticklabels(["0", "1", "2", "3", "4", "5"])
axes[1].set_yticks([0, 0.5, 1, 1.5, 2])

## 전체 그래프 제목 설정 및 표시
fig.suptitle("Matplotlib 그래프 구조")
plt.show()