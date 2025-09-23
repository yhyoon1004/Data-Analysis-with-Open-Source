import matplotlib.pyplot as plt
import numpy as np # numpy 임포트 추가
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

## 서브플롯 생성 (2행 2열)
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

## 첫 번째 서브플롯: 선 그래프
axes[0, 0].plot([1, 2, 3, 4], [10, 20, 25, 30])
axes[0, 0].set_title("선 그래프")

## 두 번째 서브플롯: 막대 그래프
axes[0, 1].bar(['A', 'B', 'C', 'D'], [5, 7, 3, 8], color='orange')
axes[0, 1].set_title("막대 그래프")

## 세 번째 서브플롯: 산점도
axes[1, 0].scatter([1, 2, 3, 4], [15, 25, 10, 30], color='red')
axes[1, 0].set_title("산점도 그래프")

## 네 번째 서브플롯: 히스토그램
data = np.random.randn(100)
axes[1, 1].hist(data, bins=10, color='purple')
axes[1, 1].set_title("히스토그램")

## 레이아웃 조정 및 그래프 표시
plt.tight_layout()
plt.show()