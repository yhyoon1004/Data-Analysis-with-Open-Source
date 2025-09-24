import glob
import pandas as pd

print("12-02----------------------------------------")

## CSV 파일 목록 가져오기
all_files = glob.glob("./tpss_bcycl_od_statnhm_202303/tpss_bcycl_od_statnhm_*.csv")
dataframes = []
for filename in all_files:
    ## CSV 파일 읽어서 데이터프레임화
    df = pd.read_csv(filename, encoding='cp949')
    dataframes.append(df)
## 모든 데이터프레임 결합
df = pd.concat(dataframes, axis=0, ignore_index=True)

## 상위 5행 출력
df.head(5)
print(df.head(5))
