import sys
from urllib.request import Request, urlopen
from datetime import *
import json


# error 로그 출력
def json_request_error(e):
    print('{0}: {1}'.format(e, datetime.now()), file=sys.stderr)


# success, error에 함수를 등록해주면 그 함수를 실행시키겠다는 의미.
# js에서 ajax의 success, error와 유사
def json_request(url='', encoding='utf-8',
                 success=None,
                 error=json_request_error):
    try:
        req = Request(url)  # request 객체 생성
        res = urlopen(req)  # URL에 연결하여 response 객체 반환
        if res.getcode() == 200:
            res_body = res.read().decode(encoding)  # json string
            # print(res_body, type(res_body))
            res_json = json.loads(res_body)  # python 자료형인 Dictionary로 반환
            print(res_json)


            return res_json


    except Exception as e:
        callable(error) and error('%s %s' % (str(e), url))
