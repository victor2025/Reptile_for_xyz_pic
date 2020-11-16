import json
import os
# 用于储存和读取程序状态

class InfoOperate():
	def __init__(self):
		self.init_json()
				
	def init_json(self):
		file_name = 'info_save.json'
		if not os.path.exists(file_name):
			main_ind = {'fail_ind' :{},'last_ind' : {}}
			with open(file_name,'w') as obj:
				json.dump(main_ind,obj)
				self.page_ind = 2
				self.detail_ind = 0
				self.img_ind = 0
				obj.close()
			self.save_last_ind()
		else:
			self.fail_ind = self.get_fail_ind()
			self.last_ind = self.get_last_ind()
			self.get_every_ind()
				
	def get_every_ind(self):
		self.page_ind = self.last_ind['page']
		self.detail_ind = self.last_ind['detail']
		self.img_ind = self.last_ind['img']
			
	def get_fail_ind(self):
		info_save = self.data_load()
		return info_save['fail_ind']
		
	def get_last_ind(self):
		info_save = self.data_load()
		return info_save['last_ind']
				
	def data_load(self):
		with open("info_save.json") as obj:
			info_save = json.load(obj)
		return info_save
	
	def save_last_ind(self):
		with open('info_save.json','r') as obj_r:
			info_save = json.load(obj_r)
			last_ind = info_save['last_ind']
			obj_r.close()
		last_ind = {}
		with open('info_save.json', 'w') as obj:
			 last_ind['page'] = self.page_ind
			 last_ind['detail'] = self.detail_ind
			 last_ind['img'] = self.img_ind
			 info_save['last_ind'] = last_ind
			 json.dump(info_save, obj)
			 obj.close()
		#self.get_every_ind()
	
	def save_fail_ind(self, now_info):
		ind_page = str(now_info[0])
		ind_detail = str(now_info[1])
		ind_img = now_info[2]
		with open('info_save.json', 'r') as obj_r:
			info_save = json.load(obj_r)
			fail_ind = info_save['fail_ind']	#需要初始化json，加入各变量
			obj_r.close()
		with open('info_save.json','w') as obj:
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
				print("已成功为错误文件存档！")
			self.fail_ind = fail_ind
			info_save['fail_ind'] = fail_ind
			json.dump(info_save, obj)
			obj.close()		