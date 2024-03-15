print("2")
for i in range(1000):
    j = 2
    while j < i+1 and i%j != 0:
        j += 1
        if j == i:
            print(i)