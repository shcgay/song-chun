class people():
	def __init__(self):
		self.name = '宋'
	@classmethod
	def person(cls):
		print('这有许多人')
	@classmethod
	def getsix(cls):
		return cls.six
china = people()
print('这有许多中国人')

print(people.getsix)

