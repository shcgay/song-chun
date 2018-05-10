#list = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,90,91]
#key = 10
#center = int(len(list)/2)

#if center in list:
 #   while True:
  #      if center > key:
   #         center = center-1
    ##    elif center < key:
      #      center = center+1
       #elif center == key:
        #    print("这个执事%d索引时%d"%(key,center))
        #    break
#else:
 #   print("没有数字")













cdd = [1,2,3,4,5,6,7,8,9,20,30,40,50,60,70]
key = 40
center = int(len(cdd)/4)
if center in cdd:
    while True:
        if center > key:
            center=center-1
        elif center < key:
            center=center+1
        elif center == key:
            print("周三%d苏饮食%d"%(key,center))
            break
else:
    print("sjzc")
