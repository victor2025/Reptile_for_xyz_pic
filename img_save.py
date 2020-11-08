# -*- coding: utf-8 -*-
# @Time    : 2020/10/30 17:39
# @Author  : VICTOR2022
# @File    : img_save.py
# @Software: PyCharm

from urllib.request import urlretrieve
import os

def img_save(data_list):
    file_path = r'ImgSave'
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    for ind_img in range(0, len(data_list)):
        temp_title = data_list[ind_img][2]
        if type(temp_title) == list:
            temp_title = temp_title[0]
        temp_link = data_list[ind_img][1]
        img_name = file_path+"\\"+str(ind_img+1)+'_'+temp_title+'.jpg'
        urlretrieve(temp_link,img_name)
        print('储存第%d张海报'%(ind_img+1))
