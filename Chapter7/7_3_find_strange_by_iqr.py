import pandas as pd
import numpy as np

점수_데이터 = [72, 68, 75, 282, 64, 31, 78, 69, 88, 92, 22, 84, 61, -90, 130, 66]
학번_데이터 = list(range(1001, 1001 + len(점수_데이터)))

df = pd.DataFrame({
    '학번': 학번_데이터,
    '점수': 점수_데이터
})

### 사분위 범위 경계값 계산
quantile_1 = df['점수'].quantile(0.25)
quantile_3 = df['점수'].quantile(0.75)
print('---- quantile_1 -----')
print(quantile_1)
print('---- quantile_3 -----')
print(quantile_3)

iqr = quantile_3 - quantile_1
print('---- iqr -----')
print(iqr)

low_value = quantile_1 - 1.5 * iqr
high_value = quantile_3 + 1.5 * iqr
print('---- low_value -----')
print(low_value)
print('---- high_value -----')
print(high_value)

### IQR 통계량 출력

