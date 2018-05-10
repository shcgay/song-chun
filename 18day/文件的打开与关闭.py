with open('1.txt','w') as f:
    f.write("回家等你,等我额")
with open('2.txt','w') as f:
    f.write('好啊')
    f.write('等你额')
    f.write('一定要来啊')






with open('2.txt','r') as f:
    conent = f.readline()
    print('1:%s'%conent)
#    conent = f.readline()
 #  print('2:%s'%conent)
  #  conent = f.readlines()
    #print('0::%s'%conent)
