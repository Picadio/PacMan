import pygame

from lib.objects.movable_object import MovableObject


class PacMan(MovableObject):
    def __init__(self, x, y, width, height, map_builder):
        super().__init__(x, y, width, height, map_builder)
        self.load_texture("./assets/pak.png")

    def render(self, screen):
        screen.blit(self.texture, self.texture.get_rect(center=(self._x, self._y)))

