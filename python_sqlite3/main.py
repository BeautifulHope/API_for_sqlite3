#!/usr/bin/env python3
# -*- coding: utf-8 -*

import sqlite3
import re

if __name__=='__main__':
    # con = sqlite3.connect('tysql.sqlite')
    con = sqlite3.connect('Test.db')
    cursor = con.cursor()

    ####查询是否存在同名的表，否无则新建table
    target_table = 'PYTHONCONTROL'
    table_name = []
    query = 'SELECT * FROM sqlite_master WHERE TYPE="table"'
    for tables in cursor.execute(query):
        table_name .append([line for line in tables][1])

    if target_table in table_name:
        print("table exist!")
    else:
        query = 'CREATE TABLE {table_name} (' \
                'ID INT PRIMARY KEY NOT NULL,' \
                'NAME CHAR(50) NOT NULL,' \
                'AGE INT' \
                ')'.format(table_name=target_table)
        cursor.execute(query)
        print("table create!")

    ####获取db中table的name
    print('----------------------')
    n = 1
    query = 'SELECT * FROM sqlite_master WHERE TYPE="table"'
    for tables in cursor.execute(query):
        table_name=[line for line in tables][1]
        print(n," : ",table_name)
        n = n+1

    #### 打印表结构
    print('----------------------')

    table_struct = ''
    target_table = 'COMPANY'
    query = 'SELECT * FROM sqlite_master WHERE TYPE="table" AND NAME="{table_name}"'.format(table_name=target_table)
    for i in  cursor.execute(query):
        print(type(i))
        print('list(i):',list(i))
        [print(a,';',type(a)) for a in list(i)]
        table_struct = i[-1]

    ####提取item 名称
    print('table_struct:',table_struct)
    item_names = []
    print((table_struct.split('(',1)[-1]+')').split('))')[0])
    for i in ((table_struct.split('(', 1)[-1] + ')').split('))')[0].split(',')):
        item_names.append(i.split(' ',1)[0].strip())
    print(item_names)


    #### 查询数据
    print('----------------------')
    target_table = 'COMPANY'
    query = 'SELECT * FROM {table_name}'.format(table_name=target_table)
    for i in  cursor.execute(query):
        print(i)

    ####插入数据
    print('----------------------')
    target_table = 'COMPANY'
    query = 'INSERT INTO {table_name} VALUES ({ID}, \'{NAME}\', {AGE}, \'{ADDRESS}\', {SALARY})'\
        .format(table_name=target_table,ID='13',NAME='python',AGE='24',ADDRESS='NANSHAN',SALARY='6000')
    cursor.execute(query)

    query = 'INSERT INTO {table_name} VALUES ({ID}, \'{NAME}\', {AGE}, \'{ADDRESS}\', {SALARY})'\
        .format(table_name=target_table,ID='19',NAME='python',AGE='24',ADDRESS=None,SALARY='0')
    # print(query)
    cursor.execute(query)

    query = 'SELECT * FROM {table_name}'.format(table_name=target_table)
    for i in  cursor.execute(query):
        print(i)

    ####修改数据
    print('----------------------')
    target_table = 'COMPANY'
    query = 'UPDATE {table_name} SET ADDRESS = \'{NAME}\', SALARY ={SALARY} WHERE ID = {ID}'\
        .format(table_name=target_table,ID='13',NAME='python_update',SALARY='2333')
    cursor.execute(query)

    ####删除数据
    print('----------------------')
    target_table = 'COMPANY'
    query = 'DELETE FROM {table_name} WHERE ID = {ID}' \
        .format(table_name=target_table, ID='13', NAME='python_update', SALARY='2333')
    cursor.execute(query)

    query = 'SELECT * FROM {table_name}'.format(table_name=target_table)
    for i in  cursor.execute(query):
        print(i)

    print('----------------------')
    query = 'DELETE FROM {table_name} WHERE NAME = \'{NAME}\'' \
        .format(table_name=target_table, ID='13', NAME='python', SALARY='2333')
    cursor.execute(query)

    query = 'SELECT * FROM {table_name}'.format(table_name=target_table)
    for i in  cursor.execute(query):
        print(i)