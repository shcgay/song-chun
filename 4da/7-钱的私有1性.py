class Money():
	def __init__(self):
		self.__money = 100
	def getmoney(self):
		return self.__money
	def setmoney(self,money):
		if money < 0:
			print("输入有误")
		else:
			self.__money = money
xiaohu = Money()
print(xiaohu.getmoney())
xiaohu.setmoney(-10101010101010101010)
