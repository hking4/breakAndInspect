import MySQLdb
import DBPassDec
host = 'remotemysql.com'
user='5i48ibmWpC'
passwd= DBPassDec.getPW()
schema='5i48ibmWpC'

db = MySQLdb.connect(host, user, passwd, schema)

def connect():
	return db