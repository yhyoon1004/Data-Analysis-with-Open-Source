import pandas as pd
from pandas import DataFrame

## 데이터 딕셔너리 정의
data = {
    '이름': ['김지은', '이민호', '박서연', '최준영', '정다혜'],
    '나이': [27, 32, 29, 35, 24],
    '성적': [92, 85, 95, 78, 88],
    '부서': ['개발팀', '인사팀', '개발팀', '재무팀', '마케팅팀'] }

## 딕셔너리를 이용하여 DataFrame 생성
df = DataFrame(data)

## DataFrame 출력
print(df)