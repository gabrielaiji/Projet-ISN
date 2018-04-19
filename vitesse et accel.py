

class Acceleration (Vecteur) :
    
        def __ini__(self):
                gravitation = ForceGravi()
                poussee=ForcePoussee()
                frottement = Frottements()
                rotationDroite= ForcePousseeRotation()
                rotationGauche= ForcePousseeRotation()
                tabForces = [gravitation,pousee,frottement,rotationDroite,rotationGauche]
                
                self.actualise()
                
        def actualise(self,fusee,planete,vectVitesse):  #attention faut etre concentré
                
                ## d'abord on actualise toutes les forces une par une car elles ont toutes des parametres differents
                        #attention on a pas a les actualiser dans le code principal puisqu'ils s'actualisent automatiquement avec l'acceleration
                
                self.tabForces[0].actualise(fusee.masse,planete.masse,fusee.coordX,fusee.coordY,planete.coordX,planete.coordY,planete.rayon)
                
                self.tabForces[1].actualise(fusee.tabComposants,fusee.angle)
                
                self.tabForces[2].actualise(planete.rho,(sqrt((fusee.coordX-planete.coordX)**2+(fusee.coordY-planete.coordY)**2)) < planete.rayonAtmo,vectVitesse.norme,vectVitesse.angle)
                
                self.tabForces[3].actualise()
                self.tabForces[4].actualise()
                
                ## on fait la somme des projections des forces sur les deux axes 
                sommeX = 0
                sommeY = 0
                for k in self.tabForces :
                        sommeX = sommeX + k.normeX
                        sommeY = sommeY + k.normeY
                
                ## on divise par la masse pour avoir l'accélération
                
                normeX = sommeX/fusee.masse #variables de stockage car on ne souhaite pas modif les projections depuis l'exterieur
                normeY = sommeY/fusee.masse
                
                self.norme = sqrt(normeX**2 + normeY**2)
                
                self.calculAngleOriente(self.norme,normeX,normeY) #on fait confiance a cette fonction =) 
                
                
    

class Vitesse(Vecteur): 
        
        def actualise(self,vectAccel) :
                
                normeX = self.normeX + vectAccel.normeX
                normeY = self.normeY + vectAccel.normeY
                self.norme = sqrt(normeX**2 + normeY**2)
                self.calculAngleOriente(self.norme,normeX,normeY)

                
                
                
    