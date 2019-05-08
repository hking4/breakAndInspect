import os
import DatabaseConnection as dbc
import MySQLdb

db = dbc.connect()
cursor = db.cursor()

def log():
	
	##Keeps any duplicates from being logged to the violation table. 
	#Checks for a) image being flagged as a violation
	#			b) file path doesn't already exist
	sql_insert_query = "INSERT INTO VIOLATION(VIOL_SSPATH, VIOL_USER) SELECT SCREENSHOT_PATH, SS_USER FROM SCREENSHOTS	WHERE VIOLATION = 1 AND SCREENSHOTS.SCREENSHOT_PATH NOT IN (SELECT VIOL_SSPATH FROM VIOLATION)"
	
	cursor.execute(sql_insert_query)
	db.commit()
