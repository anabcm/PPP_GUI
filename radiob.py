from Tkinter import *
class ChannelButton(Frame):


	def __init__(self):
		listahanChannels = ["A","B","C"]
		self.napilingChannel =stringVar()
		self.napilingChannel.set("C")

		for istasyon in listahanNgChannels:
			isangButones = Radiobutton(self, text=istasyon,value=istasyon, variable=self.napilingChannel, command=self.metodo)
			isangButones.pack(side=LEFT,expand=1,fill=BOTH)

	def metodo(self):
		print self.napilingChannel.get()
		if self.napilingChannel.get()=="A":
			showinfo("Tagline","Selecciono A")
		elif self.napilingChannel.get()=="B":
			showinfo("Tagline","Selecciono B")
		elif self.napilingChannel.get()=="C":
			showinfo("Tagline","Selecciono C")
		else:
			showinfo("Tagline","No se")

ChannelButton().mainloop()
