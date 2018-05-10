class A(object):
	def __init__(self):
		print(self)
		print("这是init方法")
	def __new__(cls):
		print(cls)
		print("这是new方法")
		ret = object.__new__(cls)
		return ret
a = A()
print(a)
print(id(A))
