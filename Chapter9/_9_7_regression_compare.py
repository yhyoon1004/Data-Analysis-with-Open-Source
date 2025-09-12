from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_squared_error, r2_score

## 캘리포니아 주택 데이터셋 로드
california = fetch_california_housing()
X = california.data
y = california.target

## 다양한 회귀 모델 정의
models = {
    '선형 회귀': LinearRegression(),
    '릿지 회귀': Ridge(),
    '라쏘 회귀': Lasso(),
    '결정 트리 회귀': DecisionTreeRegressor(),
    '랜덤 포레스트 회귀': RandomForestRegressor(),
}

## 각 모델별 교차 검증 수행 및 RMSE 출력
for name, model in models.items():
    ## 5-폴드 교차 검증으로 MSE(평균 제곱 오차) 계산
    scores = cross_val_score(model, X, y, cv=5, scoring='neg_mean_squared_error')
    rmse = (-scores.mean()) ** 0.5 ## MSE를 RMSE로 변환
    print(f"{name}: RMSE = {rmse:.4f}")