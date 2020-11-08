# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 23:24
# @Author  : VICTOR2022
# @File    : Test_bs4.py
# @Software: PyCharm

from bs4 import BeautifulSoup

file = open("./Baidu.html","rb")
html_data = file.read()
bs_obj = BeautifulSoup(html_data, "html.parser")

# print(bs_obj.title)
# print(bs_obj.body)

# print(bs_obj.title.string)
# print(type(bs_obj.title))

# print(bs_obj.a.attrs)

# print(type(bs_obj))
# print(bs_obj.name)
# print(bs_obj.attrs)
# print(bs_obj)

# print(bs_obj.a.string)

#文档的遍历
# print(bs_obj.head.contents)

#文档的搜索
# 字符串过滤：会查找与字符串完全匹配的内容


# 1.find_all()
# t_list = bs_obj.find_all("a")

import re
# 正则表达式搜索：使用search()方法匹配内容
# t_list = bs_obj.find_all(re.compile("a")) #只要标签包含该内容则被找出
#
#

# 方法：传入一个函数（方法），根据函数要求搜索 (了解)
# def name_is_exist(tag):
#     return tag.has_attr("a")
# #
# t_list = bs_obj.find_all(name_is_exist)
#
# for item in t_list:
#     print(item)

# print(t_list)

# 2.kwargs 参数

# t_list = bs_obj.find_all(id="head")
# t_list = bs_obj.find_all(class_=True)
#
# for item in t_list:
#     print(item)


# 3.text参数

# t_list = bs_obj.find_all(text="hao123")
# t_list = bs_obj.find_all(text = ["hao123","地图","贴吧"])

# t_list = bs_obj.find_all(text = re.compile("\d")) #应用正则表达式查找包含特定文本的内容（标签里面的字符串）
# for item in t_list:
#     print(item)


# 4.limit 参数

# t_list = bs_obj.find_all("a",limit=3) #搜索结果总数限定为3
#
# for item in t_list:
#     print(item)

#重要 css选择器
# t_list = bs_obj.select("title") #通过标签查找
#
# t_list = bs_obj.select(".mnav") #通过类名来查找
#
# t_list = bs_obj.select("#u1")   #通过id查找
#
# t_list = bs_obj.select("a[class=pf]")   #通过属性查找
#
# t_list = bs_obj.select("head > meta")  #通过子标签查找
#
# t_list = bs_obj.select(".mnav ~ .bri")  #通过兄弟节点查找
#
# for item in t_list:
#     print(item)