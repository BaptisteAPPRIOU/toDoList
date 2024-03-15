nom = "épée"
prix = 10
float(prix)
stock = 100
print ("L'objet vendu est : ",nom,". \nSon prix est de ",prix," pièces. \nIl y en a ",stock," en stock.\n")
stock += 20
achat = int(input("Combien d'épées voulez-vous acheter ?"))
stock -= achat
prix = prix * 1.1
print ("L'objet vendu est : ",nom,". \nSon prix est de ",str(prix)," pièces. \nIl y en a ",stock," en stock.\n")