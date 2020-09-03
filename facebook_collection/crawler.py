from datetime import datetime, timedelta
import json
import os
import fb_api

RESULT_DIRECTORY = '__resultes__/crawling'

# 전처리 함수
# 공유수, 전체 리액션 수, 등을 조회하기 위해서는 깊게 들어가야 하는데,
# 이를 간단하게 처리하게 하기 위함이다.
def pre_precess(post):
    # 공유수
    # 'shares': {'count': 57}  -> 'count_shares': 57
    if 'shares' not in post:
        post['count_shares'] = 0
    else:
        post['count_shares'] = post['shares']['count']
        del post['shares']

    # 전체 리액션 수
    # 'reactions': {'data': [], 'summary': {'total_count': 373, 'viewer_reaction': 'NONE'}}
    # -> 'count_reactions' : 373
    if 'reactions' not in post:
        post['count_reactions'] = 0
    else:
        post['count_reactions'] = post['reactions']['summary']['total_count']
        del post['reactions']

    # 시간 변경하기 ( 국제시 -> 국내시 )
    # 페이스북은 UTC를 사용하는데 KST는 UTC보다 9가 높다.
    kst = datetime.strptime(post['created_time'], '%Y-%m-%dT%H:%M:%S+0000')
    kst = kst + timedelta(hours=+9)
    post['created_time'] = kst.strftime('%Y-%m-%d %H:%M:%S')


def crawling(pagename, since, until):
    result = []
    filename = '%s/fb_%s_%s_%s.json' % (RESULT_DIRECTORY, pagename, since, until)

    for posts in fb_api.fb_fetch_post(pagename, since, until):
        # posts는 데이터가 30개씩 있는 리스트이다.
        for post in posts:
            pre_precess(post)
        result += posts

    # save result to file
    with open(filename, 'w', encoding='utf-8') as outfile:
        # json.dump()는 파이썬의 list, dict 등의 객체를 JSON 문자열로 바꾸는 함수이다.
        # indent는 여러행으로 예쁘게 출력하기 위함이다.
        # sort_key는 JSON안의 속성(key)를 정렬한다.
        # ensure_ascii는 false로 하여 ascii가 아닌 문자가 escape 되는 것을 막는다.
        json_string = json.dumps(result, indent=4, sort_keys=True, ensure_ascii=False )
        outfile.write(json_string)


# 현재 OS에 매개변수로 받은 이름의 디렉터리가 없다면 디렉터리를 생성하라.
if os.path.exists(RESULT_DIRECTORY) is False:
    os.makedirs(RESULT_DIRECTORY)