import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False # - 가 아스키표현 안되는문제 처리

## 데이터 생성 (정규 분포를 따르는 1000개의 난수)
data = np.random.randn(1000)

## 히스토그램 그리기
plt.hist(data, bins=100) #bins=픽셀 수

plt.show()