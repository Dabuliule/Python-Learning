import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化背景设置
    pygame.init()
    ai_settings = Settings()

    # 调用 pygame.display.set_mode() 来创建一个名为 screen 的显示窗口
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )

    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(screen)

    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ship)

        ship.update()

        gf.update_screen(ai_settings, screen, ship)


run_game()
