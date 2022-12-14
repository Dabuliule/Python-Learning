import urllib.request

url = 'https://www.baidu.com'

# url 的组成
# 协议 主机 端口号 路径 参数 锚点
# http/https www.baidu.com
# http 80
# https 443

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 '
                  'Safari/537.36 Edg/108.0.1462.46 '
}

# 请求对象的定制
# 解决反爬的第一种手段
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
