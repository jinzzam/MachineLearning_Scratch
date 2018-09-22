import pandas as pd  # 라이브러리 호출
import numpy as np

data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'  # Data URL
df_data = pd.read_csv(data_url, sep='\s+', header=None)  # csv타입 데이터 로드, separate는 빈공간으로 지정하고, Column은 없음

print(df_data.head())  # 처음부터 다섯번째 줄까지 출력

df_data.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT',
                   'MEDV']

print(df_data.head())
print(df_data.values)  # 값을 numpy array 형태로 표현

df_data['weight_0'] = 1  # weight 0 값 추가
df_data = df_data.drop("MEDV", axis=1)  # drop : pandas 라이브버리 내 함수, 데이터 떨궈냄, 값 제거
print(df_data.head())

df_matrix = df_data.as_matrix()  # matrix data 로 변환하기
weight_vector = np.random.random_sample((14, 1))

print(df_data.shape)  # matrix 크기 확인
print(df_matrix.dot(weight_vector).shape)  # 506 by 1
