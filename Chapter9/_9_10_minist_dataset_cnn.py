from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import set_random_seed
import matplotlib.pyplot as plt
import tensorflow as tf

# 랜덤 시드 값 설정
set_random_seed(42)

## MNIST 데이터셋 로드 및 전처리
(X_train, y_train), (X_test, y_test) = mnist.load_data()

## 이미지 데이터 형태 변환 및 정규화
X_train = X_train.reshape(-1, 28, 28, 1) / 255.0
X_test = X_test.reshape(-1, 28, 28, 1) / 255.0
## 타겟 레이블을 원-핫 인코딩
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

## CNN 모델 구축
# 이 모델은 이미지 처리에 특화된 합성곱 신경망(CNN)
# 입력 이미지의 형태는 **(높이, 너비, 채널)**이며, 28x28 흑백 이미지의 이므로 (28, 28, 1)
# **두 계층의 합성곱 층**, **평탄화 후 완전 연결층**, 그리고 **출력층**으로 구성
model = Sequential([
    # 첫번쨰 합성곱
    Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)),
    # 첫번째 풀링
    MaxPooling2D(pool_size=(2, 2)),
    # 두번쨰 합성곱
    Conv2D(64, kernel_size=(3, 3), activation='relu'),
    # 두번쨰 풀링
    MaxPooling2D(pool_size=(2, 2)),
    # 1차원 평탄화
    Flatten(),
    # 완전 연결 층
    Dense(128, activation='relu'),
    # 출력층 10개 클래스 분류
    Dense(10, activation='softmax')
])

## 모델 컴파일
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

## 모델 학습
model.fit(X_train, y_train, batch_size=128, epochs=5, validation_split=0.1, verbose=1)

## 모델 평가
score = model.evaluate(X_test, y_test, verbose=0)
print(f'테스트 정확도: {score[1]:.4f}')

## 예측 결과 시각화
predictions = model.predict(X_test[:5])
fig, axes = plt.subplots(1, 5, figsize=(15, 3))
for i, ax in enumerate(axes):
    ax.imshow(X_test[i].reshape(28, 28), cmap='gray')
    predicted_label = tf.argmax(predictions[i]).numpy()
    true_label = tf.argmax(y_test[i]).numpy()
    ax.set_title(f'예측: {predicted_label}, 실제: {true_label}')
    ax.axis('off')
plt.rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False  # - 가 아스키표현 안되는문제 처리
plt.tight_layout()
plt.show()