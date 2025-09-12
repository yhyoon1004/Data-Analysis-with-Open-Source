import seaborn as sns
from statsmodels.stats.weightstats import ttest_ind

## 아이리스 데이터셋 로드
df = sns.load_dataset('iris')

## 비교할 두 품종의 꽃받침 길이 데이터 추출
setosa = df[df['species'] == 'setosa']['sepal_length']
versicolor = df[df['species'] == 'versicolor']['sepal_length']

## 독립 표본 t-검정 수행
## 두 그룹(setosa, versicolor)의 'sepal_length' 평균이 통계적으로 유의미한 차이가 있는지 검정
t_stat, p_val, df_dof = ttest_ind(setosa, versicolor)

## t-통계량과 p-값 출력
print(f"t-통계량: {t_stat:.4f}, p-값: {p_val:.4f}")

## 검정 결과 해석
if p_val < 0.05:
    print("귀무가설 기각: 두 품종의 꽃받침 길이에 유의한 차이가 있다")
else:
    print("귀무가설 채택: 두 품종의 꽃받침 길이에 유의한 차이가 없다")