import pandas as pd

data = {
    "이름": ["김철수", "이영희", "박민수", "최지훈", "정소희"],
    "학년": [1, 2, 3, 4, 2],
    "학점": [4.2, 3.8, 4.5, 3.9, 3.5],
    "학과": ["컴퓨터공학", "경영학", "전자공학", "의학", "심리학"],
    "동아리": ["프로그래밍", "독서토론", "로봇공학", "봉사활동", "음악감상"]
}

df = pd.DataFrame(data)
print(df)
print('-----')

#DataFrame 인덱스 지정
df = df.set_index('이름') #인덱스를 이름 변경
print(df)
print('-----')

#DataFrame 행 선택
loc_kim = df.loc['김철수']
print(loc_kim)
print('-----')

loc_multi = df.loc[['김철수', '박민수']]
print(loc_multi)
print('-----')

loc_index_slicing = df.loc['김철수':'최지훈']
print(loc_index_slicing)
print('-----')

#DataFrame 위치 기반 행 선택
iloc_select = df.iloc[1]    #iloc => index location
iloc_multi = df.iloc[[0, 2]]
iloc_slicing = df.iloc[1:3]
print(iloc_select)
print('-----')
print(iloc_multi)
print('-----')
print(iloc_slicing)
print('-----')

#DataFrame 조건 기반 선택
booleanIndex = df.loc[[True, False, True, False, False]]
print(booleanIndex)
print('-----')

df_score_cond = df['학점'] >= 4.0
print(df_score_cond)
print('-----')

loc_condition_score = df.loc[df['학점'] >= 4.0]
print(loc_condition_score)
print('-----')

df_grade_cond = df[df['학년'] == 2]
print(df_grade_cond)
print('-----')

df_multi_cond = df[(df['학년'] == 2) & (df['학점'] >= 3.7)]
print(df_multi_cond)
print('-----')


