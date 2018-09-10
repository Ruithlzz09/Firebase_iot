#Dependenices
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import ListProperty

# Window Configuration --- To set Window Height and Width
from kivy.config import Config
Config.set("graphics", "width", "600")
Config.set("graphics", "height", "400")

#Custom built Module for User regarding Server Acess and User Interaction
from Server import *

class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        GridLayout.__init__(self)
        self.user =Admin()
        self.cols  = 2  #important features-- represent no. of cols in screen
        #self.rows = 2 #use with care

        self.btn1  = Button( text =   "IR1" ,font_size = 16 )
        self.btn2  = Button( text =   "IR2" ,font_size = 16 )
        self.count = Label(  text =   "Count = %d"%self.fetch_count())
        self.reset = Button( text =   "RESET" ,font_size = 16)
        #self.status1 = Button (text = "status1")
        #self.status2 = Button (text = "status2")
        #self.cls.bind(on_press = self.clear_all)
        self.btn1.bind(on_press = lambda x: self.user.set_status("IR1",self.count))
        self.btn2.bind(on_press = lambda x: self.user.set_status("IR2",self.count))
        self.reset.bind(on_press = self.intial)
        #self.status1.bind(on_press = lambda x: self.user.set_ir("IR1"))
        #self.status2.bind(on_press = lambda x: self.user.set_ir("IR2"))

        self.add_widget(self.btn1)
        self.add_widget(self.btn2)
        #self.add_widget(self.status1)
        #self.add_widget(self.status2)
        self.add_widget(self.count)
        self.add_widget(self.reset)



    def intial(self, event):
    	self.user.ref.update({"IR1": True, "IR2": True, "count":0})
    	self.count.text = "Count = 0"

    def fetch_count(self):
    	return self.user.ref.child("count").get()


class MyApp(App):
    
    def build(self):
    	self.title = "IoT_Server"  #setting window title
    	self.icon  = "abstract-icon.png"  #setting window icon..In case of given icon doesn't exist ,it will display default icon.
    	return LoginScreen()


if __name__ == "__main__":
    MyApp().run()