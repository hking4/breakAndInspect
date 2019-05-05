import MySQLdb
host = 'remotemysql.com'
user='5i48ibmWpC'
passwd='Wk4CcxeIyW'
schema='5i48ibmWpC'

db = MySQLdb.connect(host, user, passwd, schema)

def connect():
	return db