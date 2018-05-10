import time
class Game():
	def __init__(self,account,pwd):
		self.name = "宋"
		self.account = 742156464
		self.__pwd = 321654
	def getpwd(self):
		return self.__pwd
	def play(self):
		print("十步杀一人,百步不流行")
		time.sleep(3)
class jingji(Game):
	pass
	time.sleep(5)
class six():
	def __init__(self,age):
		self.age = 20
class two(six):
	pass
	time.sleep(10)
wangzhe = jingji("宋",742156464)
print(wangzhe.getpwd)
xiaoming = two(20)
time.sleep(50)
print("宋春芳")
time.sleep(45)
		

