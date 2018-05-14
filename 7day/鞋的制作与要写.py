import time
class shose:
	def walk(self):
		pass
class pixie(shose):
	def walk(self):
		print("正在享受脚气")
class qiuxie(shose):
	def walk(self):
		print("正在践踏草坪")
class shoseFactory():
	def make_shose(self):
		pass
class pixieshoseFactory(shoseFactory):
	def make_shose(self):
		return pixie()
class qiuxieshoseFactory(shoseFactory):
	def make_shose(self):
		return qiuxie()
class shoseFactory():
	def make_shose(self,name):
		if name == "qiuxie":
			return qiuxie()
		elif name == "pixie":
			return pixie()
		else:
			None
def anli_call():
	factory = shoseFactory()
	for i in range(4):
		time.sleep(5)
		shose = factory.make_shose("qiuxie")
		shose.walk()
def hengda_call():
	factory = shoseFactory()
	for i in range(3):
		time.sleep(2)
		shose = factory.make_shose("pixie")
		shose.walk()
if __name__ == "__main__":
	anli_call()
	hengda_call()
