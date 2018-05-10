import time
class wucan():
	def __init__(self,name):
		self.__name = name
	def getwucan(self):
		return self.__name
	def __del__(self):
		print("%s对象马上被干掉.."%self.__name)
yxrs = wucan("鱼香肉丝")
del yxrs
dpj = wucan("大盘鸡")
dpj2 = dpj
dpj3 = dpj
print("---马上删除dpj对象")
del dpj
print("---马上删除dpj对象")
del dpj2
print("---马上删除dpj对象")
del dpj3
print("程序会在60秒后结束")
time.sleep(60)
