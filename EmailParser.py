import os
import csv
import MySQLdb
import EmailCreateSend
import DatabaseConnection as dbc
import LogViolation as l
import getpass

def run():
    pathName = os.getcwd()
    index = []   #track image IDs 
    logFiles = []
    fileNames = os.listdir(pathName)
    terminal = os.environ['COMPUTERNAME']
    user = getpass.getuser()

    db = dbc.connect()
    cursor = db.cursor()

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
                ##update violation column on screenshots table
                updatequery = "UPDATE SCREENSHOTS SET VIOLATION = 1 where image_name = " + content[0] ##track violation pics to avoid duplicate rows in violation table
                cursor.execute(updatequery)

    selectquery = "SELECT DISTINCT S.SCREENSHOT_PATH, S.SS_USER FROM SCREENSHOTS S WHERE S.image_name IN (%s)" % ",".join(map(str,index))
    cursor.execute(selectquery)
    results = cursor.fetchall()

    #message = ''
    message2 = ''
    filepath = '\\\\' + terminal + '\\Users\\' + user + '\\Downloads\\'
    #EmailCreateSend.send(results)
    for row in results:
        #path = row[0]
        #user = row[1]
        #message += 'PC/USER- ' + user + ', Image Path - ' + path + '\n'
        ##LOG TO VIOLATION TABLE
        l.log()

    selectquery = 'SELECT COUNT(VIOLATION_ID) FROM VIOLATION WHERE REVIEWED = 0'
    cursor.execute(selectquery)
    results = cursor.fetchall()
    message2 += str(results[0][0]) + ' new violations detected since last review for USER: ' + user + ' on PC: ' + terminal + '\n Images can be found at: ' + filepath
    try:
        ## SEND EMAIL, THEN MARK VIOLATIONS AS REVIEWED 
        updatequery = 'UPDATE VIOLATION SET REVIEWED = 1'
        EmailCreateSend.send(message2)
        cursor.execute(updatequery)
        db.commit()
        
    except:
        print('Exception')