# from scheduler import
from twitter_stopper2 import *
from read_json import *
from google_crawling import google_crawling


if __name__ ==  "__main__":
    print("""
    1. 트위터 크롤링 + 권고 디엠 보내기
    2. 구글 크롤링 + 위험가능성 있는 url 저장
    
    
    """)
    inp = int(input("옵션 선택"))
    if inp == 1:
        search_words = ["고딩","중딩","17","16","15","14","13","04","03","05","06","07","판매","노예","교복","자영","자영판매","합성","거래","자위영상","합사","팔아요"]
        query = input("검색어")
        while True:
            a = input("파일 내 검색어 추가( 0 을 입력하면 종료)")

            if a == "0":
                print("검색어:", search_words)
                break
            search_words.append(a)
        crawling_twitter_live(query, search_words)
    elif inp == 2:
        search_words = ["고딩","중딩","19","18","17","16","15","14","13","04","03","05","06","07","판매","노예","교복","자영","자영판매","합성","거래","자위영상","합사","팔아요"]
        query = input("검색어")
        while True:
            a = input("파일 내 검색어 추가( 0 을 입력하면 종료)")
            if a == "0":
                break
            search_words.append(a)
        google_crawling(query, search_words)
    elif inp == 3:
        search_words = ["고딩","중딩","19","18","17","16","15","14","13","04","03","05","06","07","판매","노예","교복","자영","자영판매","합성","거래","자위영상","합사","팔아요"]
        query = input("검색어")
        while True:
            a = input("파일 내 검색어 추가( 0 을 입력하면 종료)")
            if a == "0":
                break
            search_words.append(a)
        crawling_twitter(query, search_words)
