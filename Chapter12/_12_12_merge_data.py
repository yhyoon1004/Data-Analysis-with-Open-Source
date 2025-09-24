from _12_11_waterfall_data_proc import *
from _12_09_usage_by_day import daily_usage_df

## 일자별 이용량과 강수량 데이터 병합 (daily_usage_gf의 기준_날짜, rain_df의 일시를 기준으로 결합)
merged_df = pd.merge(daily_usage_df, rain_df, how='left',left_on='기준_날짜',right_on='일시')
## 'count' 컬럼명 '이용량'으로 변경
merged_df.rename(columns={'count': '이용량'}, inplace=True)

## 병합된 데이터프레임 상위 5행 출력
print("---------------------------------")
print(merged_df.head(5))