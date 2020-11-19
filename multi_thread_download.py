#pylint:disable=E0602
#pylint:disable=E0401
import os, sys
from urllib.request import *
import requests
from threading import Thread

def download_mt(url_present, save_path_present, thread_num_present):
	global finished_num
	url = url_present
	save_path = save_path_present
	thread_num = thread_num_present		  #开启线程数目
	cache_size = 4096 	#缓存区大小
	thread_pool = []
	#file_cache = {}
	
	#req = urlopen(Request(url))
#	file_size = int(req.headers['content-length'])
	file_size = int(requests.head(url).headers['Content-Length'])
	thread_size = file_size // thread_num	#每个线程下载的大小
	finished_num = 0
	print('开始下载...')
	
	
	def download_main(start_pos, end_pos, _id):
		#start_pos = para[0]
		#end_pos = para[1]
		#_id = para[2]
		if _id == thread_num - 1:
			#若是最后一个线程，则下载完全部
			end_pos = file_size
			
		download_size = end_pos - start_pos #总下载大小
		download_num = download_size//cache_size #需要下载的次数
		end_download_size = download_size%cache_size	#若总大小不能被缓存大小整除，则最后一次下载文件大小为余数
		# 请求访问文件
		#req_file = Request(url, headers = {'range':'bytes=%s-%s'%(start_pos, end_pos)})
		#req_file = urlopen(req_file)
		req_file = requests.get(url, headers = {'range':'bytes=%s-%s'%(start_pos, end_pos)})
		#print('[Thread-%s] 开始下载.下载范围:%s-%s. '%(_id, start_pos, end_pos))
		with open(save_path, 'r+b') as obj:
			obj.seek(start_pos)
			obj.write(req_file.content)
			#n = 0
#			while download_num > n:
#				sf.write(req_file.read(cache_size))
#				n += 1
#			if not end_download_size ==0:
#				sf.write(req_file.read(end_download_size))
		#file_cache[str(_id)] = req_file
		global finished_num
		finished_num+=1
		#print(finished_num)
		print('下载进度:['+'#'*finished_num+' '*(thread_num-finished_num)+']')
	
	file_pre = open(save_path,'wb')
	file_pre.truncate(file_size)
	file_pre.close()
	
	for ind_thread in range(thread_num):	#开启线程
		#para = [1*thread_size, (ind_thread+1)*thread_size, ind_thread]
		x = Thread(target = download_main, args = (ind_thread*thread_size, (ind_thread+1)*thread_size, ind_thread))
		x.start()
		thread_pool.append(x)
		
	#while True:
#		if len(file_cache)==thread_num:
#			with open(save_path, 'ab+') as obj:
#				for save_ind in range(thread_num):
#					obj.write(file_cache[str(save_ind)].content)
#				obj.close()
#			break