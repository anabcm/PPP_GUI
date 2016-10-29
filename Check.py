from Tkinter import *
from tkMessageBox import *

class CheckbuttonTest(Frame):


	def __init__(self):
		Frame.__init__(self)
		self.master.title("Checkbutton")
		self.master.geometry("200x500")
		self.pack(expand=YES,fill=BOTH)

		self.titulo=Entry(self,width=20,font="Arial 10",justify=CENTER)
		self.titulo.insert(INSERT,"Opciones")
		self.titulo.pack(padx=5,pady=5)

		self.VarBa1=BooleanVar()
		self.check=Checkbutton(self, text="OP1",variable =self.VarBa1,command=self.metodo)
		self.check.pack(side=LEFT,expand=YES,fill=X)

		self.VarBa2=BooleanVar()
		self.check=Checkbutton(self,text="Op2",variable=self.VarBa2, command=self.metodo)
		self.check.pack(side=LEFT,expand=YES,fill=X)
	
	def metodo(self):
		Letra="Arial 10"
		if self.VarBa1.get():
			Letra+=" bold"
		if self.VarBa2.get():
			Letra+=" italic"
		self.titulo.config(font=Letra)







CheckbuttonTest().mainloop()