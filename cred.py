#Dependencies
import os
from firebase_admin import credentials

#Constant and path defines
file_id            = "iotserver_key.json"
info_id            = "info.txt"
project_id         = "D:\\IMPORTANT\\firebase_iot\\Prototype\\Server"
private_key        = os.path.join(project_id,file_id)
info_key           = os.path.join(project_id,info_id)


def get_cred():
	return credentials.Certificate(private_key)

def get_options():
	with open(info_key, mode='r') as f:
	    options = {}
	    for i in f.readlines():
	        data=i.strip("\n").split(" ")
	        options[ data[0] ] = data[1]
	return options

