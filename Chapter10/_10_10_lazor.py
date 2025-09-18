import numpy as np
import matplotlib.pyplot as plt
from networkx.algorithms.bipartite import projection

plt.rc('font', family='AppleGothic')

## 데이터 정의
labels = ['데이터 전처리', '데이터 수집', '머신러닝과 딥러닝', '시각화', '데이터베이스', '수학 및 통계']
values = [10, 7, 7, 9, 7, 6]
n = len(labels)

## 각 축의 각도 계산 및 데이터 반복 추가 (닫힌 그래프를 위해)
angles = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
values += values[:1]
angles += angles[:1]

## 레이더 차트 생성 (극 좌표계의 라인 그래프)
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(angles,values)

## 축 라벨 및 눈금 설정
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=12)
ax.set_yticks([2, 4, 6, 8, 10])
ax.set_yticklabels(['2', '4', '6', '8', '10'], fontsize=10)
ax.set_ylim(0, 10)
ax.grid(True, linestyle='-', alpha=0.7)

## 각 축에 가이드라인 추가
for angle, label in zip(angles[:-1], labels):
    ax.plot([angle, angle], [0, 10], '--', color='gray', alpha=0.3, linewidth=0.5)

plt.title('데이터 분석 역량 프로파일', fontsize=15, pad=20)
plt.tight_layout()
plt.show()