from urllib import request, parse
import ssl

# 对于https网站，我们需要使用ssl来取消验证
context = ssl._create_unverified_context()
url = "http://www.baidu.com"
# biihu.cc//account/ajax/login_process
# 普通方式，不推荐
# response = request.urlopen(url)
# print(response.read().decode('utf-8'))
# 更好的方式
request.Request(url)  # 一共4个参数：url,data=None,headers={},method=None
url = "https://biihu.cc//account/ajax/login_process"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.57'}
my_dic = {'return_url': 'https://biihu.cc/',
          'username': 'xiaoshuaib@gmail.com',
          'password': '123456789',
          '_post_type': 'ajax'}
data = bytes(parse.urlencode(my_dic), 'utf-8')
req = request.Request(url, data, headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))

