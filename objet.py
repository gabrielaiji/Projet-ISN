from tkinter import *
from PIL import Image
from PIL import ImageTk


class Objet:
	"""Classe définissant un objet caractérisé par :
	- ses coordonnées;
	- sa vitesse
	- sa masse (plus tard)
	- son image"""


	def __init__(self, coordx, coordy, vitesse, image):
		"""Constructeur de la Classe"""
		self.coordx = coordx
		self.coordy = coordy
		self._vitesse = vitesse
		#self.masse = masse
		self._image = PhotoImage(file=image)


	def _get_image(self):
		"""Getter de l'image de l'objet"""
		return self._image

	def _set_image(self, image):
		"""Setter de l'image de l'objet"""
		self._image = PhotoImage(file=image)

	def _get_vitesse(self):
		"""Getter de la vitesse de l'objet"""
		return self._vitesse

	def _set_vitesse(self, vitesse):
		"""Setter de la vitesse de l'objet"""
		self._vitesse = vitesse

	image = property(_get_image, _set_image)
	vitesse = property(_get_vitesse, _set_vitesse)
