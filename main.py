
from tkinter import *
from monitor import Monitor
from objet import Objet
from math import pi
from vecteurs import Vecteur


mainWindow = Tk()



### Left Label ###
leftLabel = LabelFrame(mainWindow, text="Menu", pady=20, padx=20)
leftLabel.pack(side=LEFT, padx=5, pady=5)

close = Button(leftLabel, text="Fermer", command=mainWindow.quit)
close.pack()






### Canvas/Monitor ###

vitesseFusee = Vecteur(2, pi/3)
fusee = Objet(0, 0, "img\Rocket.png")
fusee.vitesse = vitesseFusee


monitor = Monitor(mainWindow, 1000, 600, "img\SpaceBackground.png", 5, 5, fusee)





### RIght Label ###
rightLabel = LabelFrame(mainWindow, text="Fusée", pady=20, padx=20)
rightLabel.pack(side=RIGHT, padx=5, pady=5)

advance = Button(rightLabel, text="Avancer", command=monitor.animate)
advance.pack()
stop = Button(rightLabel, text="Stop", command=monitor.pause)
stop.pack()

rotate = Button(rightLabel, text="Rotate 90°", command=monitor.rotateObjet)
rotate.pack()

#canvasBis = Canvas(rightLabel, width=200, height=350, background="white")
#canvasBis.pack()
#img = PhotoImage(file="img\Rocket.png")
#maquette = canvasBis.create_image(100, 175, image = img)

mainWindow.mainloop()