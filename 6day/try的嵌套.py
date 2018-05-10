def test():
	print('num')
	print(num)
	print('halou')
def test2():
	print('hahah')
	test()
	print('dhdhdh')
def test3():
	try:
		print('adsa')
		test()
		print('jhsagj')
	except Exception as ret:
		print('异常信息为:%s'%ret)
	print('jhsagi')
test3()
print('******')
test2()
