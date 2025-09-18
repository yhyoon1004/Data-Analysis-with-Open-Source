import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

## 데이터 생성 (5x5 크기의 무작위 행렬)
data = np.random.rand(5, 5)

## seaborn을 이용하여 히트맵 그리기
sns.heatmap(data, annot=True, fmt='.2f')

plt.title("Heatmap")
plt.show()