import re

def get_all(re_setting,item):
    data = []
    get_link(re_setting.find_link,item,data)
    get_img_link(re_setting.find_img_link,item,data)
    get_titles(re_setting.find_title,item,data)
    get_rating(re_setting.find_rating,item,data)
    get_judge_number(re_setting.find_judge_number,item,data)
    get_inq(re_setting.find_inq,item,data)
    get_bd(re_setting.find_bd,item,data)
    return data


def get_link(find_link,item,data):
    # 获取到影片详情的链接
    link = re.findall(find_link, item)[0]  # 使用re库通过正则表达式查找所有的字符串
    # print(link)
    data.append(link)  # 添加链接

def get_img_link(find_img_link,item,data):
    # 获取图片链接
    img_link = re.findall(find_img_link, item)[0]
    data.append(img_link)  # 添加图片

def get_titles(find_title,item,data):
    titles = re.findall(find_title, item)
    if (len(titles) == 2):
        ctitle = titles[0]  # 添加中文名
        data.append(ctitle)
        otitle = titles[1].replace('/', '')  # 去掉无关的符号
        otitle = re.sub(r'(\xa0)*', "", otitle)
        data.append(otitle)  # 添加外文名
    else:
        data.append(titles[0])
        data.append('   ')  # 外文名留空

def get_rating(find_rating,item,data):
    rating = re.findall(find_rating,item)[0]
    data.append(rating)

def get_judge_number(find_judge_number,item,data):
    judge_number = re.findall(find_judge_number, item)[0]
    data.append(judge_number)  # 添加评价人数

def get_inq(find_inq,item,data):
    inq = re.findall(find_inq, item)
    if (len(inq) != 0):
        inq = inq[0].replace('。', '')  # 替换掉句号
        data.append(inq)  # 添加概述
    else:
        data.append('  ')  # 留空

def get_bd(find_bd,item,data):
    bd = re.findall(find_bd, item)[0]
    bd = re.sub(r'<br(\s+)?/>(\s+)?', "", bd)  # 去掉<br/>
    bd = re.sub(r'(\xa0)*', "", bd)
    bd = re.sub('/', '', bd)
    data.append(bd.strip())