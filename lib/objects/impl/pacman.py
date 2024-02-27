from pathlib import Path

import pygame
from pygame import Surface

from lib.objects.game_object import GameObject
from lib.objects.movable_object import MovableObject


class PacMan(MovableObject):
    def __init__(self, x, y, width, height, map_builder):
        super().__init__(x, y, width, height, map_builder)
        self.load_texture(Path("./assets")/"pak.png", "pak")
        self.load_texture(Path("./assets")/"man.png", "man")
        self.texture_name = "pak"
        self.timer = 0
        self.score = 0
        self.is_god = False

    def render(self, screen):
        texture = self.get_current_texture()
        screen.blit(texture, texture.get_rect(center=(self._x, self._y)))
        self.render_score(screen)

    def render_score(self, screen):
        font = pygame.font.SysFont("TimesNewRoman", 48)
        img = font.render('Score ' + str(self.score), True, pygame.Color('white'))
        screen.blit(img, (20, 20))

    def get_current_texture(self) -> Surface:
        """
        Get the current texture that is used to render
        :return: texture
        """
        if self.is_moving:
            if self.timer >= 5 / self.speed:
                self.texture_name = "man" if self.texture_name == "pak" else "pak"
                self.timer = 0
            self.timer += 1
        else:
            self.texture_name = "pak"

        return self.textures[self.texture_name]


