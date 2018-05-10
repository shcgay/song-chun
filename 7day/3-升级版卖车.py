class suvCar(object):
	def move(self):
		print('他在奔跑')
	def stop(self):
		print('他已经停止运动')
class svvCar(object):
	def move(self):
		print('jksjg')
	def stop(self):
		print('dsayfg')
class xiandaiCarstore():
	def sta(self,typename):
		if typename == 'SUV':
			car = suvcar()
		elif typename == 'AV':
			car = svvcar()
		return car
