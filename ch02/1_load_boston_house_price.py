import pandas as pd  # 라이브러리 호출

data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'  # Data URL
df_data = pd.read_csv(data_url, sep='\s+', header=None)  # csv타입 데이터 로드, separate는 빈공간으로 지정하고, Column은 없음

print(df_data.head())  # 처음부터 다섯번째 줄까지 출력

df_data.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT',
                   'MEDV']

print(df_data.head())
