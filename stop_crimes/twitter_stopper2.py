import twitter
import json
import datetime
from read_json import find_value_json
import pandas as pd

twitter_api = twitter.Api(consumer_key="tS0tDeWXgLfHJRzNYcW6oTMl3",
                          consumer_secret='ZWHsgPsHLDpwIlqwINtETjvOS3SU7SSWAVhhvoFc8mkjaHNs4v',
                          access_token_key="1294545707714539520-FPWfhj9y5EhuVv0QbGoZhVn1saG6dQ",
                          access_token_secret="gYcKs9IZe0YS0gfp5ZHV6oPr3JQufsDW2zmo9JN79ONaR")
def crawling_twitter(query):
    query = [query]
    statuses = twitter_api.GetSearch(term=query, count=100)

def crawling_twitter_live(query, search_words):

    query = [query]
    output_file_name = "stream_result.json"
    with open(output_file_name, "w", encoding="utf-8") as output_file:
        stream = twitter_api.GetStreamFilter(track=query)
        count = 0
        while True:
            for tweets in stream:
                print(tweets)
                tweet_published = datetime.datetime.strptime(tweets['created_at'],'%a %b %d %H:%M:%S +0000 %Y')
                tweet_published = tweet_published + datetime.timedelta(hours=+9)
                tweet_published = tweet_published.strftime('%Y-%m-%d %H:%M:%S')
                tweets["created_at"] = tweet_published
                tweet = json.dumps(tweets, ensure_ascii=False)
                tweet= tweet.encode('utf-8', 'ignore').decode('utf-8')
                print(tweet, file=output_file, flush=True)
                count += 1
                if count == 10:
                    date = datetime.date.today().strftime("%Y-%m-%d")
                    return find_value_json(date,search_words)

crawling_twitter_live("트위터", ["알"])
