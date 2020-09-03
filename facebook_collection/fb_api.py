from urllib.parse import urlencode
import json_request as jr

BASE_URL_FB_API = 'https://graph.facebook.com/v8.0'
ACCESS_TOKEN = 'EAAKPb6HM4LsBAPNJpqpaEMkNMM6OZAOWpPlqc4eB5onohQqDxWZCI7JbPIQsf77ha01CiEQEuzJtZA7CNGbmvXZC08MPMCWRmMQD0UJnMQ3nbqAc4Xc5ZCX5U0o3xjxhKeJVMcuRNKUEIJZCfoSfmLrPQIMml4urVFIrsIb6XrX5G7NFXapaqSjyZAIBDEpjIUZD'


# 여러 파라미터에 대하여, url을 생성
def fb_generate_url(base=BASE_URL_FB_API, node='', **param):
    return '%s/%s/?%s' % (base, node, urlencode(param))


# API를 사용할 때 'JTBC 뉴스' 라는 페이지 이름이 아닌, 페이지의 id가 필요하다.
# 여기서 매개변수 pagename은 JTBC 뉴스 페이지 URL( https://www.facebook.com/jtbcnews/?ref=br_rs )에 붙은 것을 의미한다.
def fb_name_to_id(pagename):
    url = fb_generate_url(node = pagename, access_token = ACCESS_TOKEN)
    print(url)
    json_result = jr.json_request(url)
    print(json_result)
    return json_result.get('id')


# 게시글 가져오기 - 크롤러는 최종적으로 이 함수를 사용한다.
# 인자로 페이스북 페이지명과 게시글 일자 기간을 넘겨준다.
def fb_fetch_post(pagename, since, until):
    # URL 생성 시, 여러 파라미터를 전달
    url = fb_generate_url(
        node = fb_name_to_id(pagename) + '/posts',
        fields = 'id, message, link, name, type, shares, created_time,\
                  reactions.limit(0).summary(true),\
                  comments.limit(0).summary(true)',
        since = since,  # 시작 날짜
         until = until,  # 끝 날짜
         limit = 30,     # 개수
         access_token = ACCESS_TOKEN
    )
    print(url)
    json_result = jr.json_request(url)
    return json_result

posts = fb_fetch_post('jtbcnews', '2018-05-01', '2018-05-30')
print(posts)