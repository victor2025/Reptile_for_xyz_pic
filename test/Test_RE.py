# -*- coding: utf-8 -*-
# @Time    : 2020/10/28 17:19
# @Author  : VICTOR2022
# @File    : Test_RE.py
# @Software: PyCharm

# 正则表达式：字符串模式，用来判断是否符合一定的标准

import re
# 创建模式对象

# pat = re.compile("AA")  #此处的参数为正则表达式，用于验证其他的字符串
# m = pat.search("ABCAAABCAAABCAA")      #search 字符串被校验的内容，只匹配第一个

# 没有模式对象
# m = re.search("Asd","Asdas")  #前面为规则，后面为校验的字符串
#
# print(m)

# print(re.findall("a","ASDAFAIifhiadiafe"))  #前面的字符串为规则（正则表达式），后面字符串为被校验的字符串，返回一个列表

# print(re.findall("[A-Z]","AONFSOAninfasdfdas")) #找到指定区间内的内容

# print(re.findall("[A-Z]+","LASFJniindakfinmenaifd"))    #根据表达式，找到指定的字符串

# sub

print(re.sub("a","A","abscsda"))    #找到a，用A替换。前一个为被替换的对象，后一个为替换的对象，最后为被操作的字符串

# 字符串中，建议在正则表达式中，被比较的字符串前面加上r，就不用再担心转义字符的问题