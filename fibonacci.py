############################################################

a = 0 # Valeure Initiale 1 
b = 1 # Valeure Initiale 2 
num = int(input("Entrer une valeure de répétition:")) # Indiquer le nombre de valeures que l'on veut avoir en sortie 

############################################################

print("Voici la Suite de Fibonacci ! ")

############################################################

for i in range (num): # Nombre de répétitions de la fonction = num 
    
    c = a + b # 3ème Nombre = Somme des deux précédents 
    
    
    print(c ,end=' ') # Print le nombre de la suite 
    a,b = b, c # Pour continuer la fonction on remplace les fonctions 
    

############################################################
