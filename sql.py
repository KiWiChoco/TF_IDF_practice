import MySQLdb
import codecs
import re
import sys
import math

db_host = "147.46.15.66"
db_user = "qmopla"
db_pw = "bde1234"
db_name = "qmopla"
connect = MySQLdb.connect(db_host, db_user, db_pw, db_name)
connect.set_character_set('utf8')
connect.autocommit = True
c = connect.cursor()


def tf(id,term):

    sql = "select text from wiki where id = %d"%id
    c.execute(sql)
    txt = c.fetchone()
    list = txt[0].split(" ")
    length = len(list)
    count = 0
    for txt in list:
        if txt.lower() == term:
            count += 1
    print(length)
    print(count)
    return math.log(1+(count/length))

def idf(term):
    sql_drop = "drop table if exists %s"%("wiki_invert")
    sql = "create table %s (%s varchar(1000) not null, %s int(11) not null)"%("wiki_invert","term","id")
    c.execute(sql_drop)
    c.execute(sql)

    

        # for i in range(len(id_tf)):
        #     arrange_txt = list(txt_tf[i])
        #     #print(arrange_txt)
        #     string_txt = arrange_txt[0].split(" ")
        #     for i in string_txt:


# tf(41631770,"also")
# tf(6688599,"debut")
# tf(13794826,"language")

idf('k')