def no_more_doublon():
    L = [10,20,30,20,10,50,60,40,80,50,40]
    L2 = []
    for i in range(11):
        if i == 0:
            L2.append(L[i])
            cpt = 1
        cpt2 = 0
        for j in range(i):
            if L2[j] == L[i]:
                break
            elif L2[j] != L[i]:
                cpt2 += 1
                if cpt2 == cpt:
                    L2.append(L[i])
                    cpt += 1
    print(L,"\n",L2)
                
no_more_doublon()