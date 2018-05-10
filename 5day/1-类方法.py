class people():
	c = 'china'
	@classmethod
	def getC(cls):
		return cls.c
	def setC(cls,c):
		cls.c = c
p = people()
print(p.getC())
print(people.getC())
print(id(p.getC()))
p.setC('japan')
print(p.getC())
print(people.getC())

