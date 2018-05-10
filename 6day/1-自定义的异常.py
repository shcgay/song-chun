class six(Exception):
	def __init__(self,two):
		self.two = two
	def three(self,s,y):
		try:
			return s/y
		except Exception as ret:
			if self.two:
				print('dsfs')
				print(ret)
			else:
				raise
s = six(True)
s.three(1,0)
print('--------------g---------------')
s.two = False
s.three(1,0)

