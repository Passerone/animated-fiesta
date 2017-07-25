import sys
import pygame

from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
import game_function as gf

def run_game():
	#初始化游戏，创建屏幕
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
                        (ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	#创建按钮
	play_button = Button(ai_settings,screen,"Play")
	
	stats = GameStats(ai_settings)
	#创建一搜飞船
	ship = Ship(ai_settings,screen)
	#创建一个用于存储子弹的编组
	bullets = Group()
	#创建一个外星人
	aliens = Group()
	
	#创建外星人群
	gf.create_fleet(ai_settings,screen,ship,aliens)
	
	#创建存储游戏统计信息的实力，并创建计分屏
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings,screen,stats)
	print(stats.ships_left)
	#开始游戏的主循环
	while True:
		gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
		
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
			gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)
			
		gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

run_game()	
