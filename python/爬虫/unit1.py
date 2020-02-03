import requests
import re
#下载一个网页
i = 1
url = 'https://www.kanshuhai.com/0/5/5218/?btwaf=54398728'
#模拟浏览器发送http请求
response = requests.get(url)  
#编码方式
response.encoding = 'gbk'
#目标小说主页的网页源码
html = response.text
#小说名称
title = re.findall(r'<meta name="keywords" content="(.*?)" />',html)[0]
#新建一个文本
fb = open('%s.txt' % title, 'w', encoding='gbk')
#获取每一章的信息（章节、url）
dl = re.findall(r'<dt>正文</dt>.*?</dl>',html,re.S)[0]
chapter_info_list = re.findall(r'href="(.*?)">(.*?)<',dl)
#循环每个章节，分别去下载
for chapter_info in chapter_info_list:
#    chapter_title = chapter_info[1]
#    chapter_url = chapter_info[0]
    chapter_url_false,chapter_title = chapter_info
#    chapter_url = chapter_url.replace('\" ccc=\"(.*?)','')
    chapter_url = re.findall(r'.*shtml',chapter_url_false)[0]
#    chapter_url = chapter_url&chapter_url_false
    chapter_url = 'https://www.kanshuhai.com/0/5/5218/%s' % chapter_url
    #下载章节内容
    chapter_respomse = requests.get(chapter_url)
    chapter_respomse.encoding = 'gbk'
    chapter_html = chapter_respomse.text
    #提取章节内容
    chapter_content = re.findall(r'<div id="con_left">(.*?)<div class="con_R">',chapter_html,re.S)[0]
    #清洗数据   
    chapter_content = chapter_content.replace(' ', '')
    chapter_content = chapter_content.replace('&nbsp;', '')
    chapter_content = chapter_content.replace('<br/>', '')
    chapter_content = chapter_content.replace('</div>', '')
    #数据持久化
    fb.write(chapter_title)
    fb.write('\n')
    fb.write(chapter_content)
    fb.write('\n')
    i = i + 1
    print(i)
    print(chapter_url)