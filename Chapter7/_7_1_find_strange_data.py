import pandas as pd
import numpy as np

data = {'이름': ['김철수', '이영희', '박민수', '최지훈', '정소희'],
        '나이': [25, 30, np.nan, 22, 35],
        '도시': ['서울', None, '인천', '서울', '대전'],
        '점수': [90, 85, np.nan, 80, 92]}

df = pd.DataFrame(data)
print("----- df -----")
print(df)

## 결측치 여부 확인
value_isnull = df.isnull()
value_isna = df.isna()
print("----- value_isnull -----")
print(value_isnull)
print("----- value_isna -----")
print(value_isna)

## 열별, 행별 결측치 개수 확인
value_isnull_sum_col = df.isnull().sum()
print("----- value_isnull_sum_col -----")
print(value_isnull_sum_col)

value_isnull_sum_row = df.isnull().sum(axis=1)
print("----- value_isnull_sum_row -----")
print(value_isnull_sum_row)

## 특정 열, 행 결측치 확인
value_err_row = df[df.isnull().any(axis=1)]
print("----- value_err_row -----")
print(value_err_row)

value_err_col = df[df['나이'].isnull()]
print("----- value_err_col -----")
print(value_err_col)

## 결측치가 아닌 항목 확인
value_notnull = df.notnull()
print("----- value_notnull -----")
print(value_notnull)

## 결측치 비율
ratio_err = df.isnull().sum().sum() / (df.shape[0] * df.shape[1]) * 100
print("----- ratio_err -----")
print(ratio_err)