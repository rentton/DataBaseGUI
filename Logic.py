from GUI import *
from tkinter import messagebox

class logic:
	def __init__(self):
		#To access to objects in the GUI
		self.__obj = GUI()

		#Srings to get the information writed in entries
		self.__field_inputs = []
		for i in labels:
			self.__field_inputs.append(StringVar())
		
		
		#To save the inputs in entries
		self.__inputs = []

	#Asign one string to each entrie
	def __config_entries(self):
		for ins, str_ in zip(self.__obj.entries(),self.__field_inputs):
			ins.config(textvariable=str_)


	def __config_buttons(self):
		pass
		# for b in self.__obj.buttons():
		# 	#Insert
		# 	if b.cget('text') == buttons_names[0]:
		# 		b.config(command= self.__insert)
		# 	#Consult
		# 	elif b.cget('text') == buttons_names[1]:


		# 	#Update
		# 	elif b.cget('text') == buttons_names[2]:
		# 		pass
			
		# 	#Delete
		# 	elif b.cget('text') == buttons_names[3]:
		# 		pass

	def config(self):
		self.__config_entries()
		self.__config_buttons()

	def read(self):
		#Read entries widget
		for str_ in self.__field_inputs:
			if str_.get() == "":
				self.__inputs.append(None)
			else:
				self.__inputs.append(str_.get())
			str_.set("")

		#Read text widget
		#Note: 1.0 --> Read in one line // end-1c --> Read till end except last tab
		self.__inputs[len(self.__inputs)-1] = self.__obj.text().get("1.0",
			'end-1c')
		print(self.__inputs)

	#Insert operation
	def __insert(self):
		read()

	def consult(self):
		pass

	def update(self):
		pass

	def delete(self):
		pass


	
	def obj(self):
		return self.__obj

l1 = logic()
l1.config()
l1.obj().root().mainloop()
