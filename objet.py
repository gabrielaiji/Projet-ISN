from tkinter import *
from PIL import Image
from PIL import ImageTk
from math import pi


class Objet:
	"""Classe définissant un objet caractérisé par :
	- ses coordonnées;
	- sa vitesse
	- sa masse (plus tard)
	- son image
	- angle de rotation de l'image (en radian)
	- force de rotation (angle de rotatation à pivoter à chaque unité de temps)"""


	def __init__(self, coordx, coordy, vitesse, imageRef):
		"""Constructeur de la Classe"""
		self.coordx = coordx
		self.coordy = coordy
		self._vitesse = vitesse
		#self.masse = masse
		self._imageRef = imageRef
		self._image = PhotoImage(file= self._imageRef)
		self._angle = 0
		self._powerAngle = 0


	def _get_image(self):
		"""Getter de l'image de l'objet"""
		return self._image

	def _set_image(self, image):
		"""Setter de l'image de l'objet"""
		self._image = PhotoImage(file=image)

	def _get_imageRef(self):
		"""Getter de l'adresse l'image de l'objet"""
		return self._imageRef

	def _set_imageRef(self, imageRef):
		"""Setter de l'adresse l'image de l'objet"""
		self._imageRef = imageRef

	def _get_vitesse(self):
		"""Getter de la vitesse de l'objet"""
		return self._vitesse

	def _set_vitesse(self, vitesse):
		"""Setter de la vitesse de l'objet"""
		self._vitesse = vitesse

	def _get_angle(self):
		"""Getter de l'angle de rotation l'image de l'objet EN RADIAN"""
		return self._angle

	def rotateAngle(self, angle):
		"""Change l'angle de rotation de l'image en ajoutant l'angle rentré EN RADIAN à l'angle initial de l'image"""
		self._angle += angle
		self._angle %= 360

		img = Image.open(self._imageRef)
		rotatedImg = img.convert('RGBA').rotate(self._angle, expand=True)				# .convert -> ajoute une couche
		#newImg = Image.new('RGBA', rotatedImg.size)									# Créé une image transparente de la taille de l'image original
		#finalImg = Image.composite(rotatedImg, newImg, rotatedImg)						# Compose l'image pivoté avec un background transparent
		#renderedImg = finalImg.convert(img.mode)										# Reconverti l'image en Image

		self._image = ImageTk.PhotoImage(rotatedImg)									# Converti l'image en ImageTk

	def _get_powerAngle(self):
		"""Getter de l'angle à pivoter à chaque unité de temps"""
		return self._powerAngle

	def _set_powerAngle(self, angle):
		"""Setter de l'angle à pivoter à chaque unité de temps"""
		self._powerAngle = angle



	image = property(_get_image, _set_image)
	imageRef = property(_get_imageRef, _set_imageRef)
	vitesse = property(_get_vitesse, _set_vitesse)
	powerAngle = property(_get_powerAngle, _set_powerAngle)