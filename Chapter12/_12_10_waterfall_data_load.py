import matplotlib.pyplot as plt
import pandas as pd
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False



## 강수량 데이터 CSV 파일 로드
file_path = 'seoul_rain_2023_04.csv'
rain_df = pd.read_csv(file_path, skiprows=12)
print(rain_df.head(5))