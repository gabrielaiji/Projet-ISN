from math import*


class ForceGravi (Vecteur) :
    

        
    def actualise(self,masseFus,massePlanete,xfus,yfus,xplanete,yplanete,rayonDeLaPlanete):
        if sqrt((xfus-xplanete)**2+(yfus-yplanete)**2) < 50 +rayonDeLaPlanete : #si la distance < 50 alors fusée posée sur la terre donc reaction normale de meme norme que la force de gravit
            self.norme = 0
        else :
            self.norme = masseFus*massePlanete*6.67e-11/sqrt((xfus-xplanete)**2+(yfus-yplanete)**2)
        
        
        self.calculAngleOriente(self.norme,xfus-xplanete,yfus-yplanete) #on a donné la bonne direction mais le vecteur est orienté vers la fusée 
        
        self.angle = (self.angle + pi) %(2*pi) #pour avoir le bon sens








class ForcePoussee(Vecteur):
    def actualise(self,tabComposantsDeLaFusee,angleFusee):  #attention au parametre
        self._norme = 0 
        for k in tabComposantsDeLaFusee:
            if k.activite:
                self._norme = self._norme + k.debitMass * k.vitEject
        self.angle = (angleFusee + pi) % (2*pi)
    
    

class Frottements(Vecteur):
    def actualise(self,rho,atmosphere,normeVitFus,angleVitFus): #atmosphere est un boolen qui n'est pas encore défini
        if atmosphere :
            self._angle = (angleVitFus + pi) % (2*pi)
            self._norme = rho * 0.2 * 10 * normeVitFus**2 #rho*Cx.S.V**2 et rho air = 1.225 kg/m³      on admet Cx = 0.2 
            
        else : 
            self._angle = 0
            self._norme = 0

class ForcePousseeRotation(Vecteur):
    
    def _init_(self):
        self._actif = false
    
    def _get_actif(self):
        return self._actif
    
    def _set_actif(self,new):
        self._actif = new 
    
    actif = property(_get_actif,_set_actif)
    

    def actualise(self):
        if self.actif:
            self.norme = 10**4 #valeur arbitraire plus c'est grand plus c'est facile de tourner
        else :
            self.norme = 0 
        