import pandas as pd
import json

data = {
    "이름": ["김철수", "이영희", "박민수", "최지훈", "정소희"],
    "학년": [1, 2, 3, 4, 2],
    "학점": [4.2, 3.8, 4.5, 3.9, 3.5],
    "학과": ["컴퓨터공학", "경영학", "전자공학", "의학", "심리학"],
    "동아리": ["프로그래밍", "독서토론", "로봇공학", "봉사활동", "음악감상"]
}

## 딕셔너리, csv, json으로 부터 DataFrame 생성
# pd.DataFrame(data)
df1 = pd.DataFrame.from_dict(data)
df2 = pd.read_csv("student_inform.csv")
df3 = pd.read_json("output.json")

## 세가지 방법 결과 비교
print(df1.shape)
print(df2.shape)
print(df3.shape)
# (5, 5)
# (5, 5)
# (3, 4)