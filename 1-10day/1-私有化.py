class Cat(object):
	def __init__(self,__name,_name):
		self._name = _name
		self.__name = _name
	def getName(cls):
		return self.__name
cat = Cat('小王','小李')
cat.getName()
cat._name()
