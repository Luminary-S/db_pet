#!/usr/bin/venv python
# -*- coding: utf-8 -*-
'''
excle to sql database
'''
# refer : https://blog.csdn.net/qq_42708830/article/details/92762302
# and https://blog.csdn.net/weixin_41580638/article/details/86550318

import xlrd
import pymysql

# Open the workbook and define the worksheet
book = xlrd.open_workbook("./DB/animal-table.xlsx") # excel文件名
sheet = book.sheet_by_name("zjj") # excel文件中的sheet名

# 建立一个MySQL连接
database = pymysql.connect(host="localhost", port=3306, user="root", passwd="owen")

def create_DB(name):
    drop database RUNOOB;

# 获得游标对象, 用于逐行遍历数据库数据
cursor = database.cursor()

# 创建插入SQL语句
query = """INSERT INTO student (name,category,age,color,gender,price) VALUES (%s, %s,%s, %s,%s, %s)"""

# 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题
'''
excel中的格式：
|-      sno      -|- sname -|
|-    16301134   -|- 吴家行 -|
'''
for r in range(1, sheet.nrows):
    sno = sheet.cell(r, 0).value
    sname = sheet.cell(r, 1).value

    values = (name,category,age,color,gender,price)

    # 执行sql语句
    cursor.execute(query, values)

# 关闭游标
cursor.close()

# 提交
database.commit()

# 关闭数据库连接
database.close()

# 打印结果
print("")
print("Done! ")
print("")
columns = str(sheet.ncols)
rows = str(sheet.nrows)
print("我刚导入了 ", columns, " 列 and ", rows, " 行数据到MySQL!")
