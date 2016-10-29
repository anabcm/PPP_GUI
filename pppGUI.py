
#===================================================================================
#Interfaz Grafica para PPP del Phd. H.Yee
#Instituto Politecnico Nacional
#Centro de Investigacion en Computacion
#Maestria en Ciencias de la Computacion
#ISC. Ana Bertha Cruz Martinez
#Directores: Dr. Adolfo Guzman Arenas   Dr. Omar Lopez-Cruz

#===================================================================================
#TO RUN, run "ppp". Commands have the following
#  format:     NAME <F1> <F2> <Optional inputs>
# maximum of 5 inputs (incl. frame #s) can be accepted; but
#  only the name is absolutely necessary. If absent, the program
#ill request further information as needed.  The optional
#inputs follow the same sequence as that requested by the
#command.  Optional inputs are indicated by: N=name (no space
#allowed), S=string (enclosed by " if there are spaces), F=
#frame #, I=int, R=real, B=box #.  No explanations to these
#are provided in help, since one can run the program faster
#by simply letting the command do the prompting instead of
#looking them up in HELP.  For 530X530 (default picture size),
#a total of 9 frames are available in the program core buffer
#for immediate operation by the program. A 10th frame is used
#as the scratch frame for many of the operations.  The use of
#it is possible for some commands but it is not recommended.
#The core picture buffer can be partitioned to larger size,
#with the maximum being 1 (+1 scratch) 1280X1280 pictures.
#Up to 250 pictures can be stored in the DISK directory 
#===================================================================================

#==================================MENU=================================================
from Tkinter import *
import Pmw
import tkFileDialog
import tkMessageBox

class Subframe(Frame):
	def __init__(self, parent):
		Frame.__init__(self,parent)
		self.parent=parent
		self.master.title("Otra cosa")
		self.pack(expand=1,fill=BOTH)




class Menu(Frame):
	def __init__(self):
		Frame.__init__(self)

		self.master.title("PPP")
		Pmw.initialise()
		self.master.geometry("300x200")
		self.pack(expand=1,fill=BOTH)
		self.menu=Pmw.MenuBar(self)
		self.menu.pack(fill=X)
		self.miBV=BooleanVar()
		self.menu.addmenu("File","Image")

		self.menu.addmenuitem("File","command",label="Open Script",command=self.OpenScript)
		self.menu.addmenuitem("File","command",label="New",command=self.NewFile)
		self.menu.addmenuitem("File","command",label="Coordinates",command=self.Coordinates)
		self.menu.addmenuitem("File","command",label="Parameters",command=self.Parameters)

		self.menu.addmenu("Image","Operations")
		self.menu.addmenuitem("Image","command",label="Read Image",command=self.OpenIma)
		self.menu.addmenuitem("Image","command",label="Write Image",command=self.metodo)
		self.menu.addmenuitem("Image","command",label="SAOimage",command=self.SAOimage)
		self.menu.addmenuitem("Image","command",label="Fixing",command=self.Fixing)
		self.menu.addmenuitem("Image","command",label="Boxing",command=self.Boxing)
		self.menu.addmenu("Operations","ObjectFinding")
		self.menu.addmenuitem("Operations","command",label="op1",command=self.metodo)
		self.menu.addmenuitem("Operations","command",label="OP2",command=self.metodo)

		self.menu.addmenu("ObjectFinding","Photometry")
		self.menu.addmenuitem("ObjectFinding","command",label="OP1",command=self.metodo)
		self.menu.addmenuitem("ObjectFinding","command",label="OP2",command=self.metodo)

		self.menu.addmenu("Photometry","Graphics")
		self.menu.addmenuitem("Photometry","command",label="OP1",command=self.metodo)
		self.menu.addmenuitem("Photometry","command",label="OP2",command=self.metodo)
		self.menu.addmenu("Graphics","File")
		self.menu.addmenuitem("Graphics","command",label="Plotting",command=self.metodo)
		self.menu.addmenuitem("Graphics","command",label="OP2",command=self.metodo)
#		self.menu.addcascademenu("File","Open","Close")


#self.menu.addmenuitem("Close","checkbutton",label="BB",command=self.metodo2,variable=self.miBV)
	def SAOimage(self):
		tkMessageBox.showinfo(None,"SAOimage")

	def Fixing(self):
		tkMessageBox.showinfo(None,"Fixing")

	def Boxing(self):
		tkMessageBox.showinfo(None,"Boxing")


	def OpenIma(self):
		inputFile= tkFileDialog.askopenfilename()
		if inputFile != None:
			print inputFile

		#set imdir /home/directory/etc
		#rdis Nombre y numero
		#write image with wdis

	def Coordinates(self):
		tkMessageBox.showinfo(None,"Coordinates")
		#parameter iorient center of pixel like (1.0,1.0) oriented=1 is default option

	def Parameters(self):
		tkMessageBox.showinfo(None,"Parameters")
		#name="dgs"
		#subFrame = Subframe(self, name=name)
    	#subFrame.pack(side="left", fill="y")
    	#self.all_instances.append(subFrame)
		#set all global parameters
		#set parameter-name value
		#option save or default
		#frame size nu an nv
		#vi ppparam for all parameters


	def NewFile(self):
		Name=tkFileDialog.asksaveasfile()
		tkMessageBox.showinfo(None,"NewFile")
#		File=open(Name,"w")

	def OpenScript(self):
		tkMessageBox.showinfo(None,"OpenScript")
		inputFile=tkFileDialog.askopenfile()
		for linya in inputFile:
	 		Output=linya.split(":")
			print Output[0]
	 	inputFile.close()

	def metodo(self):
		tkMessageBox.showinfo(None,"Limitado")

	def metodo2(self):
		if self.miBV.get():
			tkMessageBox.showinfo(None,"Para la bara")

root=Menu()
root.mainloop()



