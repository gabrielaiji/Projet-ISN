from math import*

################################ ATTENTION L'ANGLE DE LA FUSEE NE S'ACTUALISE PAS

class Fusee (Objet) : 
    """fusée avec caracteristiques d'un objet celeste : 
        - coordX et coordY
        - masse 
        - image
        - vitesse
        - acceleration
        - angle de rotation de l'image (en radian)
        - force de rotation (angle de rotatation à pivoter à chaque unité de temps)
        et des attributs propres :
        - tabComposants 
        et une methode pour actualiser sa masse et ses coordonnées """ 
        
    def __init__(self, coordX, coordY, imageRef): 
        """valeurs par defaut""" 
        chargeUtile = ChargeUtile()
        booster1 = Booster()
        booster2 = Booster()
        etage1 = PremierEtage()
        etage2 = DeuxiemeEtage()
        self.tabComposants = [chargeUtile,booster1,booster2,etage1,etage2]# manque la possibilite de choisir
        
        self.actualiseMasse() #pourquoi se faire chier pour un cas particulier si on peut faire le cas general :D
        self._coordX = coordX #il faut prendre en compte le rayon de la planete et la taille de la fusée
        self._coordY = coordY
        self._image = imageRef #a changer
        self._angle = pi/4 #angle initial
        

    def _set_angle(self,input):
        self._angle = input
        
    def _get_angle(self):
        return self._angle
    


    angle = property(_get_angle,_set_angle) 
    
    
    def actualise(self,vectVitesse):
        self.masse = 0 
        for k in self.tabComposants :
            k.actualise()
            self.masse = self.masse + k.masse 
            
        self.angle = vectVitesse.angle
        
        self.coordX = self.coordX + vectVitesse.normeX
        self.coordY = self.coordY + vectVitesse.normeY
