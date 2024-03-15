def Arrondi():
    L = [22.4,4.0,16.22,9.10,11.00,12.22,14.20,5.20,17.50]
    print(L)
    for i in range(9):
        L[i] = int(L[i])
    print(L)
    for j in range(9):
        for k in range(j,8):
            if L[j] > L[k+1]:
                a = L[j]
                L[j] = L[k+1]
                L[k+1] = a
    print(L)
    
Arrondi()