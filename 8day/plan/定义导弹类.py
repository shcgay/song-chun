class Bullet(object):
	def __init__(self,planeName,x,y):
		if planeName == 'enemy':
			self.imageName = 'Resources/bullet-3.png'
			self.direction = 'down'
		elif planeName == 'hero':
			self.imageName = 'Resources/bullet-1.png'
			self.sirection = 'up'
		#pygame框架加载图片为图像函数为:
		self.image = pygame.image.load(self.imageName).convert()
		self.x = x
		self.y = y
	#描绘出导弹的位置
	def draw(self,screen):
		if self.direction == 'down'
			self.y+=1
		elif self.direction == 'up'
			self.y-=1
		screen.blit(self.image,(self.x,self.y))
#定义一个飞机积累
class Plane(object):
	def __init__(self):
		self.bulletSleepTime = 0.2
		self.lastShootTime = time.time()
		self.bulletList = []
	def shoot(self):
		if time.time()-self.lastShootTime>self.bulletSleepTime:
			self.bulletList.append(Bullet(self.planeName,self.x+36,self.u))
			self.lastShootTime = time.time()
	def draw(self,screen):
		screen.blit(self.image,(self.x,self.y))
#完架飞机类，集成鸡肋
class Hero(Plane):
	def __init__(self):
		Plane.__init__(self):
		planeImageName = 'Resources/hero.png'
		self.image = pygame.image,load(planeImageName).convert()
		self.x = 200
		self.y = 600
		self.planeName = 'hero'
#键盘控制自己的飞机
	def keyHandle(self,keyValue):
		if keyValue == 'left':
			self.x -= 50
		elif keyValue == 'right':
			self.x += 50
		elif keyValue == 'up':
			self.y -=50
		elif keyValue == 'down':
			self.y +=50
#定义敌人费自己累
class Enemy(Plane):
	def __init__(self,speed):
		super(Enemy,self).__init__()
		randomImageNum = random.randint(1,3)
		planeImageNum = 'Resources/enemy-' + str(randomImageNum) + '.png'
		self.image = pygame.image.load(planeImageName).convert()
		#敌人飞机原始位置
		self.x = random.randint(20,400)
		self.y = 0
		self.palneName = 'enemy'
		self.direction = 'down'
		self.speed = speed
	def move(self):
		if self.direction == 'down':
			self.y += self.speed
g_ememyList = []
score = 0
hero = object
@classmethod
def createEnemy(cls,speed):
	cls.g_emenyList.append(Enemy(speed))
@classmethod
def createHero(cls):
	cls.hero = Hero()
@classmethod
def gameInit(cls):
	cls.createHero()
@classmethod
def herolaneKey(cls,keyValue):
	cls.hero.keyHandle(keyValue)
@classmethod
def setXY(cls):
	for i in cls.g_ememyList:
		i.move
@classmethod
def draw(cls,screen):
	delPlaneList = []
	j = 0
	for i in cls.g_ememyList:
		i.draw(screen)
		if i.y > 680:
			delPlaneList.append(j)
		i+=1
	for m in delPlaneList:
		del cls.g_ememyList[m]
	delBulletList = []
	i = 0
	cls.hero.draw(screen)
	for i in cls.hero.bulletList:
		i.draw(screen)
		if i.y < 0:
			delBulletList.append(j)
		i += 1
	for m in delBulletList:
		del cls.hero.bulletList[m]
@classmethod
def shoot(cls):
	cls.hero.shoot()
	ememyIndex = 0
	for i in cls.g_ememyList:
		enemyRect = pygame.Rect(i.image.get_rect())
		enemyRect.left = i.x
		enemyRect.top = i.y
		bulletIdex = 0
		for j in cls.hero.bulletList:
			bulletRect = pygame.Rect(j.image.get_rect())
			bulletRect.left = j.x
			bulletRect.top = j.y
			if enemyRect.colliderect(bulletRect):
				if enemyRect.width == 39:
					cls.scroe += 1000
				elif enemyRect.width == 60:
					cls.scroe += 5000
				elif enemyRect.width == 78:
					cls.scroe += 10000
				cls.g_ememyList.pop(ememyIndex)
				cls.hero.bulletList.pop(bulletIndex)
			bulletIndex += 1
		ememyIndex += 1
@classmethod
def gameover(cls):
	heroRect = pygame.Rect(cls.hero.image.get_rect())
	heroRect.left = cls.hero.x0
	heroRect.top = cls.hero.y
	for i in cls.g_ememyList:
		enemyRect = pygame.Rect(i.image.get_rect())
		enemyRect.left = i.x
		enemmyRect.top = i.y
		if heroRect.colliderect(enemyRect):
			return True
		return False
@staticmethod
def pause(syrface,image):
	surface.blit(image,(0,0))
	pygame.display.update(0
	while True:
		for event in pygame.event.get():
			if evnet.type == pygame.QUIT
				cls.terminate()
			elif event.type == pygame.KEYDOWN:
				if event.key == K_SPACE:
					return
@staticmethod
def drawText(text,font,surface,x,y):
	content  = font.render(text,False,(10,100,200))
	content = content.get_rect()
	content_Rect.left = x
	content_Rect.top = y
	surface.blit(content,contentRect)
