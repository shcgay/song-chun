def cfkb(x,y):
    for i in range(x,y):
        for j in range(x,i+1):
            print("%d*%d=%d\t"%(i,j,i*j),end = "")
        print(" ")
cfkb(1,99)
