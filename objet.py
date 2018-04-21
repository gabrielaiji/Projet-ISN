from tkinter import *
from PIL import Image
from PIL import ImageTk
from math import pi
from math import sqrt


class Objet:
	"""Classe définissant un objet caractérisé par :
	- ses coordonnées : x et y
	- sa vitesse
	- son accélération
	- sa masse 
	- son image
	- angle de rotation de l'image (EN RADIAN)
	- force de rotation (angle de rotatation à pivoter à chaque unité de temps)"""


	def __init__(self, coordX, coordY, imageRef):
		"""Constructeur de la Classe"""
		self.coordX = coordX
		self.coordY = coordY
		self._vitesse = 0
		self._acceleration = 0
		self.masse = 0
		self._imageRef = imageRef
		self._image = PhotoImage(file =self._imageRef)
		self._angle = pi/2  #EN RADIAN
		self._powerAngle = 0 #EN RADIAN


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

	def _set_vitesse(self, vitesse): # a changer : la détermination du powerAngle
		"""Setter de la vitesse de l'objet"""
		self._vitesse = vitesse

		if self._angle != self._vitesse.angle:
			difference = self._vitesse.angle - self._angle
			
			if (difference > 0 and difference < pi) or (difference > -2*pi and difference < -pi):
				self._powerAngle = pi/250
			elif (difference > -pi and difference < 0) or (difference > pi and difference < 2*pi):
				#difference -= 2*pi
				self._powerAngle = -pi/250


	def _get_angle(self):
		"""Getter de l'angle de rotation l'image de l'objet EN RADIAN"""
		return self._angle

	def rotateAngle(self, angle):
		"""Change l'angle de rotation de l'image en ajoutant l'angle rentré EN RADIAN à l'angle initial de l'image"""
		self._angle += angle
		self._angle %=  2*pi

		img = Image.open(self._imageRef)
		rotatedImg = img.convert('RGBA').rotate((self._angle*180/pi) - 90, expand=True)	# .convert -> ajoute une couche
		#newImg = Image.new('RGBA', rotatedImg.size)									# Créé une image transparente de la taille de l'image original
		#finalImg = Image.composite(rotatedImg, newImg, rotatedImg)						# Compose l'image pivoté avec un background transparent
		#renderedImg = finalImg.convert(img.mode)										# Reconverti l'image en Image

		self._image = ImageTk.PhotoImage(rotatedImg)									# Converti l'image en ImageTk

	def _get_powerAngle(self):
		"""Getter de l'angle à pivoter EN RADIAN à chaque unité de temps"""

		if sqrt((self._vitesse.angle - self._angle)**2) <= sqrt(self._powerAngle**2):
		#si la différence entre l'angle de l'objet et de la vitesse générale est inférieur à l'angle de rotation :
			self._powerAngle = 0
			
		return self._powerAngle

	def _set_powerAngle(self, angle):
		"""Setter de l'angle EN RADIAN à pivoter à chaque unité de temps"""
		self._powerAngle = angle



	image = property(_get_image, _set_image)
	imageRef = property(_get_imageRef, _set_imageRef)
	vitesse = property(_get_vitesse, _set_vitesse)
	angle = property(_get_angle)
	powerAngle = property(_get_powerAngle, _set_powerAngle)