import time
try:
	f = open('test.txt')
	try:
		while True:
			c = f.readline()

			if len(c) == 0:
				break
			time.sleep(20)
			print(c)
	except:
		pass
	finally:
		f.close(0)
		print('关闭文件')
except:
	print('没有这个文件')
