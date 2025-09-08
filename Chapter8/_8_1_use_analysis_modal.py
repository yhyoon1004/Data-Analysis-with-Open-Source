import pandas as pd
import random
# statsmodels의 formula api 임포트
import statsmodels.formula.api as smf



## 난수 시드 설정
random.seed(1)

## 데이터 생성
X = list(range(1, 11))
y = [2*x + 1 + random.gauss(0, 1) for x in X]

## 데이터프레임 생성
data = pd.DataFrame({'X': X, 'y': y})

## OLS(최소 제곱법) 회귀 모델 생성 및 학습
## 'y'를 종속 변수로 하고 다른 특성(X)을 독립 변수로 사용
model = smf.ols(formula='y ~ X', data=data).fit()

## 모델 요약 결과 출력
print(model.summary())