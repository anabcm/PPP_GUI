from Tkinter import *
class Grid(Frame):

	def __init__(self):
		Frame.__init__(self)
		self.master.title(" un grid")
		self.master.geometry("350x250")
		self.pack(expand=1,fill=BOTH)

		self.B1=Button(self,text="Boton1",command=self.metodo1)
		self.B1.grid(row=0,columnspan=3,sticky=W+E+N+S,padx=5,pady=5)

		self.B2=Button(self,text="Boton2",command=self.metodo2)
		self.B2.grid(row=1,column=0,sticky=W+E+N+S,padx=5,pady=5)

		self.centro=Label(self,text="Dale clic", foreground="blue")
		self.centro.grid(row=1,column=1,sticky=W+E+N+S)

		self.B3=Button(self,text="Boton3", command=self.metodo3)
		self.B3.grid(row=1,column=2,sticky=W+E+N+S,padx=5,pady=5)

		self.B3=Button(self,text="Boton4", command=self.metodo4)
		self.B3.grid(row=2,columnspan=3,sticky=W+E+N+S,padx=5,pady=5)

		self.columnconfigure(0,weight=1)
		self.columnconfigure(1,weight=1)
		self.columnconfigure(2,weight=1)
		self.rowconfigure(0,weight=1)
		self.rowconfigure(1,weight=1)
		self.rowconfigure(2,weight=1)

	def metodo1(self):

		self.centro.config(text="boton 1")

	def metodo2(self):

		self.centro.config(text="boton 2")

	def metodo3(self):
		self.centro.config(text="boton 3")

	def metodo4(self):
		self.centro.config(text="boton 4")








Grid().mainloop()