import urllib.request

url = 'http://www.baidu.com'
response = urllib.request.urlopen(url)

# 一个类型和六个方法
print(type(response))

# 按照一个字节一个字节地去读
content = response.read().decode('utf-8')
print(content)

# 如果 read('数字') 表示只读多少个字节
content = response.read(1).decode('utf-8')
print(content)

# readline() 按行读 只读一行
content = response.readline().decode('utf-8')
print(content)

# readlines() 按行读 读完
content = response.readlines().decode('utf-8')
print(content)

# 返回状态码 如果是200 证明无错
print(response.getcode())

# 返回的是 url 地址
print(response.geturl())

# 获取的是一个状态信息
print(response.getheaders())

# 一个类型 HTTPResponse
# 六个方法 read readline readlines getcode geturl getheaders
