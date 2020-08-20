import pandas as pd
import json

def find_value_json(date,values):
    with open('stream_result.json', encoding="UTF-8",newline='\n') as f:
        data = json.load(f)
    data = pd.DataFrame(data)
    print(data["text"])
    count_list = pd.DataFrame()
    for value in values:
        count_value = (data["text"].str.find(value).rename(value) > 0)
        count_list=pd.concat([count_list,count_value],axis=1)
    count_list = pd.concat([count_list,data], axis=1)
    count_list.to_csv(f"{date} twitter_data.csv", index=0)
    return count_list

