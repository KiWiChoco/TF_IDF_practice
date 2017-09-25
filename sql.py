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

# sql_drop = "drop table if exists %s" % ("wiki_invert")
# sql = "create table %s (%s varchar(1000) not null, %s int(11) not null)" % ("wiki_invert", "term", "id")
# c.execute(sql_drop)
# c.execute(sql)

sql2 = "SELECT * FROM wiki"
c.execute(sql2)
wiki = c.fetchall()

wordlist = ['also', 'debut', 'language', 'two']
idlist = []
idxdict = {}

for w in wordlist:
    for line in wiki:
        txt_li = line[2].split()
        #print(txt_li)
        if w in txt_li:
            if line[0] not in idlist:
                idlist.append(line[0])
    idxdict[w] = idlist
    idlist = []

for w in wordlist:
    ids = idxdict[w]
    for id in ids:
        sql3 = "INSERT INTO wiki_invert VALUES ('%s',%d)"%(w,id)
        c.execute(sql3)
        connect.commit()

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
    #print(length)
    #print(count)
    return math.log(1+(count/length))

def idf(term):
    sql = "SELECT COUNT(DISTINCT id) FROM wiki_invert WHERE term = '{}'".format(term)
    c.execute(sql)
    nt = c.fetchone()[0]
    nt_int = int(nt)
    return 1/nt_int


def tf_idf(id,term):
    ti = tf(id, term) * idf(term)
    print("('{term}' in {id}) TF-IDF: {ti}".format(term=term, id=id, ti=ti))


tf_idf(41631770, 'also')
tf_idf(6688599, 'debut')
tf_idf(13794826, 'language')