import requests
import json
import sys
import base64
import time
from machine import  emotion_analysis
def query() :
    IS_PY3 = sys.version_info.major == 3

    if IS_PY3:
        from urllib.request import urlopen
        from urllib.request import Request
        from urllib.error import URLError
        from urllib.parse import urlencode
        timer = time.perf_counter
    else:
        from urllib import urlopen
        from urllib import Request
        from urllib import URLError
        from urllib import urlencode
        if sys.platform == "win32":
            timer = time.clock
        else:
            # On most other platforms the best timer is time.time()
            timer = time.time

    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context

    #填写百度控制台中相关开通了“音频文件转写”接口的应用的的API_KEY及SECRET_KEY
    API_KEY = '******'
    SECRET_KEY = '******'


    """  获取请求TOKEN start 通过开通音频文件转写接口的百度应用的API_KEY及SECRET_KEY获取请求token"""

    class DemoError(Exception):
        pass

    TOKEN_URL = 'https://openapi.baidu.com/oauth/2.0/token'
    # SCOPE = 'brain_bicc'  # 有此scope表示有asr能力，没有请在网页里勾选 bicc
    SCOPE = 'brain_asr_async'  # 有此scope表示有asr能力，没有请在网页里勾选
    # SCOPE = 'brain_enhanced_asr'  # 有此scope表示有asr能力，没有请在网页里勾选

    def fetch_token():
        params = {'grant_type': 'client_credentials',
                  'client_id': API_KEY,
                  'client_secret': SECRET_KEY}
        post_data = urlencode(params)
        if (IS_PY3):
            post_data = post_data.encode( 'utf-8')
        req = Request(TOKEN_URL, post_data)
        try:
            f = urlopen(req)
            result_str = f.read()
        except URLError as err:
            print('token http response http code : ' + str(err.code))
            result_str = err.read()
        if (IS_PY3):
            result_str =  result_str.decode()

    #    print(result_str)
        result = json.loads(result_str)
    #    print(result)
        if ('access_token' in result.keys() and 'scope' in result.keys()):
            if not SCOPE in result['scope'].split(' '):
                raise DemoError('scope is not correct')
    #        print('SUCCESS WITH TOKEN: %s ; EXPIRES IN SECONDS: %s' % (result['access_token'], result['expires_in']))
            return result['access_token']
        else:
            raise DemoError('MAYBE API_KEY or SECRET_KEY not correct: access_token or scope not found in token response')

    """  获取鉴权结束，TOKEN end """

    """  发送查询结果请求 """

    #转写任务id列表，task_id是通过创建音频转写任务时获取到的，每个音频任务对应的值


    task_id_list = []

    with open("../speech_txt/task_id.txt", "r", encoding='utf-8') as f :
        task_id_list.append(f.read())

    print(task_id_list[0])

    for task_id in task_id_list:


        url = 'https://aip.baidubce.com/rpc/2.0/aasr/v1/query'  #查询音频任务转写结果请求地址

        body = {
            "task_ids": [task_id],
        }

        token = {"access_token":fetch_token()}

        headers = {'content-type': "application/json"}

        response = requests.post(url,params=token,data = json.dumps(body), headers = headers)

        json_dumps = json.dumps(response.json(),ensure_ascii=False)
        print(json_dumps)

        dict_json = json.loads(json_dumps)

        if dict_json['tasks_info'][0]['task_status'] == 'Success' :
            my_txt = dict_json['tasks_info'][0]['task_result']['result'][0]

            print(my_txt)

            with open('../speech_txt/lyrics.txt', "w", encoding='utf-8') as f :
                f.write(my_txt)
            emotion_analysis.emo()

        elif dict_json['tasks_info'][0]['task_status'] == 'Running':
            time.sleep(7)
            query()


            
