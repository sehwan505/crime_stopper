import tweepy
import pandas as pd

Consumer_Key = "tS0tDeWXgLfHJRzNYcW6oTMl3"#Applications Setting의 Consumer Key(API Key)
Consumer_Secret = "ZWHsgPsHLDpwIlqwINtETjvOS3SU7SSWAVhhvoFc8mkjaHNs4v"#Applications Setting의 Consumer Secret(API Secret)
auth = tweepy.OAuthHandler(Consumer_Key,Consumer_Secret)
Access_Token = "1294545707714539520-nzApykoUqXu4LxSU2U4YwIUyywgEcr"#위에서 생성한 Access Token Secret
Access_Token_Secret = "1ZZxqKEr0NDB6ZJneWwT2WnSEwzFinmkqIAMiAmANaAxL"
auth.set_access_token(Access_Token,Access_Token_Secret)
api = tweepy.API(auth)

"""
    Args:
        date : 오늘 날짜
        values : stop word 리스트 

    Returns:
        null 반환
"""
def find_value_json(date, values):
    data = pd.read_json("stream_result.json", lines=True)
    data_index = data[data["created_at"].astype("str") == date].index.values[0]
    data = data.iloc[data_index:,:]
    #전체 데이터에서 방금 뽑은 데이터만 분류
    count_list = pd.DataFrame()
    for value in values:
        count_value = (data["text"].str.find(value).rename(value) > 0)
        count_list = pd.concat([count_list, count_value], axis=1)
    count_list = pd.concat([count_list, data], axis=1)

    date = date[:13]
    count_list.to_csv(f"data_twitter/{date} twitter_data.csv", index=0)
    twitter_dm_bot(count_list,values)
    return 0

""" stopword에 걸리는 게시글을 올린 사용자에게 warning dm 보냄
    Args:
        count_list : stop word에 걸리는 개수 list
        values : stop word 리스트 

    Returns:
        null 반환
"""
def twitter_dm_bot(count_list,values):
    ans = count_list[values].sum(axis=1) >= 1
    id_list=pd.DataFrame()#pd.read_csv("twitter_id.csv")
    for i in count_list[ans]["user"]:
        try:
            id = i["id"]
            if (id_list["id"] == id).sum() > 0:
                continue
            else:
                id_list = id_list.append({"id": id,"name":i["name"],"screen_name":i["screen_name"]}, ignore_index=True)
            api.send_direct_message(id,text="아동 및 청소년을 대상으로 하실 경우 하고 있는 행동은 사이버 성폭력이 될 수 있습니다 이는 범법행위임을 인지하시기 바랍니다. 혹은 본인이 아동및 청소년일 경우 사이버 성폭력의 대상이 될 가능성이 매우 높습니다. 아래의 예방수칙을 숙지하시기 바랍니다.")
            img = api.media_upload('images/rules2.jfif') #사진 올리고 아래에서 media_id 받아서 보냄
            api.send_direct_message(id, '하고 있는 일에 대해서 다시 생각해보시기를 바라며 그만두시기를 추천드립니다, 혹여 본인의 행동에 전혀 문제가 없다고 생각하시거나 더 이상 알림 메시지를 받고 싶지 않으시면 이 계정을 차단해주시면 감사하겠습니다', attachment_type='media', attachment_media_id=img.media_id)
        except:
            continue
    print(id_list)
    id_list.to_csv("twitter_id.csv", index=0)
    return 0
