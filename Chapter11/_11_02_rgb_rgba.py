import matplotlib.pyplot as plt
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

## 그래프 및 축 객체 생성
fig, ax = plt.subplots(figsize=(6, 4))

## RGB 및 RGBA 색상 정의 (마지막 값은 투명도)
labels = ['Red', 'Green', 'Blue', 'Yellow', 'Cyan (Transparent)']
colors = [(1,0,0),(0,1,0),(0,0,1),(1,1,0),(0,1,1,0.5)]

## 막대 그래프 그리기 (정의된 색상 사용)
ax.bar(labels, [5, 7, 6, 4, 8], color=colors)
ax.set_title("RGB 및 RGBA 색상 예제", fontsize=14)
ax.set_xlabel("색상", fontsize=12)
ax.set_ylabel("값", fontsize=12)

plt.show()