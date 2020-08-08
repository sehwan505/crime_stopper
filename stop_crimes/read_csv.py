import pandas as pd

def find_value(date,values):
    data = pd.read_csv(f"{date} google_data.csv", encoding='utf-8')
    title = pd.read_csv(f"{date} google_titles.csv",encoding='utf-8')

    data = data.transpose() # 열 행 변환
    data.columns = title[:len(data.columns)]
    count_list = []
    for value in values:
        a = []
        for text in data.columns:
            count_value = (data[text].str.find(value) > 0).value_counts()
            a.append(len(data[text])-count_value[0])
        count_list.append(a)
        count = pd.DataFrame(count_list)
    return count

count = pd.DataFrame(find_value("2020-08-05",["자영","빅데이터","이","이란"]))
sum = count.sum(axis=0)

print(count, sum)

