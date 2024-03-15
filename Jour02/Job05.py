def Inverse(mot):
    a = ""
    for i in range(1,len(mot)+1):
        a += mot[-i]
        ## print(a)
    return a

print(Inverse("nikana"))
print(Inverse("je suis un crack"))
print(Inverse(input("Met un mot ")))