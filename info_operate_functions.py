import json
import os
# 用于储存和读取数据

class InfoOperate():
	def __init__():
		init_json()
		self.fail_ind = get_fail_ind()
		self.last_ind = get_last_ind()
		self.last_page_ind = last_ind['page']
		self.last_detail_ind = last_ind['detail']
		self.last_img_ind = last_ind['img']
		
	def init_json():
		file_name = 'info_save.json'
		if not os.path.exists(file_name):
			fail_ind = {}
			last_ind = {}
			with open(file_name,'w') as obj:
				json.dump(fail_ind,obj)
				json.dump(last_ind,obj)
			
	def get_fail_ind():
		info_save = data_load()
		return info_save['fail_ind']
		
	def get_last_ind():
		info_save = data_load()
		return info_save['last_ind']
				
	def data_load():
		with open("info_save.json") as obj:
			info_save = json.load(obj)
		return info_save
		
	def save_last_ind(para):
		with open('info_save.json', 'w') as obj
			 info_save = json.load(obj)
			 last_ind = info_save['last_ind']
			 for key,value in para.item():
			 	last_ind[key] = value
			 json.dump(last_ind, obj)
			 obj.close()
	
	def save_fail_ind(now_info):
	ind_page = str(now_info[0])
	ind_detail = str(now_info[1])
	ind_img = now_info[2]
	with open('info_save.json','w') as obj:
		info_save = json.load(obj)
		fail_ind = info_save['fail_ind']	#需要初始化json，加入各变量
		try:
			#提取数据
			ind_detail_info = fail_ind[ind_page]
			ind_img_info = ind_detail_info[ind_detail]
			ind_img_info.append(ind_img).set()
			#保存数据
			ind_detail_info[ind_detail] = ind_img_info
			fail_ind[ind_page] = ind_detail_info
		except Exception as e:
			print(e)
			ind_img_info = [ind_img]
			ind_detail_info[ind_detail] = ind_img_info
			fail_ind[ind_page] = ind_detail_info
			print("已为成功错误文件存档！")
		json.dump(fail_ind, obj)
		obj.close()		