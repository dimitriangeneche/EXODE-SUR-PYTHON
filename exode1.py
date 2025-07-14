import math

class couleur:
    def __init__(self,nom_couleur,code_hexadecimal):
        self.nom_couleur=nom_couleur
        self.code_hexadecimal=code_hexadecimal
    def information_couleur(self):
        print(f"j ais une couleur :{self.nom_couleur} avec un code hexadecimal :{self.code_hexadecimal}")
        #text de ma fonction.
couleur1=couleur("blak","#fffff")
couleur1.information_couleur()
class figure:
    def __init__(self,couleur_figure,nom_figure):
        self.couleur_figure=couleur_figure
        self.nom_figure=nom_figure
    def information_figure(self):
        print(f"j ais une figure de couleur : {self.couleur_figure} et de nom :{self.nom_figure}")
        #text de ma fonction 
figure1=figure("blak","carre")
figure1.information_figure()
class cercle(figure):
    def __init__(self, couleur_figure, nom_figure,couleur_du_cercle,rayon_cercle):
        super().__init__(couleur_figure, nom_figure)
        self.couleur_du_cercle=couleur_du_cercle
        self.rayon_cercle=rayon_cercle
    def aire_cercle(self):
        print(f" mon cerle as une couleur :{self.couleur_du_cercle} et l aire est :{math.pi*self.rayon_cercle**2}")
    def perimetre_cercle(self):
        print(math.pi*2*(self.rayon_cercle))  
        #text de m as fonccion


class rectangle(figure):
    def __init__(self, couleur_figure, nom_figure,couleur_du_rectangle,longleur_rectangle,hauteur_rectangle):
        super().__init__(couleur_figure, nom_figure)
        self.couleur_du_rectangle=couleur_du_rectangle
        self.longleur_rectangle=longleur_rectangle
        self.hauteur_rectangle=hauteur_rectangle
    def aire(self):
        print((self.longleur_rectangle*self.hauteur_rectangle))
    def perimetre(self):
        print((self.longleur_rectangle*self.hauteur_rectangle)*2)
class triangle(figure):
    def __init__(self, couleur_figure, nom_figure,couleur_du_triangle,base_triangle,hauteur_triangle):
        super().__init__(couleur_figure, nom_figure)
        self.couleur_du_triangle=couleur_du_triangle
        self.base_triangle=base_triangle
        self.hauteur_triangle=hauteur_triangle
    def aire(self):
            print(0.5*(self.base_triangle*self.hauteur_triangle))
    def perimetre(self):
        print (math.sqrt(((self.base_triangle**2)+(self.hauteur_triangle**2))+self.base_triangle+self.hauteur_triangle))

   
    
   

        

        