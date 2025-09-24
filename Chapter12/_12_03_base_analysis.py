from _12_02_csv_data_collect import df

## 수치형 데이터 요약 통계 출력
print("수치형 데이터 요약 통계:\n" , df.describe().to_markdown())

## 범주형 데이터 요약 통계 출력
print("범주형 데이터 요약 통계:\n", df.describe(include=['object']))