import pandas as pd
import json

data = {
    "이름": "홍길동",
    "나이": 25,
    "거주지": "서울",
    "관심사": ["프로그래밍", "데이터 분석", "여행"]
}

## json.dump를 이용한 저장

with open('output.json', mode='w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)#json으 아스키코드만 저장

## DataFrame을 이용한 저장

js = pd.read_json('output.json')


df = pd.DataFrame([data])
# df.to_json('output_df_by_record.json',orient='records', indent=4, force_ascii=False)
df.to_json('output_df_by_column.json',orient='columns', indent=4, force_ascii=False)

