from bs4 import BeautifulSoup as bs     #网页解析，获取数据
import urllib.request,urllib.error  #制定url,获取网络数据
import get_functions
import gzip
import img_save

def major_data_get(base_url,re_setting, info_main):
    # New Project
    data_list=[]
    base_url = base_url + '/pic/2'
    base_url_page = base_url + '/index_' + str(info_main.page_ind) +'.html'
    #html_main_site = ask_URL(base_url)	#获取主站HTML
	#save_html(html_main_site, 'html_pic_2.html')
    #逐一解析数据
    soup_main_site = soup_link(base_url_page)
    item_type = soup_main_site.find_all('div',class_='box list channel')[0]
    for item in item_type.find_all('li'):
	    #print(item)
	    data = []
	    item = str(item)
	    data = get_functions.get_pic_site(item,re_setting)
	    data[0] = base_url+data[0]
	    #data.insert(0,type_title)
	    print(data)
	    #temp_data_list.append(data)
	    data_list.append(data)
    #print(data_list)	
    return data_list
    
def major_detail_get(data_list, re_setting, info_main):
	pic_list = []
	detail_site_begin = info_main.detail_ind
	for detail_ind in range(detail_site_begin,len(data_list)):
		detail_site = data_list[detail_ind]
		temp_link = detail_site[0]
		temp_title = detail_site[1]
		soup_detail = soup_link(temp_link)
		item_pic = soup_detail.find_all('div', class_='content')
		item_pic = str(item_pic).strip()
		temp_data = get_functions.get_pic_detail(item_pic, re_setting)
		temp_data.insert(0,temp_title)
		print(temp_data)
		# 保存此次文件
		img_save.img_save_2(temp_data, info_main)
		#储存程序状态
		info_main.save_last_ind({'detail':detail_ind})
		
		pic_list.append(temp_data)
	return  pic_list

def soup_link(link):
	temp_html = ask_URL(link)
	save_html(temp_html,'temp_html.html')
	soup = bs(temp_html,"html.parser")
	return soup
	
# 得到指定url中的内容
def ask_URL(url):
    head = head_def()
    page_pre = urllib.request.Request(url, headers=head)
    html = ""
    try:
        page = urllib.request.urlopen(page_pre)
        html = ungzip(page.read())
        html = html.decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html

def ungzip(data):
    try:
        data = gzip.decompress(data)
    except:
        pass
    return data

def head_def():
    #Cookie = "HstCfa4075068=1604828676140; HstCmu4075068=1604828676140; HstCnv4075068=1; c_ref_4075068=https%3A%2F%2F2121mz.com%2F; HstCns4075068=2; __dtsu=6D001604829374D19D498B2B8850E0EE; HstCla4075068=1604829383173; HstPn4075068=4; HstPt4075068=4"
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        #"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        #"Cookie": Cookie
    }   #用户代理表示告诉服务器，我们是什么类型的设备/浏览器
    return head

def save_html(html, file_name):
    with open(file_name, 'w', encoding='utf-8') as obj:
        obj.write(html)
        obj.close()