import time
try:
	print(1)
	time.sleep(2)
	raise ValueError(123)
	print(2)
except ValueError:
	print(3)
	time.sleep(3)
except Exception as ret:
	print(4)
	print('异常信息为:',ret)
else:
	print(5)
finally:
	print(6)
	time.sleep(4.5)
	print('宋春芳我等了你那莫久,你也等了我那莫久,但是咱们总是错过')
