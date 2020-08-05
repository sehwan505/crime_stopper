import pandas as pd

def find_value(date,value):
    data = pd.read_csv(f"{date} google_data.csv", encoding='utf-8')
    title = pd.read_csv(f"{date} google_titles.csv",encoding='utf-8')

    data = data.transpose() # 열 행 변환
    data.columns = title[:len(data.columns)]

    a = []
    for text in data.columns:
        count_value = (data[text].str.find(value) > 0).value_counts()
        a.append(count_value[1])

    return a

count = find_value("2020-08-05","자영")
print(count)
