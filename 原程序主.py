import pygame
from test import *
# pygame.init()
# pygame.mixer.music.load('./music/bgm.mp3')
# pygame.mixer.music.play()
class HuYouJiaPlaneGame(object):
	def __init__(self):
		print("游戏初始化")
		#1 游戏窗口 2 游戏时钟 3 精灵和精灵组的创建	

		self.screen = pygame.display.set_mode((SCREEN_RECT.width,SCREEN_RECT.height))
		self.clock = pygame.time.Clock()
		self.__create_sprites()
		pygame.time.set_timer(CREATE_ENEMY,800)
		pygame.time.set_timer(HREO_FIRE_EVENT,1000)
		self.name = 0
		self.music = Music()
		self.player = 0
		self.player2 = 0
	def start_game(self):
		print("开始游戏")
		while True:
			self.clock.tick(60)
			#事件监听
			self.__event_handler()
			# 碰撞检测
			self.__check_collide()
			# 更新精灵组
			self.__update_sprites()
			#打印分数
			self.__print_score()

			pygame.display.set_caption("飞机大战1.0")

			#更新屏幕显示
			pygame.display.update()

	#创建精灵
	def __create_sprites(self):
		self.hero = Hero()
		self.hero2 = Hero2()
		self.hero_group = pygame.sprite.Group(self.hero)
		self.hero2_group = pygame.sprite.Group(self.hero2)
		self.enemy = Enemy()
		self.enemy_group = pygame.sprite.Group(self.enemy)
		bg1 = Background()
		bg2 = Background(True)
		self.back_group = pygame.sprite.Group(bg1,bg2)
	
	#事件监听
	def __event_handler(self):
		for event in pygame.event.get():
			key = pygame.key.get_pressed()
			if key[pygame.K_RIGHT]:
				self.hero.speed = 8
			elif key[pygame.K_LEFT]:
				self.hero.speed = -8
			else:
				self.hero.speed = 0
			if key[pygame.K_UP]:
				self.hero.speed1 =-8
			elif key[pygame.K_DOWN]:
				self.hero.speed1 = 8
			else:
				self.hero.speed1 = 0
			if key[pygame.K_d]:
				self.hero2.speed = 8
			elif key[pygame.K_a]:
				self.hero2.speed = -8
			else:
				self.hero2.speed = 0
			if key[pygame.K_w]:
				self.hero2.speed2 =-8
			elif key[pygame.K_s]:
				self.hero2.speed2 = 8
			else:
				self.hero2.speed2= 0
			if event.type == pygame.QUIT:
				self.__game_over()
			elif event.type == CREATE_ENEMY:
				self.enemy_group.add(Enemy())
				print("敌机出场")		
			elif event.type == HREO_FIRE_EVENT:
				self.hero.fire()
				self.hero2.fire()
			#音乐控制
			if key[pygame.K_SPACE]:
				self.name += 1
				if self.name %2 ==0:
					self.music.unpause()
				else:
					self.music.stopa()

	#检测碰撞
	def __check_collide(self):
		#子弹摧毁敌机
		if pygame.sprite.groupcollide(self.hero.bullet_group,self.enemy_group,True,True):
			self.player += 1
			print("第一台飞机分数是%d"%self.player)
		elif pygame.sprite.groupcollide(self.hero2.bullet2_group,self.enemy_group,True,True):
			self.player2 += 1
			print("第二台飞机分数是%d"%self.player2)


		#敌机摧毁英雄
		enemies = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
		enemies2 = pygame.sprite.spritecollide(self.hero2,self.enemy_group,True)
		#判断列表时候有内容
		if len(enemies) == 1:
			self.hero.kill()
			self.hero.rect.x = -10000
		if len(enemies2) == 1:
			self.hero2.kill()
			self.hero2.rect.x = -10000
		if self.hero.rect.x == -10000 and self.hero2.rect.x == -10000:
			HuYouJiaPlaneGame.__game_over()

	#显示分数
	def __print_score(self):
		pygame.font.init()
		#位置
		pos1 = (200,0)
		pos2 = (400,0)
		#颜色
		color = (0,0,0)
		text1 ="player1:" + str(self.player)
		text2 = "player2:" + str(self.player2)
		cur_font = pygame.font.SysFont("楷体",30)
		text_font1 = cur_font.render(text1,1,color)
		text_font2 = cur_font.render(text2,1,color)
		self.screen.blit(text_font1,pos1)
		self.screen.blit(text_font2,pos2)


	@staticmethod
	def __game_over():
		print("游戏结束")
		pygame.quit()
		exit()


	def __update_sprites(self):
		for i in [self.back_group,self.hero_group,self.enemy_group,self.hero.bullet_group,self.hero2_group,self.hero2.bullet2_group]:
			i.update()
			i.draw(self.screen)
if __name__ == "__main__":
	game = HuYouJiaPlaneGame()
	game.start_game()

			
