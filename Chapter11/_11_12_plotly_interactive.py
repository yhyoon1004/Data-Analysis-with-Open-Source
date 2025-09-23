import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False


## 데이터프레임 생성
df = pd.DataFrame({
    'X값': [1, 2, 3, 4, 5],
    'Y값': [10, 14, 18, 24, 30]
})

## 인터랙티브 산점도 생성 및 표시
fig = px.scatter(df,x='X값',y='Y값')
fig.show()