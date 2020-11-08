from bs4 import BeautifulSoup as bs     #网页解析，获取数据
import urllib.request,urllib.error  #制定url,获取网络数据
import get_functions

def major_data_get(base_url,re_setting):
    data_list=[]
    for i in range(0, 10):  # 调用获取页面信息的函数，10次
        url = base_url + "?start=" + str(i * 25)
        html = ask_URL(url)  # 保存获取到的网页资源
        # 逐一解析数据
        soup = bs(html, "html.parser")
        for item in soup.find_all("div", class_="item"):
            # print(item) #测试，用来查看电影item所有信息
            # data = []   #保存一部电影的所有信息
            item = str(item)
            data = get_functions.get_all(re_setting, item)
            data_list.append(data)

    return data_list

# 得到指定url中的内容
def ask_URL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }   #用户代理表示告诉服务器，我们是什么类型的设备/浏览器
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html