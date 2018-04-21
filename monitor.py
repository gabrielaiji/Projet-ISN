
from tkinter import *
from objet import Objet
from time import sleep
from math import pi #temporary
from PIL import Image
from PIL import ImageTk

class Monitor:
	"""Classe Défénissant l'écran du jeu caractérisé par:
	- canvas de tkinter
	- superWindow
	- objets{Instance de l'objet = objet affiché dans le canvas} si affiché
	- background
	- width
	- height
	- animation/pause
	- focus : le canvas peut être centré sur un objet"""

	def __init__(self):
		self._width = 750
		self._height = 500
		self._background = "#0080FF"
		self._renderedBackground
		self._superWindow = Tk()
		self.canvas = Canvas(self._superWindow, width =self._width, height =self._height, background =self._background)
		self.canvas.pack(side=LEFT, padx=5, pady=5)
		self._objets = {}
		self._animation = False
		self._focus
		

	def __init__(self, superWindow, width, height, background, padX, padY, focus):
		self._width = width
		self._height = height
		self._superWindow = superWindow
		self.canvas = Canvas(self._superWindow, width =self._width, height =self._height, background ="#0080FF")
		self.canvas.pack(side=LEFT, padx=padX, pady=padY)
		self._objets = {}
		self._animation = False

		self._set_focus(focus)
		self._set_background(background)
		self.addObjet(focus)
		
		
		
		


	def _get_width(self):
		"""Getter de la largeur du canvas"""
		return self._width

	def _set_width(self, width):
		"""Setter de la largeur du canvas"""
		self._width = width
		self.canvas.config(width = self._width)
		self.canvas.pack()

	def _get_height(self):
		"""Getter de la hauteur du canvas"""
		return self._height

	def _set_height(self, height):
		"""Setter de la hauteur du canvas"""
		self._width = height
		self.canvas.config(height = self._height)
		self.canvas.pack()

	def _get_background(self):
		"""Getter du background du canvas"""
		return self._background

	def _set_background(self, background):
		"""Setter du background du canvas : path de l'Image"""
		self._background = ImageTk.PhotoImage(file=background)

		self._renderedBackground = self.canvas.create_image(self._width/2 - self._focus.coordX, self._height/2 - self._focus.coordY, image=self._background)

	def _get_focus(self, objet):
		"""Getter de l'objet sur lequel est centré le canvas"""
		return self._focus

	def _set_focus(self, objet):
		"""Setter du focus du canvas : le canvas sera centré sur cet objet"""
		self._focus = objet
	

	width = property(_get_width, _set_width)
	height = property(_get_height, _set_height)
	background = property(_get_background, _set_background)
	focus = property(_get_focus, _set_focus)



	def addObjet(self, objet):
		"""Ajouter un objet à afficher"""

		self._objets[objet] = self.canvas.create_image(objet.coordX - self._focus.coordX + self._width/2, objet.coordY - self._focus.coordY + self._height/2, image=objet.image)

	def deleteObjet(self, objet):
		"""Supprimer un ojbet de l'écran"""

		self.canvas.delete(self._objets[objet])
		del self._objets[objet]

	def rotateObjet(self, objet, angle):
		"""Pivote l'image de l'objet avec un angle en degré"""

		objet.rotateAngle(angle)
		self.canvas.itemconfigure(self._objets[objet], image=objet.image)

	def rotateObjet(self): #temporary
		"""Test de la fonction sur boutton"""

		for o in self._objets.keys():
			
			o.rotateAngle(-pi/2)
			self.canvas.itemconfigure(self._objets[o], image=o.image)
			o.vitesse = o.vitesse

	def animate(self):
		"""Anime les objets du canvas : pivote puis bouge"""

		self.canvas.coords(self._renderedBackground, self._width/2 -(self._focus.coordX + self._focus.vitesse.normeX), self._height/2 -(self._focus.coordY - self._focus.vitesse.normeY))
		#recentre le background sur le l'objet focus

		for o in self._objets.keys():

			if o.powerAngle:	
				o.rotateAngle(o.powerAngle)
				self.canvas.itemconfigure(self._objets[o], image=o.image)
			else:
				o.rotateAngle(o.vitesse.angle - o.angle)
				self.canvas.itemconfigure(self._objets[o], image=o.image)

			if o.vitesse:

				o.coordY -= o.vitesse.normeY
				o.coordX += o.vitesse.normeX
				self.canvas.coords(self._objets[o], o.coordX - self._focus.coordX + self._width/2, o.coordY - self._focus.coordY + self._height/2)



		self._animation = self.canvas.after(10, self.animate) # Rappelle la fonction animate() toutes les 10 millisecondes


	def pause(self):
		"""Arrête/pause l'animation"""
		self.canvas.after_cancel(self._animation)



