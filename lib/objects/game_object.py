import pygame


class GameObject:
    def __init__(self, x, y, width, height, map_builder):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._map_builder = map_builder
        self._shape = pygame.Rect(x, y, width, height)

    def get_shape(self):
        return self._shape

    def render(self, screen):
        pass

    def load_texture(self, filename):
        pass