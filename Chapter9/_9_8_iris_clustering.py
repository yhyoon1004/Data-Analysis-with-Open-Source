from scipy.cluster.vq import kmeans
from sklearn.cluster import KMeans, DBSCAN
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

## 아이리스 데이터셋 로드
iris = load_iris()
X = iris.data
y = iris.target

## K-평균 군집화 수행
kmeans = KMeans(n_clusters=3)
cluster_labels = kmeans.fit_predict(X)


## PCA를 이용한 차원 축소 (2차원)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

## 군집화 결과 및 실제 클래스 시각화
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False  # - 가 아스키표현 안되는문제 처리
plt.figure(figsize=(12, 5))

## K-평균 군집화 결과 시각화
plt.subplot(1, 2, 1)
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=cluster_labels, cmap='viridis')
plt.title('K-평균 군집화 결과 (PCA)')
plt.colorbar(scatter, label='군집')

## 실제 클래스 시각화
plt.subplot(1, 2, 2)
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis')
plt.title('실제 클래스 (PCA)')
plt.colorbar(scatter, label='클래스')
plt.tight_layout()
plt.show()