import urllib.parse
import  urllib.request

base_url = 'https://www.baidu.com/s?'

data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '中国台湾省'
}

data = urllib.parse.urlencode(data)

url = base_url + data

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 '
                  'Safari/537.36 Edg/108.0.1462.46 '
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
