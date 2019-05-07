import os
import DatabaseConnection as dbc
import MySQLdb

db = dbc.connect()
cursor = db.cursor()

def log(user, path):
	sql_insert_query = "INSERT INTO VIOLATION (VIOL_SSPATH, VIOL_USER) VALUES (%s, %s)"
	val = (path, user)
	
	
	cursor.execute(sql_insert_query, val)
	db.commit()
