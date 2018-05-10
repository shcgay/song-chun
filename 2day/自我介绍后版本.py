class cat():
    def play(self):
        print("捉老鼠")
    def sleep(self):
        print("喵喵喵")
    def iins(self):
        print("我的名字叫%s\t\n年龄是%d\t\n喜欢的颜色是%s\t\n"%(self.name,self.age,self.color))
tom = cat()
tom.play()
tom.sleep()
tom.color = "黑色"
tom.name = "汤姆"
tom.age = 12
tom.iins()

