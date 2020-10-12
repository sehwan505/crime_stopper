import tweepy
import pandas as pd
import time
Consumer_Key = "tS0tDeWXgLfHJRzNYcW6oTMl3"#Applications Setting의 Consumer Key(API Key)
Consumer_Secret = "ZWHsgPsHLDpwIlqwINtETjvOS3SU7SSWAVhhvoFc8mkjaHNs4v"#Applications Setting의 Consumer Secret(API Secret)

auth = tweepy.OAuthHandler(Consumer_Key,Consumer_Secret)
Access_Token = "1294545707714539520-nzApykoUqXu4LxSU2U4YwIUyywgEcr"#위에서 생성한 Access Token
Access_Token_Secret = "1ZZxqKEr0NDB6ZJneWwT2WnSEwzFinmkqIAMiAmANaAxL"#위에서 생성한 Access Token Secret
auth.set_access_token(Access_Token,Access_Token_Secret)
api = tweepy.API(auth)

id_list = pd.read_csv("twitter_id4.csv")
for id in id_list[1300:]["id"]:
    try:
        api.send_direct_message(id,text="아동 및 청소년을 대상으로 하실 경우 하고 있는 행동은 사이버 성폭력이 될 수 있습니다 이는 범법행위임을 인지하시기 바랍니다. 혹은 본인이 아동및 청소년일 경우 사이버 성폭력의 대상이 될 가능성이 매우 높습니다. 아래의 예방수칙을 숙지하시기 바랍니다.")
        img = api.media_upload('rules2.jfif') #사진 올리고 아래에서 media_id 받아서 보냄
        api.send_direct_message(id, '하고 있는 일에 대해서 다시 생각해보시기를 바라며 그만두시기를 추천드립니다, 혹여 본인의 행동에 전혀 문제가 없다고 생각하시거나 더 이상 알림 메시지를 받고 싶지 않으시면 이 계정을 차단해주시면 감사하겠습니다', attachment_type='media', attachment_media_id=img.media_id)
    except:
        print(1)
        continue

id_list = pd.read_csv("twitter_id4.csv")
# list = []
# def get_dm(id):
#     try:
#         list.append(api.get_direct_message(id))
#     except:
#         pass
#     return 0
# id_list["id"].apply(get_dm)
# print(list)
#
# list = []
# for idx,i in enumerate(a["id"]):
#     time.sleep(50)
#     try:
#         b = api.followers(i)
#         if idx == 50:
#             break
#         for j in b:
#             print(j._json["screen_name"])
#             list.append([j._json["name"],j._json["screen_name"]])
#     except Exception as e:
#         print(e)
#         continue
# list = pd.DataFrame(list, columns=["name","screen_name"])
# list.to_csv("friends.csv",index=0)
# print(list)