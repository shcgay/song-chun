class my(object):
	__instance = None
	__inited = None
	def __new__(cls,sing,song):
		if cls.__instance is None:
			cls.__instance = object.__new__(cls)
		return cls.__instance
	def __init__(self,sing1,song2):
		if self.__inited is None:
			self.sing1 = sing1
			self.song2 = song2
		my.__inited = True
s1 = my('first',1)
s2 = my('sconed',2)
print(id(s1))
print(s1.sing1,s2.song2)
print(id(s2))
print(s2.sing1,s2.song2)
		
