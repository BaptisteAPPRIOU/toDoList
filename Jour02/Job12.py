def draw_rectangle(width,height):
    for i in range(width):
        print("-",end="")
    print("\n")
    for j in range(height):
        print("|",end="")
        for k in range(width-2):
            print(" ",end="")
        print("|",end="")
        print("\n")
    for i in range(width):
        print("-",end="")
        
draw_rectangle(10,3)