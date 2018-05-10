class home():
    def __init__(self,area,address,price):
        self.area = area
        self.address = address
        self.price = price
        self.jiaju = []
    




    def __str__(self):
        msg = "房子的面积是%d地址是%s价格是%s"%(self.area,self.address,self.price)
        return msg
    def addbed(self,bed):
        if self.area >= bed.getarea:
            self.jiaju.append(bed)
            self.area-=bed.getarea()
            print("加入成功")
            print(self.area)
        else:
            print("加入失败")

class bed():
    def __init__(self,name,area):
        self.name = name
        self.area = area





    def __str__(self):
        msg = "床的名字是%s面积是%d"%(self.name,self.area)
        return msg
    def getarea(self):
        return self.area

myhome = home(130,"我的中心",2400)
print(myhome)
jiamengde = bed("架梦德",5)
print(jiamengde)
myhome.addbed(jiamengde)


