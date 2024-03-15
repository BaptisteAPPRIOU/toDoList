def my_sort(L):
    cpt = 0
    for j in range(len(L)):
        for k in range(0,len(L)-1):
            if L[k] > L[k+1]:
                a = L[k]
                L[k] = L[k+1]
                L[k+1] = a
                cpt += 1
                print(L)
    print("Nombre total de coups nécessaires pour trier la liste : ",cpt)
    print("Liste triée : ",L)
    
LISTE = [12,45,26,1,4,89,0,7,96,88]
my_sort(LISTE)