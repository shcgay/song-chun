class boy():
    def __init__(self,age,color):
        self.game = []
        self.color = color
        self.age = age
    def study(self):
        print('学习')
    def play(self):
        print('玩')
    def showage(self):
        print('年龄是%d'%self.age)
    def shoegame(self):
        for i in self.game:
            print(i)
tom = boy(52,'黑色')
tom.study()
tom.play()
tom.showgame('吃鸡')



