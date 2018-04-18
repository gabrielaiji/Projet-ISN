from math import*

class Fusee (ObjetCeleste) :
    """fusée avec caracteristiques d'un objet celeste : 
        - coordX et coordY
        - masse 
        - image
        et des attributs propres :
        - angle
        - tabComposants 
        et une methode pour actualiser sa masse""" 
        
    def __init__(self): 
        """valeurs par defaut""" 
    
        
        
        
        chargeUtile = ChargeUtile()
        booster1 = Booster()
        booster2 = Booster()
        etage1 = PremierEtage()
        etage2 = DeuxiemeEtage()
        self.tabComposants = [chargeUtile,booster1,booster2,etage1,etage2]#manque la possibilite de choisir
        
        self.actualiseMasse() #pourquoi se faire chier pour un cas particulier si on peut faire le cas general :D
        self._coordX = 0 
        self._coordY = 6371*(10**3)
        self._image = "trollface.jpg" #a changer
        self._angle = pi/4 #angle initial
        

    def _set_angle(self,input):
        self._angle = input
        
    def _get_angle(self):
        return self._angle
    


    angle = property(_get_angle,_set_angle) 
    
    
    def actualiseMasse(self):
        self.masse = 0 
        for k in self.tabComposants :
            k.actualise()
            self.masse = self.masse + k.masse 