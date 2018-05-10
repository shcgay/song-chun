import time
class Father():
	def eat(self):
		print("吃东西")
		time.sleep(2)
	def play(self):
		print("打飞机")
		time.sleep(10)
class Mother():
	def chao(self):
		print("总是朝我")
		time.sleep(5)
class Son(Father,Mother):
	pass
xiaoming = Son()
xiaoming.eat()
xiaoming.play()
xiaoming.chao()
time.sleep(30)
print("打飞机")
