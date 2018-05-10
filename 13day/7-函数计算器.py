#for i in range(1,10):
 #   for j in range(1,i+1):
  #      print("%d*%d=%d\t"%(i,j,j*i),end = "")
   # print("")












for i in range(100,201):
    flag = 0
    for j in range(100,i):
        if i%j == 0:
            flag = 1
            break
    if flag == 0:
        print(i)
