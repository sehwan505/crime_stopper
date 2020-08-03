import pandas as pd

data = pd.read_csv("2020-08-02 google_data.csv", encoding='utf-8')
title = pd.read_csv("google.title.csv",encoding='utf-8')

data = data.transpose() # 열 행 변환
data.columns = title[:len(data.columns)]

