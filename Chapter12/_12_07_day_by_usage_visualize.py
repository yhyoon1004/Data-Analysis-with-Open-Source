import matplotlib.pyplot as plt
from _12_06_day_usage_analysis import *

plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

print("12-07----------------------------------------")

## 요일별 이용량 막대 그래프 생성
plt.bar(day_df.index, day_df.values)


plt.title('요일별 이용량')
plt.xlabel('요일')
plt.ylabel('이용량')
## Dataframe의 plot을 이용한 요일별 이용량 막대 그래프 생성
day_df.plot(kind='bar')
plt.show()