# @Time    : 2018/4/24 14:58
# @Author  : freedomyeah
# @Email   : iamdouble@163.com
# @Copyright:  MIT

from settings import *
from pygame import *
import pygame

class Piece():
    def __init__(self, shape, screen):
        self.x = 3
        self.y = 0
        self.shape = shape
        self.turn = 0   #翻转了几次，决定显示的模样
        self.screen = screen

    def paint(self):
        shape_template = PIECES[self.shape]
        shape_turn = shape_template[self.turn]
        #print(shape_turn)
        for r in range(len(shape_turn)):
            for c in range(len(shape_turn[0])):
                if shape_turn[r][c] == 'O':
                    self.draw_cell(self.x + c, self.y + r)

    def draw_cell(self, x, y):
        cell_position = (x * CELL_WIDTH + GAME_AREA_LEFT + 1,
                         y * CELL_WIDTH + GAME_AREA_TOP + 1)
        cell_width_height = (CELL_WIDTH - 2, CELL_WIDTH - 2)
        cell_rect = Rect(cell_position, cell_width_height)
        pygame.draw.rect(self.screen, CELL_COLOR, cell_rect)
