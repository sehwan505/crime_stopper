import twitter
import json
import datetime
from read_json import find_value_json
import pandas as pd

twitter_api = twitter.Api(consumer_key="tS0tDeWXgLfHJRzNYcW6oTMl3",
                          consumer_secret='ZWHsgPsHLDpwIlqwINtETjvOS3SU7SSWAVhhvoFc8mkjaHNs4v',
                          access_token_key="1294545707714539520-nzApykoUqXu4LxSU2U4YwIUyywgEcr",
                          access_token_secret="1ZZxqKEr0NDB6ZJneWwT2WnSEwzFinmkqIAMiAmANaAxL")
def crawling_twitter(query, search_words):
    query = [query]
    statuses = twitter_api.GetSearch(term=query, count=100)
    output_file_name = "stream_result2.json"
    # with open(output_file_name, "a+", encoding="utf-8") as output_file:
    #     for tweets in statuses:
    #         print(tweets)
    #         tweet_published = datetime.datetime.strptime(tweets['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
    #         tweet_published = tweet_published + datetime.timedelta(hours=+9)
    #         tweet_published = tweet_published.strftime('%Y-%m-%d %H:%M:%S')
    #         tweets["created_at"] = tweet_published
    #         tweet = json.dumps(tweets, ensure_ascii=False)
    #         tweet = tweet.encode('utf-8', 'ignore').decode('utf-8')  # 이모티콘 제거
    #         date = tweet_published
    #         print(tweet, file=output_file, flush=True)
    #         return find_value_json(date, search_words, live=False)

def crawling_twitter_live(query, search_words, max_count=500):
    query = [query,"자영판매","영상판매"]
    output_file_name = "stream_result.json"
    with open(output_file_name, "a+", encoding="utf-8") as output_file:
        stream = twitter_api.GetStreamFilter(track=query)
        count = 0
        while True:
            for tweets in stream:

                print(tweets)
                tweet_published = datetime.datetime.strptime(tweets['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
                tweet_published = tweet_published + datetime.timedelta(hours=+9)
                tweet_published = tweet_published.strftime('%Y-%m-%d %H:%M:%S')
                if count==0:
                    date=tweet_published
                tweets["created_at"] = tweet_published
                tweet = json.dumps(tweets, ensure_ascii=False)
                tweet= tweet.encode('utf-8', 'ignore').decode('utf-8') #이모티콘 제거
                print(tweet, file=output_file, flush=True)
                count += 1
                if count == max_count:
                    return find_value_json(date,search_words)

