import sqlite3

# 1.连接数据库
# # conn = sqlite3.connect('test.db')   #打开或创建数据库文件
# #
# print("Open database successfully")

# 2.创建数据表
# conn = sqlite3.connect('test.db')   #打开或创建数据库文件
#
# print("成功打开数据库")
#
# c = conn.cursor()   #获取游标
#
# sql = '''
#     create table company
#         (id int primary key not null,
#         name text not null,
#         age int not null,
#         address char(50),
#         salary real);
# '''
#
# c.execute(sql)     #执行sql
# conn.commit()   #提交数据库操作
# conn.close()    #关闭数据库
#
# print("成功建表")

# 3.插入数据
# conn = sqlite3.connect('test.db')   #打开或创建数据库文件
#
# print("成功打开数据库")
#
# c = conn.cursor()   #获取游标
#
# sql_1 = '''
#     insert into company (id,name,age,address,salary)
#     values(1,"张三",32,"成都",8000)
# '''
# sql_2 = '''
#     insert into company (id,name,age,address,salary)
#     values(2,"李四",32,"成都",8000)
# '''
#
# c.execute(sql_1)     #执行sql
# c.execute(sql_2)
# conn.commit()   #提交数据库操作
# conn.close()    #关闭数据库
#
# print("插入数据完毕")

# 4.查询数据
conn = sqlite3.connect('test.db')   #打开或创建数据库文件

print("成功打开数据库")

c = conn.cursor()   #获取游标

sql_1 = '''
    select id, name, address,salary from company
'''

cusor_temp = c.execute(sql_1)     #执行sql

for row in cusor_temp:
    print("id = ",row[0])
    print("name = ",row[1])
    print("address = ",row[2])
    print("salary = ",row[3])

conn.close()    #关闭数据库

print("插入数据完毕")