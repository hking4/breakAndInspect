import MySQLdb
import PWdecr as pw
#import DBPassDec
host = 'remotemysql.com'
user='5i48ibmWpC'
#passwd= DBPassDec.getPW()
passwd = pw.getPW('.\mySQLPW.bin')
schema='5i48ibmWpC'

db = MySQLdb.connect(host, user, passwd, schema)

def connect():
	return db