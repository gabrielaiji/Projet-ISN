
from tkinter import *
from objet import Objet
from time import sleep

class Monitor:
	"""Classe Défénissant l'écran du jeu caractérisé par:
	- canvas de tkinter
	- superWindow
	- objets{Instance de l'objet = objet affiché dans le canvas} si affiché
	- background
	- width
	- height
	- animation/pause"""

	def __init__(self):
		self._width = 750
		self._height = 500
		self._background = "#0080FF"
		self._superWindow = Tk()
		self.canvas = Canvas(self._superWindow, width =self._width, height =self._height, background =self._background)
		self.canvas.pack(side=LEFT, padx=5, pady=5)
		self._objets = {}
		self._animation = False
		

	def __init__(self, superWindow, width, height, background, padX, padY):
		self._width = width
		self._height = height
		self._background = background
		self._superWindow = superWindow
		self.canvas = Canvas(self._superWindow, width =self._width, height =self._height, background =self._background)
		self.canvas.pack(side=LEFT, padx=padX, pady=padY)
		self._objets = {}
		self._animation = False
		


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
		"""Setter du background du canvas : RGB ou Image"""
		self._background = background
		self.canvas.config(background = self._background)
		self.canvas.pack()

	width = property(_get_width, _set_width)
	height = property(_get_height, _set_height)
	background = property(_get_background, _set_background)



	def addObjet(self, objet):
		"""Ajouter un objet à afficher"""

		img = objet.image
		self._objets[objet] = self.canvas.create_image(objet.coordx, objet.coordy, image=img)

	def deleteObjet(self, objet):
		"""Supprimer un ojbet de l'écran"""
		#i = self._objets.index(objet)
		#self._objets.remove(objet)
		self.canvas.delete(self._objets[objet])
		del self._objets[objet]

	def rotateObjet(self, objet, angle):
		"""Pivote l'image de l'objet avec un angle en degré"""
		objet.rotateAngle(angle)
		self.canvas.itemconfigure(self._objets[objet], image=objet.image)

	def rotateObjet(self):
		"""Test de la fonction sur boutton"""

		for o in self._objets.keys():
			for i in range(9):
				sleep(1)
				o.rotateAngle(10)
				self.canvas.itemconfigure(self._objets[o], image=o.image)

	def animate(self):
		"""Anime les objets du canvas : pivote puis bouge
		A revoir avec la classe Vecteur à faire"""

		for o in self._objets.keys():

			if o.powerAngle:
				o.rotateAngle(o.powerAngle)
				self.canvas.itemconfigure(self._objets[o], image=o.image)

			o.coordy -= o.vitesse
			self.canvas.coords(self._objets[o], o.coordx, o.coordy)

		self._animation = self.canvas.after(5, self.animate) # Rappelle la fonction animate() toutes les 5 millisecondes


	def pause(self):
		"""Arrête/pause l'animation"""
		self.canvas.after_cancel(self._animation)


