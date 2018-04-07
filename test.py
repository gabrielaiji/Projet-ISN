from tkinter import *
from tkinter.messagebox import *
from time import sleep
from PIL import Image
from PIL import ImageTk


def game():
	animate()


i, o = 0, 0
animationFLow = True
def animate():
	global i
	global o

	i += 1
	canvas.coords(fusee, 375, 500 - 104 - i)
	#sleep(0.01)

	if animationFLow:
		canvas.after(10, animate)
		print(animationFLow)
		#print(animationFLow)
		#o += 1
		#print(o)

def stop():
	animationFLow = False


mainWindow = Tk()


### Left Label
leftLabel = LabelFrame(mainWindow, text="Menu", pady=20, padx=20)
leftLabel.pack(side=LEFT)

close = Button(leftLabel, text="Fermer", command=mainWindow.quit)
close.pack()


### Canvas
canvas = Canvas(mainWindow, width=750, height=500, background="#0080FF")
canvas.pack(side=LEFT, pady=5)
pp = PhotoImage(file="img\Rocket.png")
ppx, ppy = 375, 500-104
fusee = canvas.create_image(ppx, ppy, image=pp)

#rotatedPp = ImageTk.PhotoImage(Image.open("img\Rocket.png").rotate(90))
#canvas.itemconfigure(fusee, image=rotatedPp)


### Right Label
rightLabel = LabelFrame(mainWindow, text="Game", pady=20, padx=20)
rightLabel.pack(side=RIGHT)

start = Button(rightLabel, text="Start", command=game)
start.pack(pady = 5)
stop = Button(rightLabel, text="Stop", command=stop)
stop.pack()


mainWindow.mainloop()
