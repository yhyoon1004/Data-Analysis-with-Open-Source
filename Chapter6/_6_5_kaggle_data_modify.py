import pandas as pd

# Grocery Sales 데이터 DataFrame 로드
train = pd.read_csv('.kaggle/train.csv')
stores = pd.read_csv('.kaggle/stores.csv')
transactions = pd.read_csv('.kaggle/transactions.csv')
oil = pd.read_csv('.kaggle/oil.csv')
holidays_events = pd.read_csv('.kaggle/holidays_events.csv')
# 판매 데이터 살펴보기
# train.info()
