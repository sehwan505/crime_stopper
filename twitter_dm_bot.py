import tweepy
import pandas as pd
Consumer_Key = "tS0tDeWXgLfHJRzNYcW6oTMl3"#Applications Setting의 Consumer Key(API Key)
Consumer_Secret = "ZWHsgPsHLDpwIlqwINtETjvOS3SU7SSWAVhhvoFc8mkjaHNs4v"#Applications Setting의 Consumer Secret(API Secret)

auth = tweepy.OAuthHandler(Consumer_Key,Consumer_Secret)
Access_Token = "1294545707714539520-nzApykoUqXu4LxSU2U4YwIUyywgEcr"#위에서 생성한 Access Token
Access_Token_Secret = "1ZZxqKEr0NDB6ZJneWwT2WnSEwzFinmkqIAMiAmANaAxL"#위에서 생성한 Access Token Secret
auth.set_access_token(Access_Token,Access_Token_Secret)
api = tweepy.API(auth)
def twitter_dm_bot(count_list,values):
    ans = count_list[values].sum(axis=1) >= 1
    id_list=pd.read_csv("twitter_id2.csv")
    for i in count_list[ans]["user"]:

        try:
            id = i["id"]
            if (id_list["id"] == id).sum() > 0:
                continue
            else:
                id_list = id_list.append({"id": id,"name":i["name"],"screen_name":i["screen_name"]}, ignore_index=True)
            api.send_direct_message(id,text="아동 및 청소년을 대상으로 하실 경우 하고 있는 행동은 사이버 성폭력이 될 수 있습니다. 혹은 본인이 아동및 청소년일 경우 사이버 성폭력의 대상이 될 가능성이 매우 높습니다. 아래의 예방수칙을 숙지하시기 바랍니다.")
            img = api.media_upload('rules2.jfif') #사진 올리고 아래에서 media_id 받아서 보냄
            api.send_direct_message(id, '하고 있는 일에 대해서 다시 생각해보시기를 바라며 그만두시기를 추천드립니다, 혹여 본인의 행동에 전혀 문제가 없다고 생각하시거나 더 이상 알림 메시지를 받고 싶지 않으시면 이 계정을 차단해주시면 감사하겠습니다', attachment_type='media', attachment_media_id=img.media_id)

        except:
            continue
    print(id_list)
    id_list.to_csv("twitter_id2.csv", index=0)
    return 0
