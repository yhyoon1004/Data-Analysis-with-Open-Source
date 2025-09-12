from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

## 아이리스 데이터셋 로드
iris = load_iris()
X, y = iris.data, iris.target

## 다양한 분류 모델 정의
models = {
    '로지스틱 회귀': LogisticRegression(),
    '결정 트리': DecisionTreeClassifier(),
    '랜덤 포레스트': RandomForestClassifier(),
    '서포트 백터 머신': SVC(),
    'k-최근접 이웃': KNeighborsClassifier(),
}

## 각 모델별 교차 검증 수행 및 결과 출력
for name, model in models.items():
    # cross_val_score를 이용하여 학습 및 성능 평가를 수행
    # cv=크로스벨리데이션 5 => 전체데이터를 5개로 분할 4개를 사용하고 한개를 검즘함
    scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
    print(f"{name}:")
    print(f"  평균 정확도 = {scores.mean():.4f} (±{scores.std():.4f})")
    print(f"  개별 폴드 점수 = {[round(score, 4) for score in scores]}")
    print("-"*50)

    # 로지스틱 회귀:
    #   평균 정확도 = 0.9733 (±0.0249)
    #   개별 폴드 점수 = [np.float64(0.9667), np.float64(1.0), np.float64(0.9333), np.float64(0.9667), np.float64(1.0)]
    # --------------------------------------------------
    # 결정 트리:
    #   평균 정확도 = 0.9600 (±0.0327)
    #   개별 폴드 점수 = [np.float64(0.9667), np.float64(0.9667), np.float64(0.9), np.float64(0.9667), np.float64(1.0)]
    # --------------------------------------------------
    # 랜덤 포레스트:
    #   평균 정확도 = 0.9600 (±0.0249)
    #   개별 폴드 점수 = [np.float64(0.9667), np.float64(0.9667), np.float64(0.9333), np.float64(0.9333), np.float64(1.0)]
    # --------------------------------------------------
    # 서포트 백터 머신:
    #   평균 정확도 = 0.9667 (±0.0211)
    #   개별 폴드 점수 = [np.float64(0.9667), np.float64(0.9667), np.float64(0.9667), np.float64(0.9333), np.float64(1.0)]
    # --------------------------------------------------
    # k-최근접 이웃:
    #   평균 정확도 = 0.9733 (±0.0249)
    #   개별 폴드 점수 = [np.float64(0.9667), np.float64(1.0), np.float64(0.9333), np.float64(0.9667), np.float64(1.0)]
    # --------------------------------------------------