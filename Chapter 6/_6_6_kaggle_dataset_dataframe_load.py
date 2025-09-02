import pandas as pd
from _6_5_kaggle_data_modify import *

# 판매 데이터 기본 통계량
desc_train = train.describe()
print(desc_train)
print("-----")

# 매장 데이터 기본 정보
stores_head = stores.head()
print(stores_head)
print("-----")

# 원유 가격 데이터 기본 정보
oil_head = oil.head()
print(oil_head)
print("-----")
