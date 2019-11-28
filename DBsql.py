#!/usr/bin/venv python
# -*- coding: utf-8 -*-
'''
pymysql usage 
'''

# refer: https://www.cnblogs.com/xfxing/p/9322199.html
# and https://www.cnblogs.com/quanloveshui/p/11059568.html


import pymysql

class DBsql():

    def __init__(self, fname):
        self.init_db(fname)
        self.host='192.168.0.103',
        self.port=3306,
        self.user='root',
        self.password='123',
        self.database = fname,
        self.charset = 'utf8' 

    def init_db(self, fname):
        pass
    
    def build_conn(self):
        conn = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
            charset=self.charset
        )

        # get a cursor
        cursor = conn.cursor()
        return conn, cursor

    def del_val(self, val):
        # build connection
        conn, cursor = self.build_conn() 
        cursor = conn.cursor()
        # 定义将要执行的SQL语句
        sql = "delete from userinfo where user=%s;"
        name = "june"
        # 拼接并执行SQL语句
        cursor.execute(sql, [name])
        # 涉及写操作注意要提交
        conn.commit()
        # 关闭连接
        cursor.close()
        conn.close()

    def add_val(self, val):
        # build connection
        conn, cursor = self.build_conn()        
        
        # define the cmd
        sql = 'insert into userinfo(user,pwd) values(%s,%s);'
        data = [
            ('july', '147'),
            ('june', '258'),
            ('marin', '369')
        ]

        # joint cmd and implement cmd
        cursor.executemany(sql, data)
        # commit write
        conn.commit()
 
        # close connection
        cursor.close()
        conn.close()
        # pass

    def get_latest_val(self):
        # build connection
        conn, cursor = self.build_conn() 

        sql = "insert into userinfo (user, pwd) values (%s, %s);"
        name = "wuli"
        pwd = "123456789"
        # 并执行SQL语句
        cursor.execute(sql, [name, pwd])
        # 涉及写操作注意要提交
        conn.commit()
        # 关闭连接

        # 获取最新的那一条数据的ID
        last_id = cursor.lastrowid
        print("lastest data id:", last_id)

        cursor.close()
        conn.close()
        # return

    def read_to_dict(self):
        pass

    