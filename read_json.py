import pandas as pd
from twitter_dm_bot import twitter_dm_bot
import json


def find_value_json(date, values, live=True):
    # if live==False:
    #     data = pd.read_json("stream_result2.json", lines=True)
    #     data=data[-100:]
    #     print(data)
    data = pd.read_json("stream_result.json", lines=True)
    data_index = data[data["created_at"].astype("str") == date].index.values[0]
    data = data.iloc[data_index:,:]
    #전체 데이터에서 방금 뽑은 데이터만 분류
    print(data["text"])
    count_list = pd.DataFrame()
    for value in values:
        count_value = (data["text"].str.find(value).rename(value) > 0)
        count_list = pd.concat([count_list, count_value], axis=1)
        # for user in data["user"]:
        #     if user['name'] == None:
        #         user['name'] = "0"
        #     if user['description'] == None:
        #         user['description'] = "0"
        #     print("name:",user["name"].find(value),user["name"])
        #     print("des:",user["description"].find(value),user["description"])

    count_list = pd.concat([count_list, data], axis=1)

    date = date[:13]
    count_list.to_csv(f"data_twitter_google/{date} twitter_data.csv", index=0)
    twitter_dm_bot(count_list,values)
    return 0

# find_value_json("2020-08-31 20:10:06",["암"])