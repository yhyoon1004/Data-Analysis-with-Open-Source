import pandas as pd

data = {'age': [25, 30, None, 22, 35],
        'city': ['Seoul', None, 'Incheon', 'Seoul', 'Daejeon'],
        'score': [90, 85, None, 80, 92]}
df = pd.DataFrame(data)

### replace를 이용한 Seoul -> 서울
df['city'] = df['city'].replace('Seoul', '서울')
print("----- df[\'city\'] -----")
print(df['city'])

### replace를 이용한 None -> 미정, Incheon -> 인천
df['city'] = df['city'].replace({None: '미정', 'Incheon': '인천'})

### map을 이용한 값 변경
city_map = {'Seoul': '서울특별시', None: '미정', 'Incheon': '인천광역시', 'Daejeon': '대전광역시'}
df['city'] = df['city'].map(city_map)
df['age_str'] = df['age'].map(lambda x: f"{x}살" if pd.notna(x) else "알수없음")
print("----- df['age_str'] -----")
print(df['age_str'])

### apply 함수를 이용한 값 변경
df['age_apply'] = df['age'].apply(lambda x: x * 2 if pd.notna(x) else None)
print("----- df['age_apply'] -----")
print(df['age_apply'])


### apply 함수를 이용한 행단위 값 변경
def age_plus_score(row):
    age = row['age'] if pd.notna(row['age']) else 0
    score = row['score'] if pd.notna(row['score']) else 0
    return age + score


df['age_plus_score'] = df.apply(age_plus_score, axis=1)
print("----- df['age_plus_score'] -----")
print(df['age_plus_score'])

### loc 인덱스를 이용한 값 변경
df.loc[df['score'] < 90, 'score'] = 90
print("----- -----")
print("\n점수가 90점 미만인 사람 90점으로 변경:\n", df)
### where 함수를 이용한 값 변경
df['age_where'] = df['age'].where(df['age'] >= 30, 30)
print('\nage가 30이상인 값만 유지하고 나머지를 0으로 변경 \n', df['age_where'])
print(df)
