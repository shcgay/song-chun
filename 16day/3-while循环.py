#count = 1
#sum = 0
#while count <11:
 #   sum = sum + count
  #  print("sum = %d,count = %d"%(sum,count))
   # count = count+1
#print("循环结束后的count = %d"%count)
count = int(input("请输入一个胡子"))

i = 0
d = 0
c = 0
a = 0

while i <999999999999999999999999999999:
    print("当前熟悉:%d"%i)
    i+=1
    if i%2 == 0:
        d = d+i
    elif i%2 != 0:
        c = c+i
    
print("偶数合适%d"%d)
print("技术合适%d"%c)
print("综合无%d"%(d+c))


    
