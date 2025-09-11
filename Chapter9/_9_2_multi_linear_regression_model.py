import statsmodels.formula.api as smf
import seaborn as sns
import matplotlib.pyplot as plt

## 아이리스 데이터셋 로드
df = sns.load_dataset('iris')

## 다중 선형 회귀 모델 생성 및 학습
## 'petal_width'를 종속 변수로 하고 다른 특성들(sepal_length, sepal_width, petal_length)을 독립 변수로 사용
model = smf.ols(
    formula='petal_width ~ sepal_length + sepal_width + petal_length',
    data=df
).fit()
## 모델 요약 결과 출력
print(model.summary())

## 실제 값 vs 예측 값 시각화
plt.figure(figsize=(8, 6))
predictions = model.predict(df) ## 모델 예측값 계산
plt.scatter(df['petal_width'], predictions, alpha=0.7) ## 실제 값과 예측 값 산점도
plt.plot([df['petal_width'].min(), df['petal_width'].max()],
         [df['petal_width'].min(), df['petal_width'].max()], 'k--', lw=2) ## 이상적인 예측 라인 (y=x)
plt.xlabel('Actual Values', fontsize=12)
plt.ylabel('Predicted Values', fontsize=12)
plt.title('Actual vs Predicted Values', fontsize=14)
plt.grid(True, alpha=0.3)
plt.show()