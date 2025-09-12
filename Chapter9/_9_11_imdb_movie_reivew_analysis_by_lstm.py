from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from tensorflow.keras.utils import set_random_seed

# 랜덤 시드 값 설정
set_random_seed(42)

## 데이터셋 로드 및 전처리
vocab_size = 10000 ## 사용할 단어의 최대 개수
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=vocab_size) ## IMDB 데이터셋 로드

# 학습 데이터 크기 축소
X_train = X_train[:len(X_train) // 20]
y_trian = y_train[:len(y_train) // 20]

max_length = 200 ## 시퀀스(리뷰)의 최대 길이
X_train = pad_sequences(X_train, maxlen=max_length) ## 시퀀스 길이 맞추기 (패딩)
X_test = pad_sequences(X_test, maxlen=max_length)

## LSTM 모델 구축
embedding_dim = 128 ## 임베딩 벡터 차원
# 이 모델은 시퀀스 데이터(예: 텍스트) 처리에 특화된 순환 신경망(Recurrent Neural Network, RNN)의 한 종류인 LSTM을 사용
# 주요 구성은 임베딩 층, LSTM 층, 그리고 출력층으로 구성
model = Sequential([
    # 임베딩 층
    Embedding(vocab_size, embedding_dim, input_length=max_length),
    # LSTM 층
    LSTM(128, dropout=0.2, recurrent_dropout=0.2),
    # 이진 분류를 위한 출력 (긍정/부정)
    Dense(1, activation='sigmoid')
])




## 모델 컴파일
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

## 모델 학습
model.fit(X_train, y_train, batch_size=32, epochs=1, validation_split=0.2)

## 모델 평가
score = model.evaluate(X_test, y_test, verbose=0)
print(f'테스트 정확도: {score[1]:.4f}')

# 테스트 정확도: 0.6303
