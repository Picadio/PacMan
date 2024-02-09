import pygame


class GameObject:
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def render(self, screen):
        pass

    def load_texture(self, filename):
        pass