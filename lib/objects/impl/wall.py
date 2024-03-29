import pygame

from lib.objects.game_object import GameObject


class Wall(GameObject):
    def __init__(self, x, y, width, height, map_builder):
        super().__init__(x, y, width, height, map_builder)

    def render(self, screen):
        pygame.draw.rect(screen, "blue", (self._x, self._y, self._width, self._height), 0)
    
