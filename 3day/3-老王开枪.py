class person():v
    def __init__(self,name):
        self.name = name
        self.hp = 100
    def addzhuangzidan(self,danjia,zidan):
        danjia.addZidan(zidan)
    def addzhuangdanjia(self,gun,danjia):
        gun.addDanjia(danjia)
    def takegun(self,gun):
        self.gun = gun
    def opengun(self,diren):
        if diren.hp > 0:
            zidan = self.gun.pop.GunZidan()
            if zidan:
                zidan.kill(diren)
            else:
                print('没子弹了')


class Gun():
    def __init__(self,name):
        self.name = name
        self.danjia = None
    def addDanjia(self,danjia)
        self.danjia = danjia
    def popGunZidan(self,danjia):
        return self.danjia.popZidan


class Danjia():
    def __init__(self,size):
        self.size = size
        self.zidan_list = []
    def addZidan(self,zidan)
        self.zidan_list.append(zidan)
        print(len(sel.zidan_list))
    def popZidan(self):
        return self.zidan_list.pop()


class Zidan():
    def __init__(self):
        self.weili = 5
    def kill(self,diren):
        diren.hp -= self.weili
        print('生育谢亮%d'%diren.hp)









laowang = person('老王')
m416 = Gun(m416)
danjia =  Danjia(20)
for i in range(10):
    zidan = Zidan()
laowang.zhuangzidan(danjia,zidan)
laowang.zhuangdanjia(m416,danjia)
laosong = person('老宋')
laowang.takegun(m416)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
