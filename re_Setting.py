import re

class ReSetting():
    def __init__(self):
        # 影片详情链接的规则，只会查找到括号里面的内容
        self.find_link = re.compile(r'<a href="(.*?)">')    #创建正则表达式对象，表示规则（字符串的模式）
        # 影片图片链接，re.S让换行符包含在字符中
        self.find_img_link = re.compile(r'<img.*src="(.*?)"',re.S)
        # 影片片名
        self.find_title = re.compile(r'<span class="title">(.*)</span>')
        # 影片评分
        self.find_rating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
        # 评价人数
        self.find_judge_number = re.compile(r'<span>(\d*)人评价</span>')
        # 电影概况
        self.find_inq = re.compile(r'<span class="inq">(.*)</span>')
        # 相关内容
        self.find_bd = re.compile(r'<p class="">(.*?)</p>',re.S)