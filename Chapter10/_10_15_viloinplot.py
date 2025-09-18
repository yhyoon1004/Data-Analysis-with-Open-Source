import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

plt.rc('font', family='AppleGothic')

np.random.seed(42) ## 난수 시드 설정

## 도시별 가상 기온 데이터 생성
seoul_temp = np.random.normal(22, 3, 100)
busan_temp = np.random.normal(24, 2, 100)
jeju_temp = np.random.normal(26, 2.5, 100)

## DataFrame 생성
data = pd.DataFrame({
    '도시': ['서울'] * 100 + ['부산'] * 100 + ['제주'] * 100,
    '기온(°C)': np.concatenate([seoul_temp, busan_temp, jeju_temp])
})

## seaborn을 이용하여 바이올린 플롯 그리기
sns.violinplot(x='도시', y='기온(°C)', data=data)

## 그래프 제목 및 축 레이블 설정
plt.xticks(rotation=45, fontsize=12, ha='right')
plt.title('2025년 여름 주요 도시 일일 기온 분포', fontsize=14)
plt.xlabel('도시', fontsize=12)
plt.ylabel('기온(°C)', fontsize=12)
plt.ylim(15, 35)

plt.tight_layout()
plt.show()