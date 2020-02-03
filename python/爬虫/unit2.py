import requests

url = 'https://www.xicidaili.com/nn/'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36'}

response = requests.get(url=url,headers=headers)

code = response.status_code

print(code)

if code == 200:
    with open("./test.html","w") as fp:
        fp.write(response.text)
        

