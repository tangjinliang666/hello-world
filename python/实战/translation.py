import urllib.request
import urllib.parse
import json
import time

while True:
    content = input ("请输入带翻译的内容：(输入“q！”退出程序)")
    if content == 'q!' :
        break

    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    '''
    head = {}
    head['User-Agent'] = Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3486.0 Safari/537.36
    '''

    data = {}
    data['type'] = 'AUTO'
    data['i'] = 'content'
    data['doctype']= 'json'
    data['xmlversion'] = '1.6'
    data['keyfrom']= 'fanyi.web'
    data['ue'] = 'UTF-8'
    data['typoResult'] = 'true'
    data = urllib.parse.urlencode(data).encode('utf-8')

    req = urllib.request.Request(url,data)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3486.0 Safari/537.36')

    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')

    target = json.loads(html)
    target = target['translationResult'][0][0]['tgt']

    print(target)
    time.sleep(1)
