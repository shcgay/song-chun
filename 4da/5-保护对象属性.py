class Dog():
	def __init__(self,age):
		self.age =age
	def walk(self):
		print("汪汪叫")
	def __str__(self):
		return "够的年龄是%d"%self.age
xiaoming = Dog(10)
print(xiaoming)
xiaoming.walk()
