


from math import*

class ObjetCeleste:
    """tout objet dans l'espace avec :
        - coordX et coordY
        - masse 
        - vitesse 
        - image """
    
    
    
    def __init__(self): 
        """valeurs par defaut"""
    
        self._coordX = 0 
        self._coordY = 0 
        self._masse = 0 
        self._image = "trollface.jpg" #a changer
    
    
    
    
    def _get_coordX(self):
        return self._coordX
    
    def _set_coordX(self,newcoordX):
        self._coordX = newcoordX
        
    def _get_coordY(self):
        return self._coordY
    
    def _set_coordY(self,newcoordY):
        self._coordY = newcoordY
        
    def _get_masse(self):
        return self._masse 
    
    def _set_masse(self,newmasse):
        self._masse = newmasse
    
    def _set_image(self,pathFichier):
        self._image = pathFichier 
        
    def _get_image(self) :
        return self._image
    
    coordX = property(_get_coordX,_set_coordX)
    coordY = property(_get_coordY,_set_coordY)
    masse = property(_get_masse, _set_masse)
    image = property(_get_image,_set_image)








