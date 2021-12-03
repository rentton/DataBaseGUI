import sqlite3
from tkinter import messagebox


#We r going to considere that dir and more can be null

#Dedicate to sql commands
class DataBase:

	def __init__(self):
		self.__connex = sqlite3.connect("DB")
		self.__pointer = self.__connex.cursor()
		self.__pointer.execute(''' 
			CREATE TABLE DB(
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			Name VARCHAR(15) NOT NULL,
			Password VARCHAR(20) UNIQUE NOT NULL,
			Dir VARCHAR(10),
			More VARCHAR(50) )
			''')

	def exit():
		self.__connex.close()

	def __rewrite(self,data, separator):
		str = ""
		for d in data:
			if data[d]:
				str += f"{d} = {data[d]} {separator}"

		#To remove the last separator
		str = str[0:len(str)-len(separator)]
		return str

	def insert(self,data):
			for i in data:
				if not data[i]:
					data[i] = 'NULL'
			self.__pointer.execute(f"INSERT INTO DB VALUES {str(tuple(data.values()))}")
			self.__connex.commit()

	def consult(self,data):

		#True if at least one is different to None
		print(data)
		if any(data.values()):
			self.__pointer.execute(f"SELECT * FROM DB WHERE {self.__rewrite(data,'AND')}")
	
		else:
			self.__pointer.execute("SELECT * FROM DB")
		outs = self.__pointer.fetchall()
		print(outs)


	def delete(self,data):
		#True if at least one is different to None
		if any(data.values()):
			self.__pointer.execute(f"DELETE FROM DB WHERE {self.__rewrite(data,'AND')}")
		else:
			self.__pointer.execute("DELETE FROM DB")

	#Updates are done by ID field
	def update(self,data):
		ID = data["ID"]
		data["ID"] = None
		self.__pointer.execute(f"UPDATE DB SET {self.__rewrite(data,',')} WHERE ID = {ID}")






	