import requests

#定义请求的url

url = 'https://www.bilibili.com/'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
           'Cookie':'_uuid=3B8AD97F-2FA7-49FD-FFE1-6F5C902B33B852595infoc; buvid3=98B15D0C-1B89-40DA-89B7-DEE1D683E4E1190972infoc; LIVE_BUVID=AUTO9715663819562727; CURRENT_FNVAL=16; stardustvideo=1; rpdid=|(umY~|lu~Jm0J\'ulYYJ)um~Y; sid=kdy687kt; UM_distinctid=16daaed41eb1c7-051930995adfb1-19117259-100200-16daaed41ec47e; DedeUserID=64697333; DedeUserID__ckMd5=2cb6a1b4a92d1e8e; CURRENT_QUALITY=64; SESSDATA=cfc52d2e%2C1578040057%2Cdbfd7ec1; bili_jct=b96bd64073940dc7a57087bb55d9a0b5; INTVER=1'}

response = requests.get(url=url,headers=headers)
html = response.text
print(html)
code = response.status_code

print(code)

if code == 200:
    with open('./test.html','w',encoding='utf-8') as fp:
        fp.write(response.text)