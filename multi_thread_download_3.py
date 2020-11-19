#pylint:disable=E0602
#pylint:disable=E0401
import os, sys
from urllib.request import *
import requests
from threading import Thread,enumerate

def download_mt(url_present, save_path_present, thread_num_max, title):
	global finished_num, finished_size,live_thread_num
	live_thread_num = 0
	
	url = url_present
	save_path = save_path_present
	cache_size = 1024*8	#缓存区大小
	thread_pool = []
	
	req = urlopen(Request(url))
	file_size = int(req.headers['content-length'])
	thread_num = file_size // cache_size	#每个线程下载的大小
	#part_size = file_size // part_num
	#thread_size = part_size // thread_num
	finished_num = 0
	finished_size = 0
	print('开始下载...')
	#print('下载进度:',end='')
	#show_process(finished_size, file_size, title)
	
	def download_main(start_pos, end_pos,  _id, file_size):
		if _id == thread_num - 1:
			#若是最后一个线程，则下载完全部
			end_pos = file_size
			
		download_size = end_pos - start_pos #总下载大小
		# 请求访问文件
		try:
			req_file = requests.get(url, headers = {'range':'bytes=%s-%s'%(start_pos, end_pos)})
			#存储文件
			with open(save_path, 'r+b') as obj:
				obj.seek(start_pos)
				obj.write(req_file.content)
		except Exception as e:
			print("Thread-%d error"%_id)
		#记录下载进度
		global finished_num,finished_size
		finished_num+=1
		finished_size += download_size 
		print('当前%s已完成：%.2f'%(title,finished_size/file_size*100)+'%')
		#show_process(finished_size,file_size,title)
		
	#初始化文件
	file_pre = open(save_path,'wb')
	file_pre.truncate(file_size)
	file_pre.close()
	#开启线程
	for ind_thread in range(thread_num):
		#show_process(finished_size, file_size, title)
		x = Thread(target = download_main, args = (ind_thread*cache_size, (ind_thread+1)*cache_size, ind_thread, file_size))
		x.start()
		thread_pool.append(x)
		#print('%s_Thread_%d'%(title,ind_thread))
		#live_thread_num = len(enumerate())
		#while live_thread_num-finished_num>thread_num_max:
			#show_process(finished_size, file_size, title)
			#print(live_thread_num)
	
		
def show_process(finished_size, file_size,title):
		#def show(file_size):
			#while True:
				global live_thread_num
				#print(live_thread_num)
				process_now = finished_size/file_size*100
				#os.system('clear')
				#print(finished_size)
				print('当前%s已完成：%.2f/%.2f'%(title,finished_size/1024/1024,file_size/1024/1024))
				#print(finished_num)
		#show = Thread(target = show, args = (file_size))