import pygame
import random

SCREEN_RECT = pygame.Rect(0,0,1000,626)
CREATE_ENEMY = pygame.USEREVENT
HREO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprites(pygame.sprite.Sprite):
	def __init__(self, image_name, speed=1):
		super().__init__()
		self.image = pygame.image.load(image_name)
		self.rect = self.image.get_rect()
		self.speed = speed

	def update(self):
		self.rect.x += self.speed

#背景类
class Background(GameSprites):
	def __init__(self,is_alt=False):
		image_name = "./images/meitu.png_"
		super().__init__(image_name)
		if is_alt:
			self.rect.right = 0

	def update(self):
		super().update()
		if self.rect.right < 0 :
			self.rect.right= self.rect.width


#飞机类
class Hero(GameSprites):
	def __init__(self):
		image_name = "./images/32ce7ee507daf21ea59f61dd10a430fe_meitu_1.png" 
		super().__init__(image_name)
		self.rect.centerx = SCREEN_RECT.centerx + 240
		self.rect.bottom = SCREEN_RECT.bottom -300
		#self.hero2.rect.centerx = self.hero.rect.centerx - 100
		self.speed1 =0
		#创建子弹精灵组
		self.bullet_group = pygame.sprite.Group()
		self.speed = 0
	def update(self):

		#飞机移动水平
		self.rect.x += self.speed
		self.rect.y += self.speed1
		#判断英雄边界
		if self.rect.bottom <= SCREEN_RECT.y:
			self.rect.y = SCREEN_RECT.bottom
		elif self.rect.y >= SCREEN_RECT.height:
		 	self.rect.y= -self.rect.height
		elif self.rect.left <= 0:
			self.rect.left = 0
		elif self.rect.right >=SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right

	def fire(self):
		for i in range(1,4):
			self.bullet = Bullet()
			#设置精灵位置
			self.bullet.rect.left = self.rect.left -15*i
			self.bullet.rect.centery= self.rect.centery
			
			#将精灵添加到精灵组
			self.bullet_group.add(self.bullet)

class Hero2(GameSprites):
	def __init__(self):
		image_name = "./images/32ce7ee507daf21ea59f61dd10a430fe_meitu_1.png" 
		super().__init__(image_name)
		self.rect.centerx = SCREEN_RECT.centerx +330
		self.rect.bottom = SCREEN_RECT.bottom - 400
		self.speed2 =0
		#创建子弹精灵组
		self.bullet2_group = pygame.sprite.Group()
		self.speed = 0
	def update(self):
		#飞机移动水平
		self.rect.x += self.speed
		self.rect.y += self.speed2
		#判断英雄边界
		if self.rect.bottom <= SCREEN_RECT.y:
			self.rect.y = SCREEN_RECT.bottom
		elif self.rect.y >= SCREEN_RECT.height:
		 	self.rect.y= -self.rect.height
		elif self.rect.left <= 0:
			self.rect.left = 0
		elif self.rect.right >=SCREEN_RECT.right:
			self.rect.right = SCREEN_RECT.right

	def fire(self):
		for i in range(1,4):
			self.bullet2 = Bullet()
			#设置精灵位置
			self.bullet2.rect.left = self.rect.left-15*i
			self.bullet2.rect.centery= self.rect.centery
			
			#将精灵添加到精灵组
			self.bullet2_group.add(self.bullet2)

#敌机类
class Enemy(GameSprites):
	def __init__(self):
		image_name = "./images/_meitu_8.png"
		super().__init__(image_name)
		self.speed = random.randint(2,5)
		#设置敌机随机初始位置
		self.rect.x = -self.rect.left
		max_x = SCREEN_RECT.height - self.rect.height
		self.rect.y= random.randint(0, max_x)

	def update(self):
		super().update()
		if self.rect.right < 0:
			print("敌机飞出屏幕")
			self.kill()		

class Bullet(GameSprites):
	def __init__(self):
		image_name = "./images/bullet2.png"
		super().__init__(image_name,-6)

	def update(self):
		super().update()
		#判断是否超出屏幕 如果是 从屏幕删除
		if self.rect.right < 0:
			self.kill()
class Music(object):
	def __init__(self):
		pygame.init()
		pygame.mixer.music.load("./music/bgm.mp3")
		pygame.mixer.music.play()

	def stopa(self):
		pygame.mixer.music.pause()

	def  unpause(self):
		pygame.mixer.music.unpause()
