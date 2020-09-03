import crawler as crawler

if __name__ == '__main__':
    items = [
        {
            # jtbc 뉴스
            'pagename': 'jtbcnews',
            'since': '2018-05-01',
            'until': '2018-05-30'
        },
        {   # 대한민국 청와대
            'pagename': 'TheBlueHouseKR',
            'since': '2018-05-01',
            'until': '2018-05-30'
        }
    ]

    for item in items:
        resultfile = crawler.crawling(**item)