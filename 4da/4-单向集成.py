class animal():
	def __init__(self,name):
		self.__name = name
	def getname(self):
		return self.__name
	def eat(self):
		print("吃饭")
class cat(animal):
	pass
c = animal()

xiaoming = cat()
xiaoming.eat()
