import pandas as pd
import numpy as np

점수_데이터 = [72, 68, 75, 282, 64, 31, 78, 69, 88, 92, 22, 84, 61, -90, 130, 66]
학번_데이터 = list(range(1001, 1001 + len(점수_데이터)))

df = pd.DataFrame({
    '학번': 학번_데이터,
    '점수': 점수_데이터
})

### Z-점수 계산
avg_score = df['점수'].mean()
std_score = df['점수'].std()

df['점수_Z'] = (df['점수'] - avg_score) / std_score
score_z = df['점수_Z']
print("----- score_z -----")
print(score_z)

### 임계값 설정 및 이상치 여부 판단
threshold = 2
df['이상치여부'] = df['점수_Z'].abs() > threshold
value_strange = df['이상치여부']
print('----- value_strange -----')
print(value_strange)

### 이상치 데이터 출력
value_is_strange = df[df['이상치여부']]
print('----- value_is_strange -----')
print(value_is_strange)

### 이상치 비율 출력
percent_of_strange = df['이상치여부'].mean() * 100
print('----- percent_of_strange -----')
print(percent_of_strange)
