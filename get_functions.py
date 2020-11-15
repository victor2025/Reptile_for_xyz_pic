import re

def get_pic_site(item,re_setting):
    data = []
    #数据获取
    detail = get_detail(item,re_setting.find_detail)
    title = get_titles(item, re_setting.find_title)
    date = get_date(item, re_setting.find_date)
    #储存数据
    data = [detail, title, date]
    return data
    
def get_pic_detail(item,re_setting):
	data = get_img_link(item, re_setting.find_img_link)
	return data
	

def get_type_title(item,re_setting):
	type_title = re.findall(re_setting.find_type_title, item)[0]
	return type_title

def get_detail(item, find_detail):
    # 获取到影片详情的链接
    detail_link = re.findall(find_detail, item)[0]  # 使用re库通过正则表达式查找所有的字符串
    #print(detail_link)
    return detail_link
    
def get_img_link(item,find_img_link):
    # 获取图片链接
    img_link = re.findall(find_img_link, item)
    #print(img_link)
    return img_link

def get_titles(item, find_title):
    title = re.findall(find_title, item)[0]
    #print(titles)
    return title
    
    #if (len(titles) == 2):
#        ctitle = titles[0]  # 添加中文名
#        data.append(ctitle)
#        otitle = titles[1].replace('/', '')  # 去掉无关的符号
#        otitle = re.sub(r'(\xa0)*', "", otitle)
#        data.append(otitle)  # 添加外文名
#    else:
#        data.append(titles[0])
#        data.append('   ')  # 外文名留空

def get_date(item,find_date):
	date = re.findall(find_date,item)[0]
	#print(dates)
	return date

#def get_bd(find_bd,item,data):
#    bd = re.findall(find_bd, item)[0]
#    bd = re.sub(r'<br(\s+)?/>(\s+)?', "", bd)  # 去掉<br/>
#    bd = re.sub(r'(\xa0)*', "", bd)
#    bd = re.sub('/', '', bd)
#    data.append(bd.strip())