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

	def __valid_name(self,name):
		max_lenght = 15

		#Checking the lenght 
		if len(name) > max_lenght:
			return (False,len(name))

		#Checking the letters r correct
		for letter in name:
			if not ('A' <= letter <= 'Z' or 'a' <= letter <= 'z'):
				print(f"{letter} --")
				return (False,letter)
		return (True,'')

	def __valid_password(self,password):
		number = False
		letter = False
		capital = False
		min_length = 5

		#Checking the lenght
		if len(password) < min_length:
			return (False,len(password))

		#Checking the letters r correct
		for let in password:
			if 'a' <= let <= 'z':
				letter = True
			elif 'A' <= let <= 'Z':
				capital = True
			elif '0' <= let <= '9':
				number = True
			else:
				return (False,let)

		if number and capital and letter:
			return (True,'')
		return (False,'Invalid rule')


	def __valid(self,vals):
		valid_name = self.__valid_name(vals["Name"])
		valid_pass = self.__valid_password(vals["Password"])
		error = ""
		
		#Checks the id: if doesn't exist is created automatically bc of 
		# AUTOINCREMENT SQLite3 argument
		if vals["ID"]:
			#We try to convert ID into integer
			try:
				int(vals["ID"])
			except:
				error += "ID must be numeric\n"

		#Checks the name
		if not valid_name[0]:
			#Too long
			if isinstance(valid_name[1],int): 
				error += "Maximum size for the name is 15 characters\n"
			#Invalid charac
			if isinstance(valid_name[1],str):
				error += f"The character {valid_name[1]} is invalid for the name\n"

		#Check the password
		if not valid_pass[0]:
			#Too short
			if isinstance(valid_pass[1],int): 
				error += f"Minimun size for the password is 5 characters\n"
			#Incorrect password
			if valid_pass[1] == "Invalid rule":
				error += "The password should contain at least a capital letter a lower case letter and a number\n"
			#Invalid character
			if isinstance(valid_pass[1],str):
				error += f"The password cannot contain the character {valid_pass[1]}\n"
		
		if error:
			messagebox.showerror("Data Exception", error)
			return False
		return True

	#Read the characters writed in the entries
	def read(self):
		#Entries widget
		for str_ in self.__field_inputs:
			if str_.get() == "":
				self.__inputs.append(None)
			else:
				self.__inputs.append(str_.get())

		#Text widget
		#Note: 1.0 --> Read in one line // end-1c --> Read till end except last tab
		text = self.__obj.text().get("1.0", 'end-1c')
		if text == '':
			self.__inputs[len(self.__inputs)-1] = None
		else:
			self.__inputs[len(self.__inputs)-1] = text

		vals = dict(zip(labels,self.__inputs))
		
		#If the entries are valid
		if self.__valid(vals):
			self.__delete_entries()
			return vals
		#If not keep the entries to the user fix the error
		return None

	#Action when we push a buttom
	def act(self,kind):
		#We need create DB before
		if not self.__DB:
			messagebox.showwarning("DataBase", 
				"You have to create database first. Go DB/start")
		else:	
			data = self.read()
			if data:	
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
