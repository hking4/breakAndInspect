import os
import csv
import MySQLdb
import EmailCreateSend
import DatabaseConnection as dbc
import LogViolation as l

def run():
    pathName = os.getcwd()
    index = []   #track image IDs 
    logFiles = []
    fileNames = os.listdir(pathName)
    ##Load all csv files in directory
    ##Script can scan multiple csv logs 
    for fileNames in fileNames:
        if fileNames.endswith(".csv"):
            logFiles.append(fileNames)
            
    ##Loop for each log file
    for i in logFiles:
        file = open(os.path.join(pathName, i), newline='')
        reader = csv.reader(file, delimiter=',')
        #print('\n'+i)   ##print log file name 
        
        for row in reader:
            content = list(row[i] for i in [0,1]) ##[0,1] are included columns from CNN csv logs

            print (content)
            if float(content[1]) < .5:
                #print('Violation')  
                index.append(content[0])

    db = dbc.connect()
    cursor = db.cursor()

    #query = "SELECT U.USER_ID, U.FNAME, U.LNAME, SS.SCREENSHOT_PATH FROM USERS U LEFT JOIN SCREENSHOTS SS ON U.USER_ID = SS.SS_USER WHERE SS.SS_ID IN (%s)" % ",".join(map(str,index))
    selectquery = "SELECT S.SS_USER, S.SCREENSHOT_PATH FROM SCREENSHOTS S WHERE S.image_name IN (%s)" % ",".join(map(str,index))
    cursor.execute(selectquery)
    results = cursor.fetchall()

    message = ''
    #EmailCreateSend.send(results)
    for row in results:
        user = row[0]
        path = row[1]
        message += 'PC/USER- ' + user + ', Image Path - ' + path + '\n'
        ##LOG TO VIOLATION TABLE
        l.log(user, path)
    #print(message)
    EmailCreateSend.send(message)