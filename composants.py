
class Composant(): #charge utile et propulseurs
    """composant de la fusée avec comme attributs :
        - masse"""
        
    def __init__(self): 
        """valeurs par defaut"""
        self._masse = 0 

    def _get_masse(self):
        return self._masse 
    
    def _set_masse(self,newmasse):
        self._masse = newmasse

    masse = property(_get_masse, _set_masse)






class ChargeUtile(Composant): #masse invariable apres le lancement
    def __init__(self):
        self._masse = 70000
        
    def actualise(self):
        #rien a faire lol
        gabriel = 1+1


        
class Propulseur(Composant) :
    """propulseur de la fusée avec comme attributs :
        - masse
        - activité (true ou false)
        - un debit massique
        - une vitesse d'ejection
        - une reserve de carburant max (en kg) appelé reservoir
        - une quantité de carburant restant (en kg) appelé carburant
        - attache (boolean) : rattaché a la fusee ou non"""

    ## Fonctions de base
    def __init__(self): 
        """valeurs par defaut (booster)"""
        self._masse = 730*10**3 #kg c'est la masse totale en fonction du temps (contenu + contenant)
        self._activite = False #si il propulse ou non
        self._debitMass = 6040 #kg/s
        self._vitEject = 2650  # m/s 
        self._reservoir = 630*10**3  # kg masse de carburant max on peut mettre en L stv ca fait juste un calcul en plus
        self._carburant = self.reservoir # kg masse de carburant encore dans le reservoir
        self._attache = True #si le composant est toujours sur la fusee 
        
    def _get_masse(self):
        return self._masse 
    
    def _set_masse(self,newmasse):
        self._masse = newmasse
    
    def _get_activite(self):
        return self._activite
    
    def _set_activite(self,newactivite):
        self._activite = newactivite
        
    def _get_debitMass(self):
        return self._debitMass
    
    def _set_debitMass(self,newDebitMass):
        self._debitMass = newDebitMass
        
    def _get_vitEject(self):
        return self._vitEject
    
    def _set_vitEject(self,newvitEject):
        self._vitEject = newvitEject
        
    def _get_reservoir(self):
        return self._reservoir
    
    def _set_reservoir(self,newreservoir):
        self._reservoir = newreservoir
    
    def _get_carburant(self):
        return self._carburant

    def _set_carburant(self,newcarburant):
        self._carburant = newcarburant

    def _get_attache(self):
        return self._attache

    def _set_attache(self,new):
        self._attache = new
        
    
    masse = property(_get_masse, _set_masse)
    activite = property(_get_activite, _set_activite)
    debitMass = property(_get_debitMass, _set_debitMass)
    vitEject = property(_get_vitEject, _set_vitEject)
    reservoir = property(_get_reservoir, _set_reservoir)
    carburant = property(_get_carburant, _set_carburant)
    attache = property(_get_attache,_set_attache)
    
    
    ##Actualisation des variables apres 1 sec
    def actualise(self) :
        
        if self.attache :
            if self.activite and self.carburant > 0 :
                self.carburant = self.carburant-self.debitMass #on considere qu'1 sec exactement s'est ecoulé
                self.masse = self.masse - self.debitMass
        else : 
            self.masse = 0 # masse nulle si partie detachée
            
##exemples de composants tirés du CG 
#(on peut en creer d'autres directement a partir de la classe Propulseur()
        
class Booster(Propulseur):
    def __init__(self): 
        """valeurs par defaut (booster)"""
        self._masse = 730*10**3 #kg
        self._activite = False
        self._debitMass = 6040 #kg/s
        self._vitEject = 2650  # m/s
        self._reservoir = 630*10**3  # kg
        self._carburant = self.reservoir # kg
        self._attache = True
        
class PremierEtage(Propulseur):
    def __init__(self): 
        """valeurs par defaut (1er etage)"""
        self._masse = 1100000 #kg
        self._activite = False
        self._debitMass = 1.97*10**3 #kg/s
        self._vitEject = 3.53*10**3  # m/s
        self._reservoir = 980000  # kg
        self._carburant = self.reservoir # kg
        self._attache = True
        
class DeuxiemeEtage(Propulseur):
    def __init__(self): 
        """valeurs par defaut (2e etage)"""
        self._masse = 31000 #kg
        self._activite = False
        self._debitMass = 24 #kg/s
        self._vitEject = 4513  # m/s
        self._reservoir = 27000  # kg
        self._carburant = self.reservoir # kg
        self._attache = True
    
    
    
    
    
    
    
    
    
    
    