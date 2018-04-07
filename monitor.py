
from tkinter import *
from objet import Objet

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

	def animate(self):
		"""Anime les objets du canvas
		A revoir avec la classe Vecteur à faire"""

		for o in self._objets.keys():
			o.coordy -= o.vitesse
			self.canvas.coords(self._objets[o], o.coordx, o.coordy)

		self._animation = self.canvas.after(10, self.animate)


	def pause(self):
		"""Arrête/pause l'animation"""
		self.canvas.after_cancel(self._animation)



