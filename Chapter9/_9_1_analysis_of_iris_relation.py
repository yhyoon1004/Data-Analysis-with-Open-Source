import matplotlib.pyplot as plt
import seaborn as sns

plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False # - 가 아스키표현 안되는문제 처리

## 아이리스 데이터셋 로드
df = sns.load_dataset('iris')

## 상관계수 행렬 계산 및 출력
correlation = df.iloc[:, :-1].corr()
print("상관계수 행렬:")
print(correlation)

## 상관관계 히트맵 시각화
plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('특성 간 상관관계')
plt.show()