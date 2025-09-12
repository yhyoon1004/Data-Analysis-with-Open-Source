import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols

## 아이리스 데이터셋 로드
df = sns.load_dataset('iris')

## 일원 분산 분석(ANOVA) 모델 생성 및 학습
## 'sepal_length'에 대한 'species'의 영향 분석
model = ols('sepal_length ~ C(species)', data=df).fit()


## ANOVA 테이블 생성 및 출력
anova_table = sm.stats.anova_lm(model, typ=2)
print("ANOVA 결과:")
print(anova_table)

## p-값을 이용한 결과 해석
p_val = anova_table['PR(>F)'][0]
if p_val < 0.05:
    print("\n결과: 귀무가설 기각 (p < 0.05)")
    print("세 품종 간 꽃받침 길이에 통계적으로 유의미한 차이가 존재합니다.")
else:
    print("\n결과: 귀무가설 채택 (p >= 0.05)")
    print("세 품종 간 꽃받침 길이에 유의미한 차이가 없습니다.")