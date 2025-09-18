import matplotlib.pyplot as plt
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] =False

## 데이터 정의
labels =['A','B','C','D']
sizes =[20,30,25,25]

## 파이 차트 그리기
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

plt.title("파이 차트")
plt.show()