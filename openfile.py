from Tkinter import *
import tkFileDialog
class abrearchivo(Frame):

	def __init__(self):
		Frame.__init__(self)
		self.master.geometry("200x100")
		self.pack(expand=1,fill=BOTH)
		self.boton=Button(self,text = "AbrirArchivo",command = self.abri)
		self.boton.pack()

	def abri(self):
		inputFile=tkFileDialog.askopenfile()
	 	for linya in inputFile:
	 		Salida=linya.split(":")

	 		print Salida[0]
	 	inputFile.close()


abrearchivo().mainloop()