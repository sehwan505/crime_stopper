import pandas as pd

def find_value(date,values):
    data = pd.read_csv(f"{date} google_data.csv", encoding='utf-8')
    title = pd.read_csv(f"{date} google_titles.csv",encoding='utf-8',header=None)

    data = data.transpose() # 열 행 변환
    print(data)
    data.columns = title[:len(data.columns)]
    count_list = []
    for value in values:
        a = []
        for text in data.columns:
            count_value = (data[text].str.find(value) > 0).value_counts()
            a.append(len(data[text])-count_value[0])
        count_list.append(a)
    count_list = pd.DataFrame(count_list,columns=data.columns)

    with open('urls.csv', 'a') as f:
        count_list.to_csv(f,index=0)
    return count_list


