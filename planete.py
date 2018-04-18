    
class Planete (ObjetCeleste):
    """planete avec caracteristiques d'un objet celeste : 
        - coordX et coordY
        - masse 
        - image
        et des attributs propres :
        - un rayon
        - rayon de l'atmosphere
        - masse volumique de l'air """ 
        

    def __init__(self): 
        """valeurs par defaut (de la Terre)""" 
    
        self._coordX = 0 
        self._coordY = 0 
        self._masse = 5.972 * (10**24) 
        self._image = "trollface.jpg" #a changer
        self._rayon = 6371*(10**3)
        self._rayonAtmo =  50000 #99.9% de l'atmo a 50 km 
        self._rho = 1.22550
        
    def _get_rayon(self):
        return self._rayon
    
    def _set_rayon(self,newrayon):
        self._rayon = newrayon
        
    def _get_rayonAtmo(self):
        return self._rayonAtmo
    
    def _set_rayonAtmo(self,newrayonAtmo):
        self._rayonAtmo = newrayonAtmo
        
    def _get_rho(self):
        return self._rho
    
    def _set_rho(self,newrho):
        self._rho = newrho 
        

    rayon = property(_get_rayon,_set_rayon)
    rayonAtmo = property(_get_rayonAtmo,_set_rayonAtmo)
    rho = property(_get_rho, _set_rho)