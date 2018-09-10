#Dependencies
from os.path import join, exists
from firebase_admin import db
import firebase_admin as firebase


from Server.cred import *

import sys
sys.path.append(os.getcwd() )


class Database():

	def __init__(self, root =None):
		self.ref = db.reference(root)

	def clear_all(self, default = None):
	    if (default != None):
	        self.ref.set(default)
	        return
	    self.ref.set({})



class Admin(Database):
	def __init__(self ):
		self.__cred = get_cred()
		self.__options = get_options()
		self.app = firebase.initialize_app(options=self.__options,credential = self.__cred)  #Instanzing Root app
		Database.__init__(self,"Sensor")

	def display_count(self):
		return self.ref.child("count").get() 

	def set_status(self,sensor,btn):
		#sensors = ["IR1", "IR2"]
		count = self.display_count()
		status = self.get_status()
		if sensor =="IR1" and status[0] == True:
			count+=1 
		
		else:
			if status[1] == True:
				if count>0 :
					count-=1
				else:
					print("Some Error")

		
		self.ref.update({"count": count})
		btn.text = "Count = %d"%count

	def set_ir(self, sensor,flag = 1):
		status = self.get_status(sensor, flag = 1)
		self.ref.update({sensor: not status})

	def get_status(self,sensors = ["IR1","IR2"],flag =0):
		if flag == 1:
			return self.ref.child(sensors).get()

		return [self.ref.child(sensor).get() for sensor in sensors]


	def __del__(self):
		firebase.delete_app(self.app)

