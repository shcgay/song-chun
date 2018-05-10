class account():
	def __init__(self,pwd):
		self.__pwd = 1
	def setpwd(self,pwd):
		if pwd <0:
			print("输入有误")
		else:
			self.__pwd = pwd
	def getpwd(self):
		return self.__pwd
	def __str__(self):
		return "密码是%d"%self.__pwd
xiaoming = account(-1)
xiaoming.setpwd(-1)

print(xiaoming)
print(xiaoming.getpwd())
