from GUI import *
from DataBase import *
import sys

#Create the logic of the program
class logic:
	def __init__(self):
		#To access to objects in the GUI
		self.__obj = GUI()

		#Strings to get the information writed in entries
		self.__field_inputs = []
		for i in labels:
			self.__field_inputs.append(StringVar())
		
		#To save the entries inputs
		self.__inputs = []

		#DB 
		self.__DB = None


	#Read the characters writed in the entries
	def read(self):
		#Entries widget
		for str_ in self.__field_inputs:
			if str_.get() == "":
				self.__inputs.append(None)
			else:
				self.__inputs.append(str_.get())
			str_.set("")

		#Text widget
		#Note: 1.0 --> Read in one line // end-1c --> Read till end except last tab
		text = self.__obj.text().get("1.0",
			'end-1c')
		if text == '':
			self.__inputs[len(self.__inputs)-1] = None
		else:
			self.__inputs[len(self.__inputs)-1] = text

		print(dict(zip(labels,self.__inputs)))
		return dict(zip(labels,self.__inputs))

	#Action when we push a buttom
	def act(self,kind):
		#We need create DB before
		if not self.__DB:
			messagebox.showwarning("DataBase", 
				"You have to create database first. Go DB/start")
		else:	
			data = self.read()
			if kind == 'Insert':
				self.__DB.insert(data)
			elif kind == 'Consult':
				self.__DB.consult(data)
			elif kind == 'Update':
				self.__DB.update(data)
			elif kind == 'Delete':
				self.__DB.delete(data)
			self.__inputs.clear()


	def __config_entries(self):
		#Asign one string to each entry
		for ins, str_ in zip(self.__obj.entries(),self.__field_inputs):
			ins.config(textvariable=str_)

	def __config_buttons(self):
		#Asign a function to the buttons, action = button text
		for b in self.__obj.buttons():
			b.config(command = lambda action=b.cget('text') : self.act(action))

	def __start(self):
		self.__DB = DataBase()
		print("Creating DataBase...")

	def __exit(self):
		exit()
		self.__obj.destroy()
		sys.exit(0)

	def __delete_entries(self):
		for i in self.__field_inputs:
			i.set("")
		self.__obj.text().delete(1.0,"end")

	def __config_menu(self):
		DB = self.__obj.menu()[0]
		DB.entryconfig(0,command = self.__start)
		DB.entryconfig(1,command = self.__exit)

		edit = self.__obj.menu()[1]
		edit.entryconfig(0,command = self.__delete_entries)


	def config(self):
		self.__config_entries()
		self.__config_buttons()
		self.__config_menu()

	
	def obj(self):
		return self.__obj

l1 = logic()
l1.config()
l1.obj().root().mainloop()
