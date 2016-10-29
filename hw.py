from Tkinter import *
import Tkinter
from tkMessageBox import *
#top=Tkinter.Tk()

#CheckVar2=IntVar()
#C1=Checkbutton(top,text="Music",variable=CheckVar1,onvalue= 1,offvalue= 0, height = 5,width= 20)	
#C2=Checkbutton(top,text="Video",variable=CheckVar2,onvalue= 1,offvalue= 0, height = 5,width= 20)

class Application(Frame):


    def say_hi(self):
        print "hi there, everyone!"
    
    def mi(self):
        print "Este es mi boton!"

    def anL(self, probeta):
	print "Hola",probeta.widget.get()

    def Mensaje(self, probeta):

	pangalan=probeta.widget.winfo_name()
	laman=probeta.widget.get()
	showinfo("Mesage",pangalan+" : "+laman)#nombre de la caja de texto mas el contenido

    def enter(self, probeta):
	probeta.widget.config(relief=GROOVE)

    def soltar(self, probeta):
	probeta.widget.config(relief=RAISED)

    def createWidgets(self):

	CheckVar1=IntVar()
#LABELS
	self.label=Label(self, text="Esta es una GUI en Python")
	self.label.pack()
#Entry
	self.text=Entry(self,name="cajadeTexto")
	self.text.bind("<Return>",self.Mensaje)
	#self.text.insert(INSERT,"noseque") #porsiquiero texto por defaul
	self.text.pack()

#creando botones
	
	self.rowconfigure(0,weight=1)
	self.columnconfigure(0,weight=1)
	
	self.boton=	Button(self, text="otro", command = self.Mensaje)
	self.boton.bind("<Enter>",self.enter)
	self.boton.bind("<Leave>",self.soltar)
	
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

	self.Mio = Button(self)
	self.Mio["text"] = "Mi boton"
	self.Mio["fg"] = "blue"
	self.Mio["command"] = self.mi
	self.Mio.pack({"side": "left"})
	
	self.Mio1 = Button(self)
	self.Mio1["bitmap"] = "info"
	self.Mio1["fg"] = "blue"
	self.Mio1["command"] = self.mi
	self.Mio1.pack({"side": "left"})

#radiobutton



#cHEKBUTTON
	self.opcions=Checkbutton(self,text="otra",variable=CheckVar1,onvalue= 1,offvalue= 0, height = 5,width= 20)
	#self.opcions.pack({"side": "left"})


    def __init__(self, master=None):
        Frame.__init__(self, master)
	self.master.title("Mi API")

        self.pack()
	#C1.pack()
	#C2.pack()

        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
