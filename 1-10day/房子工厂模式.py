class store (object):
	def createFactory(self,type):
		pass
	def order(self,type):
		return self.createFactory(type)
class BigHousestore(store):
	def createFactory(self,type):
		return BigHouseFactory().selectHouse(type)
class SmallHousestore(store):
	def createFactory(self,type):
		return SmallHouseFactory().selectHouse(type)
class Factory(object):
	def __init__(self,name):
		self.name = name
	def select(self,type):
		pass
class BigHouseFactory(Factory):
	def select(self,type):
		if type == 1:
			return BigHouse()
class SmallHouseFactory(Factory):
	def select(self,type):
		if type == 2:
			return SmallHouse()





class House(object):
	def zhu(self):
		print('主人朱进来了')
	def li(self):
		print('主人搬走了')
class BigHouse(House):
	pass
class SmallHouse(House):
	pass
if __name__ == '__main__':
	store = BigHousestore()
	bigHouse = store.select(1)
	bigHouse.move()
	bigHouse.stop()
