class Game():
	def __init__(self):
		self.__pwd = 123
	def __str__(self):
		msg = "密码是%d"%self.__pwd
		return msg
	def getpwd(self):
		return self.__pwd
	def setpwd(self,pwd):
		if pwd > 3:
			print("输入错误")
		else:
			self.__pwd = pwd
xiaoming = Game()
xiaoming.setpwd(123)
print(xiaoming.getpwd())

