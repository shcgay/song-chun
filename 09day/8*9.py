i=1
while i <=9:
    j=1
    while j <=i:
    #1*1=1
        print("%d*%d=%d" %(j,i,j*i),end="")
        j+=1
    print("")

    i+=1





i = int(input("请输入数字"))
n = 1
while n <= i:
    print(""*(i-n)),end = "")
    j = 1
    while j <= n:
        print("*",end = "")
        j += 1
    print("")
    n += 1
