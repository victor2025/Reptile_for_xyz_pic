import re

class ReSetting():
    def __init__(self):
        #New Project
        self.find_detail = re.compile(r'<li><a href="/pic/2(.*.html)"')
        self.find_date = re.compile(r'<span>(.*)</span>')
        self.find_title  = re.compile(r'</span>(.*?)</a>')
        self.find_img_link = re.compile(r'src="(.*?.jpg)"',re.S)
        
        #self.find_type_title=re.compile(r'<b>(.*)</b>')
        
        