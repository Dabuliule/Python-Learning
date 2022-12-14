import urllib.request

# 下载网页
url_page = 'http://www.baidu.com'

# url 代表的是下载的路径 filename 代表文件的名字
urllib.request.urlretrieve(url_page, 'baidu.html')

# 下载图片
url_img = 'https://static2.yan.vn/YanNews/2167221/201902/14-ed11bbda.jpg'
urllib.request.urlretrieve(url=url_img, filename='lisa.jpg')


