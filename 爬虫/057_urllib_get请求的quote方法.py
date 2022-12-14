"""获取 https://www.baidu.com/s?wd=周杰伦 的网页源码"""

import urllib.request
import urllib.parse

url = 'https://www.baidu.com/s?wd='

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 '
                  'Safari/537.36 Edg/108.0.1462.46 '
}

# 将'周杰伦'变成unicode编码的格式
name = urllib.parse.quote('周杰伦')

url = url + name

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
