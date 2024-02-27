import pygame

from lib.objects.game_object import GameObject


class Coin(GameObject):
    def __init__(self, x, y, width, height, map_builder, coin_type):
        super().__init__(x, y, width, height, map_builder)
        self.coin_type = coin_type


    def render(self, screen):
        pygame.draw.rect(screen, "yellow", (self._x, self._y, self._width, self._height), 0)
