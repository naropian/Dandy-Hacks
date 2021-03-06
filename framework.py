# NapTimes 0.1.0
#
# Made entirely by Santiago Loane and nobody else at all
#
# #leggo #dandyhacks
#

#imports needed libraries, tkinter is the graphics & display tool
from tkinter import *
from tkinter import ttk
#from PIL import Image

#im = Image.open("images/pillow.png")

occupied = [False]*288
for x in range(7*12,11*12):
	occupied[x]=True


def sleep(*args):
	"Zzzz"

def pillow(*args):
#	im.show()
	"woo"

def clrtoggle(x,y):
	#mainframe.grid_remove(column=i+1,row=j+2)
	ttk.Button(mainframe, text="%d AM" %(j+1), style='busy.TButton').grid(column=i+1, row=j+2)

#beginning of a tkinter window
root = Tk()
root.title("NapTime bEtA")

busy = ttk.Style()
busy.configure('busy.TButton',background='#D96267')
free = ttk.Style()
free.configure('free.TButton',background='#62D962')

#makes the primary display widget
mainframe = ttk.Frame(root, padding = "2 2 2 2")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure(1,weight=1)

#Adds labels for each day of the week
weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
for i in range(0,len(weekdays)):
	ttk.Label(mainframe, text=weekdays[i]).grid(column=i+1, row=1, sticky=N)

#Adds hour labels
for j in range(0, 11): 
	ttk.Label(mainframe, text="%d AM" %(j+1)).grid(column=0, row=(j+3)*12, rowspan=12)
for k in range(12, 23): 
	ttk.Label(mainframe, text="%d PM" %(k-12+1)).grid(column=0, row=(k+4)*12, rowspan=12)

ttk.Label(mainframe, text="12 AM").grid(column=0, row=2*12, rowspan=12)
ttk.Label(mainframe, text="12 PM").grid(column=0, row=14*12, rowspan=12)

#hours = StringVar()
#time = StringVar()
#hours_entry = ttk.Entry(mainframe, width=7, textvariable=hours)
#hours_entry.grid(column=2, row=3, sticky=(W,E))
#ttk.Label(mainframe, textvariable=time).grid(column=2, row=2, sticky=(W,E))
#ttk.Button(mainframe, text="Nothing! Wow!", command=sleep).grid(column=3, row=3, sticky=W)

#Adds labels for each day of the week
weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
for i in range(0,len(weekdays)):
	ttk.Label(mainframe, text=weekdays[i]).grid(column=i+1, row=1, sticky=N)


#ttk.Label(mainframe, text="Hours").grid(column=1, row=2, sticky=W)
#ttk.Label(mainframe, text="you should").grid(column=2, row=2, sticky=E)
#ttk.Label(mainframe, text="take a nap!").grid(column=3, row=2, sticky=W)

#ttk.Button(mainframe, text = "Go to sleep now", command=pillow).grid(column=4, row=2, columnspan=2)

#image.grid(row=3, column=6, rowspan=2, columnspan=2, sticky = (N,E,S,W), padx=5, pady=5)

#adds extra padding for each element in grid
for child in mainframe.winfo_children():
	child.grid_configure(padx=5, pady=5)
#focus on the hours entered!
#hours_entry.focus()
#also submit the form if they press enter, not just on button press
root.bind('<Return>', sleep)

#end of tkinter window
root.mainloop()