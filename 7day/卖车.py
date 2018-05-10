class Car(object):
	def move(self):
		print("他在奔跑")
	def stop(self):
		print("他停止了")
class Carstore(object):
	def order(self):

		self.car = Car
		self.move = move
		self.stop = stop
xiandai = Car()
xiandai.move()
xiandai.stop()
