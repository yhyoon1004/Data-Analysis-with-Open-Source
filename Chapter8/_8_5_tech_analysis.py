import pandas as pd
import seaborn as sns

## 아이리스 데이터셋 로드
df = sns.load_dataset('iris')

# 기술 통계량
print("=== 기본 통계량 ===")
print(df.describe())

# 데이터 미리보기
print("\n=== 데이터 미리보기 ===")
print(df.head())

# 그룹별 통계정보
print("\n=== 품종별 평균값 ===")
print(df.groupby('species').mean())
