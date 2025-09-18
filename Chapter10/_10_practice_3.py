import matplotlib.pyplot as plt

## 월별 총 매출 계산
# retail_data_clean을 Year와 Month 단위로 그룹화 한 후 TotalPrice의 합을 구함

# YearMonth 칼럼에 label을 설정
monthly_sales['YearMonth'] = monthly_sales['Year'].astype(str) + '-' + monthly_sales['Month'].astype(str)

## 월별 총 매출 추이 시각화


## 그래프 제목 및 축 레이블 설정
plt.title('월별 총 매출 추이', fontsize=15)
plt.xlabel('연월', fontsize=12)
plt.ylabel('총 매출(£)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

## 국가별 총 매출 계산 및 상위 10개국 추출
# retail_data_clean을 Country 단위로 그룹화 한 후 TotalPrice의 합을 구함

# 역순으로 정렬한 다음 상위 10개 선택


## 국가별 총 매출 시각화 (막대 그래프)


## 그래프 제목 및 축 레이블 설정
plt.title('국가별 총 매출 (상위 10개국)', fontsize=15)
plt.xlabel('국가', fontsize=12)
plt.ylabel('총 매출(£)', fontsize=12)
plt.grid(True, axis='y') ## Y축 그리드만 표시
plt.show()