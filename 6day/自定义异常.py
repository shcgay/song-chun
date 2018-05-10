class Show(Exception):
	def __init__(self,name,age):
		super().__init__(self)
		self.name = name
		self.age = age
def main():
	try:
		s = input('请输入')
		if len(s) == '小明':
			raise Show(len('小明'),'小明')
	except Show as ret:
		print('Show:输入的名字是%s,名字应是%s'%(ret.name,ret.age))
		print('异常信息为:',ret)
	else:
		print('没有异常')
main()
