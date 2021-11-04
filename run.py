from scheduler import run_scheduler
from read_json import *


if __name__ ==  "__main__":
    print("""
    1. 트위터 크롤링 + 권고 디엠 보내기
    2. 추가예정    
    """)
    # inp = int(input("옵션 선택"))
    # if inp == 1:
    #     search_words = ["고딩","중딩","17","16","15","14","13","04","03","05","06","07","판매","노예","교복","자영","자영판매","합성","거래","자위영상","합사","팔아요"]
    #     while True:
    #         a = input("트위터 검색어 추가( 0 을 입력하면 프로그램 시작)")

    #         if a == "0":
    #             print("검색어:", search_words)
    #             break
    #         search_words.append(a)
    run_scheduler()