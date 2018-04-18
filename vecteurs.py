


from math import* 


class Vecteur :
    """vecteur def par :
        -norme (normeX et normeY)
        -angle par rapport a l'horizontal dans le sens trigo"""
        
    
    def __init__(self):
        """valeurs par defauts"""
        
        
        self._normeX = 0 
        self._normeY = 0 
        self._norme = 0 
        self._angle = 0 #angle par rapport a l'axe x sens trigo le sens est donné par le cos ou sin + ou - 
        

    def _get_normeX(self):
        return self._normeX
        
    def _set_normeX(self,new): 
        self._normeX = new
        
    def _get_normeY(self):
        return self._normeY

    def _set_normeY(self,new): 
        self._normeY = new
    
    def _get_norme(self):
        return self._norme
    
    def _set_norme(self,new):
        self._norme = new 
        self._normeX = new * cos(self.angle)
        self._normeY = new * sin(self.angle)
    
    def _get_angle(self):
        return self._angle

    def _set_angle(self,new): #si on change l'angle la norme reste constante
        self._angle = new 
        self._normeX = self.norme * cos(new)
        self._normeY = self.norme * sin(new)
        
    angle = property(_get_angle,_set_angle)
    normeX = property(_get_normeX,_set_normeX)
    normeY = property(_get_normeY,_set_normeY)
    norme = property(_get_norme,_set_norme)
    
    def setNormeAndAngle(self, newNorme, newAngle) :
        self._angle = newAngle
        self._norme = newNorme
        self._normeX = self.norme * cos(self.angle)
        self._normeY = self.norme * sin(self.angle)
            


    
    
    
    
    
    
    
    