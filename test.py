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


a = pd.read_csv("twitter_id2.csv")

list = []
for idx,i in enumerate(a["id"]):
    time.sleep(50)
    try:
        b = api.followers(i)
        if idx == 50:
            break
        for j in b:
            print(j._json["screen_name"])
            list.append([j._json["name"],j._json["screen_name"]])
    except Exception as e:
        print(e)
        continue
list = pd.DataFrame(list, columns=["name","screen_name"])
list.to_csv("friends.csv",index=0)
print(list)