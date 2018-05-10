class songchunfang():
	def __init__(self,aini,aita):
		self.aini = aini
		self.aita = aita
	def play():
		print('咱们俩个一起做咱们喜欢的事,好吗')
		print('你希望和我其一是吗')
class jiajichuang():
	def __init__(self,aini,aita):
		self.aini= aini
		self.aita = aita
	def play():
		print('可以啊咱们俩一起做,啊哈哈哈,害羞')
		print('咱们俩个已经做了咱们俩那摩多自己喜欢做的事了')
class son(songchunfang,jiajichuang):
	pass
class girl(songchunfang,jiajichuang):
	pass




颜流逝 = son('爱我','爱你')
print(id('颜流逝'))
print('儿子希望咱们家人四个永远生活在一起,母亲:宋春芳')
print(颜流逝.aini,颜流逝.aita)
print('天长地久`ZZ')
梦清酒 = girl('爱他','爱她')
print(id('梦清酒'))
print('女儿希望咱们家人四个永远生活在一起,父亲:贾纪闯')
print(梦清酒.aini,梦清酒.aita)
print('天荒地老')
	
