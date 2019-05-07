def getPW():
	from cryptography.fernet import Fernet
	key = b'_xrTHhrdVCx825bWfeAWfjDLzhW7z1gox8auPI6SPvo='
	cipher_suite = Fernet(key)
	with open('.\emailPW.bin', 'rb') as file_object:
	    for line in file_object:
	        encryptedpwd = line
	uncipher_text = (cipher_suite.decrypt(encryptedpwd))
	plain_text_encryptedpassword = bytes(uncipher_text).decode("utf-8") #convert to string
	return plain_text_encryptedpassword