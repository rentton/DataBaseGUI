#Note: Done before understand decorators

from tkinter import *
from data import *
import sys

#Create the graphic interface
class GUI:

	def __init__(self):

		########### ROOT ###########
		self.__root = Tk()
		self.__root.title("DataBase Manager")
		self.__root.resizable(width=False, height=False)
		self.__root.iconbitmap("icono.ico")

		########### FRAME ###########
		self.__frame = Frame()
		self.__frame.pack()
		self.__frame.configure(background="#2E4C6D")

		self.__entries = []
		self.__buttons = []
		
		########### CREATE THE LABELS ###########
		for lab,pos in zip(labels,range(len(labels))):
			Label(self.__frame,text=lab, bg="#2E4C6D", font=("Arial",11,"bold")).grid(row=pos,
				column=0,padx=10,pady=10,columnspan=2)


		########### CREATE AND SAVE THE ENTRIES ###########
		for ins in range(len(labels)-1):
			inp = Entry(self.__frame,bg="#396EB0",bd="6")
			inp.grid(row=ins,column=1,padx=10, pady=10,columnspan=4)
			self.__entries.append(inp)

		########### CREATE THE TEXT WITH SCROLL ###########
		self.__text = Text(self.__frame,width=15,height=5,bg="#396EB0",bd="6")
		self.__text.grid(row=len(labels)-1,column=1, padx=10,pady=10, columnspan=4)
		scroll = Scrollbar(self.__frame,command=self.__text.yview)
		scroll.grid(row=len(labels)-1, column=1, pady=10, sticky="nse", columnspan=4)
		self.__text.config(yscrollcommand=scroll.set)

		########### CREATE THE MENU ###########
		menu_bar = Menu(self.__root)
		self.__root.config(menu=menu_bar)

		DB = Menu(menu_bar,tearoff=0)
		DB.add_command(label="Start")
		DB.add_command(label="Exit")
		edit = Menu(menu_bar,tearoff=0)
		edit.add_command(label="Delete entries")

		menu_bar.add_cascade(label="BD", menu=DB)
		menu_bar.add_cascade(label="Edit", menu=edit)

		########### CREATE AND SAVE THE BUTTONS ###########
		for b,pos in zip(buttons_names,range(len(buttons_names))):
			button = Button(self.__frame, text=b, bg="#2E4C6D", font=("Arial",10,"bold"), 
				bd = 6, relief="raised", cursor = "hand2", highlightcolor="#396EB0", 
				width="6")
			button.grid(row=len(labels),column=pos, padx=3,pady=3)
			self.__buttons.append(button)


	def root(self):
		return self.__root

	def buttons(self):
		return self.__buttons

	def entries(self):
		return self.__entries

	def text(self):
		return self.__text

	def destroy(self):
		self.__root.destroy()


