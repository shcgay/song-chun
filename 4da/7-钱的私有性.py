class Money():
	def __init__(self):
		self.__money = 100
	def setmoney(self,money):
		if money<=0:
			print("传输有误")
		else:
			self.__money = money
	def getmoney(self):
		return self.__money
money = Money()
print(money.getmoney())
money.setmoney(30)
