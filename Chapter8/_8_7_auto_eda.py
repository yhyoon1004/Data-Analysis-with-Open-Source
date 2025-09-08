import seaborn as sns
from ydata_profiling import ProfileReport

## 아이리스 데이터셋 로드
df = sns.load_dataset('iris')

## 데이터 프로파일링 보고서 생성
profile = ProfileReport(df, title='보고서!')

## HTML 파일로 보고서 저장
profile.to_file('report.html')
## 보고서 표시 (Jupyter Notebook 환경에서 보고서가 바로 표시됨)
print(profile)