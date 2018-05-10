import time
class animal():
	def __init__(self,name):
		print("__init__方法被调用")
		self.__name = name

	def __del__(self):
		print("__del__方法被调用")
		print("%s对象马上被嘎嘣掉.."%self.__name)
dog = animal("太低")
del dog
cat = animal("加菲猫")
cat2 = cat
cat3 = cat
print("---马上删除cat对象")
del cat
print("---马上删除cat2对象")
del cat2
print("---马上删除cat3对象")
del cat3
print("程序1分钟后结束")
time.sleep(60)
