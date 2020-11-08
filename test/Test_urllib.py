# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 14:25
# @Author  : VICTOR2022
# @File    : Test_urllib.py
# @Software: PyCharm

import urllib.request
import urllib.parse

# 获取get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode("utf-8"))  #对获取到的网页进行utf-8解码

# #获取post请求
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response = urllib.request.urlopen("http://www.httpbin.org/post",data=data)
# print(response.read().decode("utf-8"))  #对获取到的网页进行utf-8解码

# # 超时处理
# try:
#     response = urllib.request.urlopen("http://www.httpbin.org/get",timeout=1)
#     print(response.read().decode("utf-8"))  #对获取到的网页进行utf-8解码
# except urllib.error.URLError as e:
#     print("请求超时！")

# # 响应头问题
# response = urllib.request.urlopen("https://www.baidu.com",timeout=1)
# # print(response.status)
# print(response.getheader("Server"))

# 伪装身份
url="https://www.douban.com"
data = bytes(urllib.parse.urlencode({"name":"eric"}),encoding="utf-8")
herders = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
}
req=urllib.request.Request(url=url,data=data,headers=herders,method="POST")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))