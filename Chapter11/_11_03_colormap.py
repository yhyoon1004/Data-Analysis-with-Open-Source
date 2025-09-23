import matplotlib.pyplot as plt
import numpy as np
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

## 컬러맵 리스트
colormaps = ['viridis', 'plasma', 'inferno', 'magma', 'cividis', 'Blues', 'Greens', 'Reds',
              'Purples', 'Oranges', 'coolwarm', 'RdBu', 'coolwarm', 'Spectral', 'Set1',
              'Set2', 'Set3', 'tab10', 'tab20', 'PiYG', 'twilight', 'hsv', 'terrain', 'ocean',
              'gist_earth', 'hot', 'afmhot']

## 그래프 크기 설정
plt.figure(figsize=(8, len(colormaps) * 0.5))

## 각 컬러맵 시각화
for i, cmap in enumerate(colormaps):
    gradient = np.linspace(0, 1, 256).reshape(1, -1)
    plt.subplot(len(colormaps), 1, i + 1)
    plt.imshow(gradient, aspect='auto', cmap=cmap)
    plt.axis('off')
    plt.title(cmap, fontsize=10, loc='left')

plt.tight_layout()
plt.show()