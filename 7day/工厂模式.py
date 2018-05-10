def factory(aCalss,*args,**kargs):
		eturn aCalss(*args,**kargs)
class Apple:
	def __init__(self,weight,color = 'red',sweet = True):
		self.weight = weight
		self.color = color
		self.sweet = sweet
class Person:
	def __init__(self,name = 'rose',age = '12'):
		self.name = name
		self.age = age
a = factory(Apple,1.5,sweet = False,color = 'green')
p = factory(Person,'rose',24)
print(a,p)
