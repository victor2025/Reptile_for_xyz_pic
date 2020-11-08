import xlwt

work_book = xlwt.Workbook(encoding="utf-8") #创建WorkBook对象
work_sheet = work_book.add_sheet("sheet_1") #创建sheet1
# work_sheet.write(0,0,'hello')   #第一个参数为行，第二个参数为列，第三个参数为内容
work_book.save('test_xlwt.xls')

# 存储乘法表练习
for i in range(1,10):
    for j in range(1,i+1):
        ij=i*j
        string = str(i)+"*"+str(j)+"="+str(ij)
        work_sheet.write(i-1,j-1,string)
        print(string,end='')
    print('\n')

work_book.save('test_xlwt.xls')