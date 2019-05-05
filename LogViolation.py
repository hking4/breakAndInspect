import os
import DatabaseConnection as dbc
import MySQLdb

db = dbc.connect()
cursor = db.cursor()

def log(user, url, path):
	sql_insert_query = "INSERT INTO VIOLATION (VIOL_USER_ID, VIOL_URL, VIOL_SSPATH) VALUES (%s, %s, %s)"
	val = (user, url, path)
	
	
	cursor.execute(sql_insert_query, val)
	db.commit()
