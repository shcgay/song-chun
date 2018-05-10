class person():
    def __init__(self,name):
        self.name = name
        self.gun = None
        self.hp = 100
    def zhuangzidan(self,danjia,zidan.):
        danjia.addzidan(zidan.)
    def zhuangdanjia(self,gun,danjia):
        gun.addDanjia(danjia)
    def takegun(self,gun):
        self.gun = gun
    def opengun(self,diren):
        if diren.hp >0:
             zidan = self.gun.popGunzidan()
             if zidan:
                 zidan.kill(diren)
             else:
                 print('没子弹了')





class Gun():
    def __init__(self,name):
        self.name = name
        self.danjia = None
    def addDanjia(self,danjia):
        self.danjia = danjia
        print(id(self.danjia))
    def popGunzidan(self):
        return self.danjia.popzidan()






class Danjia():
    def __init__(self,size):
        self.sizen = size
        self.zidan._list = []
    def addzidan(self,zidan.):
        self.zidan._list.append(zidan.)
        print(len(zidan._list))
    def popzidan(self):
        return self.zidan_list.pop()








class zidan():



laowang = person('老王')
m416 = Gun('m416')
danjia = Danjia(20)
for i in range(20):
    zidan. = zidan()
    laowang.zhuangzidan(danjia.zidan.)
laowang.zhuangdanjia(m416.danjia)
laosong = person('老宋')
laowang.takegun(m416)
laowang.opengun(laosong 
