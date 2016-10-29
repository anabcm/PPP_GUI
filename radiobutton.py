from Tkinter import *
from tkMessageBox import *

class ChannelButton(Frame):


	def __init__(self):
		Frame.__init__(self)
		self.master.title("Radiobutton")
		self.master.geometry("250x60")
		self.pack(expand = YES, fill=BOTH)
		self.laman=Entry(self, width=60,justify=CENTER)
		self.laman.insert(INSERT, "qu onda")
		self.laman.config(state=DISABLED)

		self.laman.pack(padx=5, pady=5)
		listahanNgChannels = ["A","B","C"]
		self.napilingChannel =StringVar()
		self.napilingChannel.set("A")

		for istasyon in listahanNgChannels:
			isangButones = Radiobutton(self, text=istasyon,value=istasyon, variable=self.napilingChannel, command=self.metodo)
			isangButones.pack(side=LEFT,expand=1,fill=BOTH)

	def metodo(self):
		print self.napilingChannel.get()
		if self.napilingChannel.get() == "A":
			showinfo("Tagline","Selecciono A")
		elif self.napilingChannel.get() == "B":
			showinfo("Tagline","Selecciono B")
		elif self.napilingChannel.get() == "C":
			showinfo("Tagline","Selecciono C")
		else:
			showinfo("Tagline","No se")

ChannelButton().mainloop()