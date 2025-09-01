import pandas as pd

data = {
    "이름": ["김철수", "이영희", "박민수", "최지훈", "정소희"],
    "학년": [1, 2, 3, 4, 2],
    "학점": [4.2, 3.8, 4.5, 3.9, 3.5],
    "학과": ["컴퓨터공학", "경영학", "전자공학", "의학", "심리학"],
    "동아리": ["프로그래밍", "독서토론", "로봇공학", "봉사활동", "음악감상"]
}
df = pd.DataFrame(data)

#DataFrame 인덱스 지정
df = df.set_index('이름')

#DataFrame 단일 열 오름차순, 내림차순 정렬
df_sort_default = df.sort_values(by='학점')
df_sort_descending = df.sort_values(by='학점', ascending=False)
print(df_sort_default)
print('-----')
print(df_sort_descending)
print('-----')

#DataFrame 복수 열 오름차순, 내림차순 정렬
df_sort_multi = df.sort_values(by=['학년', '학점'], ascending=[True, False])
print(df_sort_multi)
print('-----')

#DataFrame 인덱스 기분 오른차순, 내림차순 정렬
