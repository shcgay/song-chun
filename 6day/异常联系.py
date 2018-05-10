try:
	print('num')
	#print(num)
	print(123456)
#except NameError:
	#print('产生错误')
except Exception as ret:
	print('不活了很多一场')
	print('异常信息为:',ret)
else:
	print('没有异常真他妈殆尽')
