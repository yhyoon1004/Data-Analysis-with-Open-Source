import matplotlib.pyplot as plt
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

## 데이터 정의
x = [1, 2, 3, 4, 5]
y1 = [10, 2, 14, 16, 4]
y2 = [8, 10, 12, 11, 13]
y3 = [6, 9, 11, 10, 12]

## 여러 선 그래프 그리기
# y1, 마커 : o, 라인 스타일: -, 색: blue
plt.plot(x, y1, marker='o', linestyle='-', color='blue')

# y2, 마커 : s, 라인 스타일: --, 색: red
plt.plot(x, y2, marker='s', linestyle='--', color='red')

# y3, 마커 : ^, 라인 스타일: -., 색: green
plt.plot(x, y3, marker='^', linestyle='-.', color='green')


## 제목 및 축 레이블 설정
plt.title("여러 선 그래프 - 마커와 선 스타일 비교")
plt.xlabel("X축 값")
plt.ylabel("Y축 값")

plt.show()