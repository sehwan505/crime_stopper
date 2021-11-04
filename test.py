import twitter
import json
import datetime
import pandas as pd
from read_json import find_value_json

# twitter_api = twitter.Api(consumer_key="tS0tDeWXgLfHJRzNYcW6oTMl3",
#                           consumer_secret='ZWHsgPsHLDpwIlqwINtETjvOS3SU7SSWAVhhvoFc8mkjaHNs4v',
#                           access_token_key="1294545707714539520-nzApykoUqXu4LxSU2U4YwIUyywgEcr",
#                           access_token_secret="1ZZxqKEr0NDB6ZJneWwT2WnSEwzFinmkqIAMiAmANaAxL")

# def crawling_twitter_live(query, search_words, max_count=10):
#     # query = [query,"자영판매","영상판매","변녀","영상교환"]
#     statuses = twitter_api.GetSearch(term=query, count=1)
#     # find_value_json(search_words, data)
#     for status in statuses:
#         print(status.text)
#     return 0

# crawling_twitter_live("섹트",
#                           ["고딩", "중딩", "17", "16", "15", "14", "13", "04", "03", "05", "06", "07", "판매", "노예", "교복",
#                            "자영", "자영판매", "영상판매", "합성", "거래", "자위영상", "팔아요", "팜", "조건만남"])

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