class Mywrod(object):
	__instance = None
	__inited = None
	def __new__(cls,sing,song):
		if cls.__instance is None:
			cls.__instance = object.__new__(cls)
		return cls.__instance
	def __init__(self,sing1,sing2):
		if self.__inited is None:
			self.sing1 = sing1
			self.sing2 = sing2
			Mywrod.__inited = True
s1 = Mywrod('first',1)
s2 = Mywrod('second',2)
print(id(s1))
print(s1.sing1,s1.sing2)	
print(id(s2))
print(s2.sing1,s2.sing2)

