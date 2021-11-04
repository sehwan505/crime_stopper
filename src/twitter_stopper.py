from json.encoder import JSONEncoder
import tweepy
import json
import datetime
from send_twitter_dm import find_value_json

with open('config.json', 'r') as f: 
    config = json.load(f) 

auth = tweepy.OAuthHandler(config["Consumer_Key"], config["Consumer_Secret"])
auth.set_access_token(config["Access_Token"], config["Access_Token_Secret"])
api = tweepy.API(auth)


"""
    Args:
        query : 검색할 연관 단어 리스트
        stop_words : stopword 리스트
        max_count : stream에서 한 번에 받아올 게시글 개수

    Returns:
        find_value함수 호출
"""
def crawling_twitter_live(query, stop_words, max_count=500):
    output_file_name = "stream_result.json"
    date = None
    with open(output_file_name, "a+", encoding="utf-8") as output_file:
        while(True):
            for tweets in tweepy.Cursor(api.search_tweets, q=query, count=10, result_type="recent").items(10):
                print(tweets)
                tweets = tweets._json
                tweet_published = datetime.datetime.strptime(tweets['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
                tweet_published = tweet_published + datetime.timedelta(hours=+9)
                tweet_published = tweet_published.strftime('%Y-%m-%d %H:%M:%S')
                if date is None:
                    date=tweet_published
                tweets["created_at"] = tweet_published
                tweet = json.dumps(tweets, ensure_ascii=False)
                tweet= tweet.encode('utf-8', 'ignore').decode('utf-8') #이모티콘 제거
                print(tweet, file=output_file, flush=True)
            return find_value_json(date,stop_words)

