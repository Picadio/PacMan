import math

import pygame

from lib.objects.game_object import GameObject
from lib.objects.impl.wall import Wall
from lib.utills.direction import Direction


class MovableObject(GameObject):
    def __init__(self, x, y, width, height, map_builder):
        super().__init__(x, y, width, height, map_builder)
        self.direction = Direction.RIGHT
        self.texture = None

    def load_texture(self, filename):
        self.texture = pygame.image.load(filename)
        self.texture = pygame.transform.scale(self.texture, (self._width, self._height))

    def auto_move(self):
        radians = math.radians(self.direction.value)
        y = -int(math.sin(radians)) + self._y
        x = int(math.cos(radians)) + self._x
        if not self.check_collision_with_walls(x, y):
            self._y = y
            self._x = x
        else:
            x_alpha = x - self._map_builder.start_w - 10
            y_alpha = y - self._map_builder.start_h - 10
            if int(math.cos(radians)) != 0:
                if 0 < y_alpha % 20 < 10:
                    y -= y_alpha % 20
                elif 10 <= y_alpha % 20 <= 19:
                    y += 20 - y_alpha % 20
            else:
                if 0 < x_alpha % 20 < 10:
                    x -= x_alpha % 20
                elif 10 <= x_alpha % 20 <= 19:
                    x += 20 - x_alpha % 20
            if not self.check_collision_with_walls(x, y):
                self._y = y
                self._x = x
            else:
                return False
        return True

    def set_direction(self, key):
        prev_direction = self.direction
        if key == pygame.K_UP:
            self.direction = Direction.UP
        elif key == pygame.K_DOWN:
            self.direction = Direction.DOWN
        elif key == pygame.K_LEFT:
            self.direction = Direction.LEFT
        elif key == pygame.K_RIGHT:
            self.direction = Direction.RIGHT
        if not self.auto_move():
            self.direction = prev_direction
        else:
            self.texture = pygame.transform.rotate(self.texture, self.direction.value - prev_direction.value)

    def check_collision_with_walls(self, x, y):
        collision_rect = pygame.Rect(x - self._width / 2, y - self._height / 2, self._width, self._height)
        is_collision = False
        for game_object in self._map_builder.walls:
            is_collision = collision_rect.colliderect(game_object.get_shape())
            if is_collision:
                break
        return is_collision

