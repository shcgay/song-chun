class Father(object):
	def __init__(self,name,age):
		self.name = name
		self.age = age
	def play():
		print('会跑')	
	def __str__(self):
		msg = '名字是%s\n年龄是%d'%(self.name,self.age)
		return msg
class Mother(object):
	instance = None
	def __new__(cls,name,age):
		if cls.instance == None:
			cls.instance = object.__new__(cls)
			return cls.instance
	def __init__(self,song,move):
		self.song = song
		self.move = move
class Son(Father,Mother):
	pass
s1 = Father('老命',45)



son = Son()
print(id(son))
print(son.name,son.age)

