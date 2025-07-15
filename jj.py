'''donenne_list= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,19,20]
filtre = [n for n in donenne_list if  n % 3 == 0]
don=[n**3  for n in filtre ]
print(don)'''



'''while True:
    try:
        tu_entre=int(input("entre un nomble premie nombles"))
        tu_entre1=int(input("entre le nomble deux"))
        ok=tu_entre/tu_entre1
        print(ok)
        break
    except ValueError:
       
        print("Erreur :  nomble n entre est pas correct recommense ")   
    except ZeroDivisionError:
        print("il n es pas divisible pas zero")
        break'''
'''def args(ok):
    print("ok")
def kawags(mutiplicateur=1):
    print("ok")
def somme_positifs():
    def Parametre_non_nome(n1):
        f
    def parametre_optionnel(mutiplicateur=1):
        f
    def variable_posible(posible=[]):
        f
    def variable_nommes(v1=1,v2=3,v3=20):'''

''' 
with open("tre.txt","w")as fichier:
    fichier.write("1 , ")
     #mon aisser
with open ("tre.txt","r") as fichier:
    dosie=fichier.read()
    print(dosie) '''


mon_texte="bien bien je suis ravis je suis  bien et toi tu es bien ravis pas possible"
compteur_ok={}
for mots in mon_texte.split():
    if mots in compteur_ok:
        compteur_ok[mots]+=1
    else:
        compteur_ok[mots]=1
print("frequence des mots")        
for mots ,frequante in compteur_ok.items():
    print(f"{mots} frequente {frequante} foix")
unique=set(mon_texte.split())
print("\n les mots unique ")
for mots in unique:
    print(mots)
    
       
        
    

    

        



      
      
    

  
            
        
       
     
    