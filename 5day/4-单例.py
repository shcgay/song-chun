class JiuMei(object):
	__instance = None
	__first_init = False
	def __new__(cls,age,name):
		if not cls.__instance:
			cls.__instance = object.__new__(cls)
		return cls.__instance
	def __init__(self,age,name):
		if not self.__first_init:
			self.age = age
			self.name = name
			JiuMei.__first_init = True
a = JiuMei(18,'九妹')
b = JiuMei(9,'九妹')
print(id(a))
print(id(b))
