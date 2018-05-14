class  storeCar(object):
	def creatfactory(self,typeName):
		pass
	def order(self,typeName):
		return self.createfactory(typeName)
class xdstoreCar(storeCar):
	def creatfactory(self,typeName):
		return xdfactory().xuanze(typeName)
class BenstoreCar(storeCar):
	def creatfactory(self,typeName):
		return Benfactory().xuanze(typeName)
class factory(object):
	def __init__(self,name):
		self.name = name
	def xuanzeiCar(slef,typeName):
		pass
class xdfactory(factory):
	def xuanzeCar(self,typeName):

		if typeName == 0:
			return xdcar
class Benfactory(factory):
	def xuanzeCar(self,typeName):


		if typeName == 1:
			return Bencar

class Car(object):
	def move(self):
		print('正在高速移动')
	def stop(self):
		print('已经停止了')
class xdcar(Car):
	pass
class Bencar(Car):
	pass
if __name__ == '__main__':
	storeCar = BenstoreCar()
	Bencar = storeCar.xuanze(1)
	Bencar.move()
	Bencar.stop()
	
