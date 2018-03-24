from tkinter import *
from tkinter.messagebox import *
from time import sleep

#testest

i, o = 0, 0
def callTest():
	global i
	global o
	
	i += 1
	canvas.coords(fusee, 375, 440 - i)
	sleep(0.01)

	canvas.after(6, callTest)
	o += 1
	print(o)

def Test(ppx, ppy):

	for i in range(0, 250, 5):
		canvas.coords(fusee, 375, 440 - i)
		sleep(2)


fenetre = Tk()

leftLabel = LabelFrame(fenetre, text="Menu", pady=20, padx=20)
leftLabel.pack(side=LEFT)

label = Label(leftLabel, text="Hello World")
label.pack()


canvas = Canvas(fenetre, width=750, height=500, background="red")
canvas.pack(side=LEFT, pady=5)
pp = PhotoImage(file="img\ProfilePicture.png").subsample(2, 2)
ppx, ppy = 375, 440
fusee = canvas.create_image(ppx, ppy, image=pp)


rightLabel = LabelFrame(fenetre, text="Boutons", pady=20, padx=20)
rightLabel.pack(side=RIGHT)

close = Button(rightLabel, text="Fermer", command=fenetre.quit)
close.pack()
start = Button(rightLabel, text="Start", command=callTest)
start.pack()


fenetre.mainloop()
