# -*- coding: utf-8 -*-
# @Time    : 2020/10/30 17:39
# @Author  : VICTOR2022
# @File    : img_save.py
# @Software: PyCharm

from urllib.request import urlretrieve
import os
import socket

def img_save(data_list,info_main):
    # 存档还原
    page_now = info_main.page_ind
    detail_begin = info_main.detail_ind
    img_begin = info_main.img_ind
    # 开始保存
    file_path = r'.ImgSave/xyz_pic_2/page_%d'%page_now  
    for ind_detail in range(detail_begin, len(data_list)):
        detail = data_list[ind_detail]
        temp_title = detail[0]
        temp_path = file_path + '/' + str(ind_detail+1) + '_' + temp_title
        make_dir(temp_path)
        for ind_img in range(img_begin+1, len(detail)):
        #if type(temp_title) == list:
         #   temp_title = temp_title[0]
	        temp_link = detail[ind_img]
	        img_name = temp_path+"/" + str(ind_img) +temp_link[-4:]
	        print('保存%d的第%d/%d张海报，总进度%d/%d'%(ind_detail+1, ind_img, len(detail)-1, ind_detail+1,len(data_list)))
	        now_info = [page_now, ind_detail, ind_img]
	        down_from_url(temp_link,img_name, 45, 1, now_info, info_main)
	        #储存当前程序进行位置
	        pos_now = {'detail':ind_detail,'img':ind_img}
	        info_main.save_last_ind(pos_now)
        img_begin = 0
    detail_begin = 0
        
def img_save_2(pic_list,info_main):
    # 存档还原
    page_now = info_main.page_ind
    ind_detail = info_main.detail_ind
    img_begin = info_main.img_ind
    # 开始保存
    file_path = r'.ImgSave/xyz_pic_2/page_%d'%page_now  
    #for ind_detail in range(detail_begin, len(pic_list)):
    detail = pic_list
    temp_title = detail[0]
    temp_path = file_path + '/' + str(ind_detail+1) + '_' + temp_title
    make_dir(temp_path)
    for ind_img in range(img_begin+1, len(detail)):
    #if type(temp_title) == list:
     #   temp_title = temp_title[0]
	    temp_link = detail[ind_img]
	    img_name = temp_path+"/" + str(ind_img) +temp_link[-4:]
	    print('保存%d的第%d/%d张海报，总进度%d/%d'%(ind_detail+1, ind_img, len(detail)-1, ind_detail+1,len(pic_list)))
	    now_info = [page_now, ind_detail, ind_img]
	    down_from_url(temp_link,img_name, 45, 1, now_info, info_main)
	        #储存当前程序进行位置
	    pos_now = {'detail':ind_detail,'img':ind_img}
	    info_main.save_last_ind(pos_now)
    img_begin = 0
detail_begin = 0

def make_dir(path):
	if not os.path.exists(path):
		os.makedirs(path)
		
def down_from_url(url, img_name, retry_time, retry_count, now_info, info_main):
	socket.setdefaulttimeout(retry_time)
	flag = False
	while retry_count<=5:
		try:
			try:
				urlretrieve(url , img_name)
				break
			except Exception as e:
				flag = True
				print(e)
				break
		except socket.timeout:
			error_info = '时间已过%d秒，即将进行第%d次重试......'%(retry_time, retry_count)
			print(error_info)
			retry_count += 1
			retry_time -= 5
			down_from_url(url, img_name, retry_time, retry_count, now_info, info_main)
		if retry_count > 5 or flag:
			info_main.save_fail_ind(now_info)
			print("保存失败，自动跳过，失败位置已储存")