#!/usr/bin/env python3
# -*- coding: utf-8 -*

import sqlite3

if __name__=='__main__':
    con = sqlite3.connect('tysql.sqlite')
    cursor = con.cursor()
    query = 'SELECT * FROM sqlite_master WHERE TYPE="table" AND NAME="{table_name}"'.format(table_name='Customers')
    for i in  cursor.execute(query):
        print(type(i))
        print(list(i))
        [print(a) for a in list(i)]