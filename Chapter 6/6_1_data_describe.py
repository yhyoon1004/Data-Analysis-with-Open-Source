import pandas as pd
import numpy as np

data = {
    'name': ['김민수', '이지영', '박준호', '최서연', '정도윤'],
    'age': [25, 30, 28, 22, 35],
    'city': ['서울', '부산', '인천', '서울', '대전'],
    'score': [90, 85, 95, 80, np.nan]
}

# np.nan => 결측치를 위해 사용

df = pd.DataFrame(data)

# 데이터 측정
default_describe = df.describe()
print(default_describe)
print("-----")

# 모든 데이터 타입 측정
describe_all = df.describe(include='all')
print(describe_all)
print("-----")

# 수치형 데이터 측정
describe_num = df.describe(include=[np.number])
print(describe_num)
print("-----")

# 범주형 데이터 측정
describe_object = df.describe(include=['object'])
print(describe_object)
print("-----")

# 특정 열 분석
describe_column = df['score'].describe()
print(describe_column)

