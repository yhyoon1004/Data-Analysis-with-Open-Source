import pandas as pd

data = {
    "이름": ["김철수", "이영희", "박민수", "최지훈", "정소희"],
    "학년": [1, 2, 3, 4, 2],
    "학점": [4.2, 3.8, 4.5, 3.9, 3.5],
    "학과": ["컴퓨터공학", "경영학", "전자공학", "의학", "심리학"],
    "동아리": ["프로그래밍", "독서토론", "로봇공학", "봉사활동", "음악감상"]
}
df = pd.DataFrame(data)

# 특정 열 선택
df_single_name = df['이름']
print(df_single_name)
print('-----')

df_multi = df[['이름', '학과', '학점']]
print(df_multi)
print('-----')

# DataFrame 열순서 변경
reordered_cols = df[['학과', '이름', '학년', '학점', '동아리']]
print(reordered_cols)
print('-----')

# DataFrame 열이름 변경
renamed_df = df.rename(columns={'이름': '학생명', '학점': '평점', '동아리': '과외활동'})
print(renamed_df)
print('-----')
