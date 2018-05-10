import time
class Cat():
	def __init__(self,age):
		self.age = 10
		self.__name = "宋"
	def getname(self):
		return self.__name
	def __del__(self):
		print("del方法执行了")
bosimao = Cat(10)
hashiqi = bosimao
jiafeimao = bosimao
print(bosimao.getname())
del bosimao
del hashiqi
del jiafeimao
print("程序将在60秒后结束")
time.sleep(60)
print("哈哈")
