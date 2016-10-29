from Tkinter import *
import Pmw
import tkMessageBox

class Menu(Frame):
	def __init__(self):
		Frame.__init__(self)
		Pmw.initialise()
		self.master.geometry("300x200")
		self.pack(expand=1,fill=BOTH)
		self.menu=Pmw.MenuBar(self)
		self.menu.pack(fill=X)
		self.menu.addmenu("Archivo","Editar")
		self.menu.addmenuitem("Archivo","command",label="lugar",command=self.metodo)
		self.menu.addcascademenu("Archivo","Editar")
		self.miBV=BooleanVar()
		self.menu.addmenuitem("Editar","checkbutton",label="BB",command=self.metodo2,variable=self.miBV)


	def metodo(self):
		tkMessageBox.showinfo(None,"Limitado")

	def metodo2(self):
		if self.miBV.get():
			tkMessageBox.showinfo(None,"Para la bara")


Menu().mainloop()
