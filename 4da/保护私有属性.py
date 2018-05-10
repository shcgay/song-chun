class people():
    def __init__(self):
        self.__renshu = 20
    def getrenshu(self):
        return self.__renshu
    def setrenshu(self,Renshu):
        if renshu <= 0:
            print('输入有误')
        else:
            self.__renshu = Renshu
xiaoming = people()
print(xiaoming.getrenshu())
