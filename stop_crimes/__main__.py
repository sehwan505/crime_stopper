# from scheduler import
from twitter_stopper2 import *
from read_json import *
from google_crawling import google_crawling


if __name__ ==  "__main__":
    print("""
    1. 트위터 크롤링
    2. 구글 크롤링
    3. 트위터 데이터 읽기    
    
    
    """)
    inp = int(input("옵션 선택"))
    if inp == 1:
        search_words = []
        query = input("검색어")
        while True:
            a = input("파일 내 검색어( 0 을 입력하면 종료)")

            if a == "0":
                print("검색어:", search_words)
                break
            search_words.append(a)
        crawling_twitter_live(query, search_words)
    elif inp == 2:
        search_words = []
        query = input("검색어")
        while True:
            a = input("파일 내 검색어( 0 을 입력하면 종료)")
            if a == "0":
                break
            search_words.append(a)
        google_crawling(query, search_words)

