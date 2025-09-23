import matplotlib.pyplot as plt
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

## 데이터 정의
months = ['1월', '2월', '3월', '4월', '5월', '6월']
sales = [120, 150, 140, 170, 190, 210]

## 그래프 그리기
plt.figure(figsize=(8, 5))
plt.plot(months, sales, 'o-', color='blue')

## 축, 레이블, 제목 설정
# x 축 제목 : 월
plt.xlabel("월")

# y 축 제목 : 매출(만원)
plt.ylabel("매출(만원)")

# y 축 범위 (100 ~ 220)
plt.ylim(100, 220)

# 제목 : 2025년 상반기 월별 매출
plt.title('2025년 상반기 월별 매출')

plt.grid(True)
plt.show()