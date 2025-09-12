import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import set_random_seed
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris

# 랜덤 시드 값 설정
set_random_seed(42)

## 아이리스 데이터셋 로드 및 전처리
iris = load_iris()
X = iris.data
y = tf.keras.utils.to_categorical(iris.target, num_classes=3) ## 타겟 변수를 원-핫 인코딩
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

## 특성 스케일링
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

## 신경망 모델 구축
# 이 모델은 다층 퍼셉트론(MLP) 신경망으로, 3개의 완전 연결층(2개의 은닉층과 1개의 출력층)으로 구성
# 입력 특징은 총 4개, 각 층의 노드(뉴런) 수는 순서대로 10개, 8개, 3개
model = Sequential([
    Dense(10, activation='relu', input_shape=(4, )), # 첫 번째 은닉층
    Dense(8, activation='relu'),                     # 두 번째 은닉층
    Dense(3, activation='softmax')                   # 출력층 (3개 클래스 분류)
    ])

## 모델 컴파일
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

## 모델 구조 요약 출력
model.summary()

## 모델 학습
history = model.fit(X_train, y_train,
                    epochs=100,
                    batch_size=16,
                    validation_split=0.2,
                    verbose=0) ## 학습 과정 출력 비활성화

## 모델 평가
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f'테스트 정확도: {accuracy:.4f}')