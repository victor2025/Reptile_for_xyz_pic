# coding=utf-8

#import sys
#from bs4 import BeautifulSoup as bs     #网页解析，获取数据
#import re               #正则表达式，进行文字匹配
#import urllib.request,urllib.error  #制定url,获取网络数据
import xlwt             #进行excel操作
import sqlite3          #进行SQLite数据库操作
from re_Setting import ReSetting
#import get_functions
import major_functions
# import img_save
import info_operate


def main():
	info_main = info_operate.InfoOperate()
	base_url="https://www.905xyz.xyz"
	re_setting = ReSetting()
    #1.爬取网页
	page = info_main.page_ind
	while True:
		data_list = getData(base_url,re_setting,info_main)
		page=page+1
		last_ind = {'page':page,'detail':0,'img':0}
		info_main.save_last_ind(last_ind)
		save_path = r"Result_xyz_pic_%d.xls"%page
    # db_path = "movie.db"
    #3.保存数据
		saveData(data_list,save_path)
    #saveData_DB(data_list,db_path)

#爬取网页,逐一解析数据
def getData(base_url,re_setting,info_main):
    data_list_pic_site = major_functions.major_data_get(base_url,re_setting,info_main) # 获取网页数据
    #print(data_list_pic_site)
    data_list_detail_site = major_functions.major_detail_get(data_list_pic_site ,re_setting, info_main)
    #print(data_list_detail_site)
    print('完成第%d页链接的爬取'%info_main.page_ind)
    #img_save.img_save(data_list_detail_site,info_main)
    return data_list_detail_site

#保存数据
def saveData(data_list,save_path):
    print("开始储存爬取数据~~~")
    work_book = xlwt.Workbook(encoding="utf-8",style_compression=0)
    work_sheet = work_book.add_sheet("Result_xyz",cell_overwrite_ok=True)
    #col = tuple(data_list.keys())
    	
    col = ('Title','Img_link')
    for ind_col in range(0,len(col)):
        work_sheet.write(0,ind_col,col[ind_col])
    for ind_item in range(0,len(data_list)):
        print("第%d条"%(ind_item+1))
        temp_item = data_list[ind_item]
        for ind_x in range(0,len(temp_item)):
            work_sheet.write(ind_item+1,ind_x,temp_item[ind_x])
    work_book.save(save_path)       #储存数据
    #img_save.img_save(data_list)    #存储海报图片

def saveData_DB(data_list,db_path):
    init_DB(db_path)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    for data in data_list:
        for ind in range(len(data)):
            data[ind] = '"'+data[ind]+'"' # data里面的数字以列表形式出现，无法串联
        sql = '''
            insert into movie250(
            info_link,pic_link,cname,ename,score,rated,introduction,info)
            values(%s)'''%",".join(data)
        print(sql)
        cur.execute(sql)
        conn.commit()

    cur.close()
    conn.close()



def init_DB(db_path):  #初始化数据库
    sql = '''
        create table movie250 (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric ,
        rated numeric ,
        introduction text,
        info text
        )
    '''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try :
        cursor.execute(sql)
    except sqlite3.OperationalError:
        pass
    conn.commit()
    conn.close()




if __name__ == "__main__":      #当程序执行时
    # 调用函数
    main()
    print('爬取完毕!')