import cv2
import DatabaseConnection as dbc
import MySQLdb
import datetime
import getpass
import numpy as np
import os
import CNN_MODEL
from random import shuffle
from tqdm import tqdm

#DB Connection used for logging screenshots
db = dbc.connect()
cursor = db.cursor()

def run():
	d= datetime.datetime.today()
	IMAGE_DIR = '.\dataset\single_image_test'
	MODEL_NAME = 'socialmedia-4_27-0.001-6conv-basic-video.model'

	model = CNN_MODEL.getTfModel()

	if os.path.exists('{}.meta'.format(MODEL_NAME)):
	    model.load(MODEL_NAME)
	    print('model loaded!')

	def process_test_data():
	    testing_data = []
	    for img in tqdm(os.listdir(IMAGE_DIR)):
	        path = os.path.join(IMAGE_DIR, img)
	        img_num = img.split('.')[0]
	        img = cv2.resize(cv2.imread(path,cv2.IMREAD_GRAYSCALE), (CNN_MODEL.getImgSize(),CNN_MODEL.getImgSize()))
	        testing_data.append([np.array(img), img_num])
	    shuffle(testing_data)
	    np.save('single_test_data.npy', testing_data)
	    return testing_data

	test_data = process_test_data()

	with open('log-{}.csv'.format(d.strftime('%d_%m_%Y')), 'w') as f:
	    f.write('')

	with open('log-{}.csv'.format(d.strftime('%d_%m_%Y')), 'a') as f:
	    for data in tqdm(test_data):
	        img_num = data[1] #filename
	        img_data = data[0]

	        insertquery = 'INSERT INTO TEMP(SS_USER, SCREENSHOT_PATH, image_name, VIOLATION) VALUES (%s, %s, %s, %s)'

			##LOG ALL SCREENSHOTS TO TEMP

	        val = (os.environ['COMPUTERNAME'] + ':' + getpass.getuser(),'.\\dataset\\single_image_test\\' + img_num, img_num, '0')
	        cursor.execute(insertquery, val)
	        db.commit()

	        #COPY TO SCREENSHOTS IF NOT EXIST
	        insertquery = 'INSERT INTO SCREENSHOTS(SS_USER, SCREENSHOT_PATH, image_name, VIOLATION) SELECT SS_USER, SCREENSHOT_PATH, image_name, VIOLATION FROM TEMP WHERE TEMP.SCREENSHOT_PATH NOT IN (SELECT SCREENSHOT_PATH FROM SCREENSHOTS)'
	        cursor.execute(insertquery)
	        db.commit()

	        #CLEAR TEMP TABLE
	        deletequery = 'DELETE FROM TEMP'
	        cursor.execute(deletequery)
	        db.commit()

	        orig = img_data 
	        data = img_data.reshape(CNN_MODEL.getImgSize(),CNN_MODEL.getImgSize(),1)
	        model_out = model.predict([data])[0]
	        
	        f.write('{},{}\n'.format(img_num, model_out[1]))
