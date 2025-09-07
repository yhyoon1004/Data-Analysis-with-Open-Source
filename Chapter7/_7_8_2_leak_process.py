import matplotlib.pyplot as plt
import missingno as msno
import pandas as pd


train = pd.read_csv('.kaggle/train.csv')
stores = pd.read_csv('.kaggle/stores.csv')
transactions = pd.read_csv('.kaggle/transactions.csv')
oil = pd.read_csv('.kaggle/oil.csv')
holidays_events = pd.read_csv('.kaggle/holidays_events.csv')

## 판매, 매장, 거래, 원유, 휴일이벤트 데이터 결측치
print(train.isnull().sum())
print(stores.isnull().sum())
print(transactions.isnull().sum())
print(oil.isnull().sum())
print(holidays_events.isnull().sum())

msno.matrix(oil)
plt.title("원유 가격 데이터 결측치 분포")
plt.show()

oil['date'] = pd.to_datetime(oil['date'])
plt.figure(figsize=(12, 6))
plt.plot(oil['date'], oil['dcoilwtico'])
plt.title("시간에 따른 원유 가격 변화")
plt.xlabel("날짜")
plt.ylabel("원유 가격")
plt.grid(True)
plt.show()


