# coding=utf-8

"""
mysql + ubuntu
1. install mysql --> sudo apt-get install mysql-server
2. in terminal --> mysql -u root -p
3. create database contacts;
4. use contacts;
5. create table person(str varchar(20));
"""

import pymysql


def connect():
    print("connect to database")
    pw = input("Password: ")
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd=pw, db='contacts')
    conn.autocommit(True)
    cur_ = conn.cursor()
    return cur_


def show_tables(self):
    print("show tables: ")
    self.execute("""SHOW TABLES""")
    # print(self.fetchall())
    return self.fetchall()


def show_column_names(self):
    print("show column names: ")
    self.execute("""SHOW COLUMNS FROM person""")
    print(self.fetchall())


def show_all(self, table_name_):
    print("show all: ")
    self.execute("""SELECT * FROM """ + str(table_name_))
    for x in self.fetchall():
        print(x)


def show_first_line(self, table_name_):
    print("show first line: ")
    self.execute("""SELECT * FROM """ + str(table_name_) + """ LIMIT 1""")
    for x in self.fetchall():
        print(x)


def change_value(self):
    print("change a value")
    self.execute("""UPDATE person SET first_name = 'Mike' WHERE first_name = '1'""")


def add_value(self):
    print("add a value")
    self.execute("""INSERT INTO person VALUES ('Karl', 'Meier', '2013-08-30', 'M', 'New York')""")


db = connect()
table_names = show_tables(db)  # returns a tuple
print(len(table_names))  # output zero
show_column_names(db)
table_name = table_names[0][0]  # ? - todo - get item from tuple
print(table_name)
show_all(db, table_name)
# add_value(db)
# change_value(db)
