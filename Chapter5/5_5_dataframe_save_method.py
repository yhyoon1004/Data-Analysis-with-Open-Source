import pandas as pd

data = {
    "이름": ["김철수", "이영희", "박민수", "최지훈", "정소희"],
    "학년": [1, 2, 3, 4, 2],
    "학점": [4.2, 3.8, 4.5, 3.9, 3.5],
    "학과": ["컴퓨터공학", "경영학", "전자공학", "의학", "심리학"],
    "동아리": ["프로그래밍", "독서토론", "로봇공학", "봉사활동", "음악감상"]
}

## Dataframe 생성
df = pd.DataFrame(data)

## CSV, JSON 형식으로 저장
df.to_csv("student_score.csv")
df.to_json("student_score.json")

## HTML 형식으로 저장
html = df.to_html("student_score.html")

print(html)