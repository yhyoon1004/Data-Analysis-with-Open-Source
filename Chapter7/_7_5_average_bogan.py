
import pandas as pd
import numpy as np

file_path = "raw_large_shopping_customer.csv"
df = pd.read_csv(file_path)
print(df.isnull().sum()) # 결측치 개수

# 결측치가 2개 이상인 경우 삭제  / thresh:임계점, df.shape[1]:칼럼의 개수  -1
df_cleaned = df.dropna(thresh=df.shape[1] - 1)
print("----- df_cleaned -----")
print(df_cleaned)

### 나이, 소득 평균값 대치 및 결과 출력

df_cleaned.loc[:,['나이', '소득']] = df_cleaned[['나이', '소득']].fillna(df_cleaned[['나이','소득']].mean())

print('-----  -----')
print(df_cleaned.loc[:,['나이', '소득']])


### 지출, 평균구매횟수 선형보간법 적용
df_cleaned.loc[:,['지출', '평균구매횟수']] = (df_cleaned[['지출', '평균구매횟수']]
                                      .interpolate(method='linear')) #null값인 것들에 값을 채워라.
print('----- df_cleaned.loc[:,[\'지출\', \'평균구매횟수\']] -----')
print(df_cleaned.loc[:,['지출', '평균구매횟수']] )
df_cleaned.to_csv("cleaned_large_shopping_customer.csv", index=False, encoding="utf-8-sig")