import math

import pygame

from lib.objects.game_object import GameObject
from lib.objects.impl.coin import Coin
from lib.objects.impl.wall import Wall
from lib.utills.direction import Direction


class MovableObject(GameObject):
    def __init__(self, x, y, width, height, map_builder):
        super().__init__(x, y, width, height, map_builder)
        self.direction = Direction.RIGHT
        self.is_moving = None
        self.speed = 1

    def set_speed(self, speed) -> None:
        """
        Set the speed
        :arg speed: The speed that will be applied to the object
        :return: None
        """
        self.speed = speed

    def auto_move(self) -> None:
        """
        Move the object
        :return: None
        """
        radians = math.radians(self.direction.value)
        y = -int(math.sin(radians)) * self.speed + self._y
        x = int(math.cos(radians)) * self.speed + self._x
        x_alpha = x - self._map_builder.start_w - self._width / 2
        y_alpha = y - self._map_builder.start_h - self._height / 2
        if int(math.cos(radians)) != 0:
            if 0 < y_alpha % self._height < self._height / 2:
                y -= y_alpha % self._height
            elif self._height / 2 <= y_alpha % self._height < self._height:
                y += self._height - y_alpha % self._height
        else:
            if 0 < x_alpha % self._width < self._width / 2:
                x -= x_alpha % self._width
            elif self._width / 2 <= x_alpha % self._width < self._width:
                x += self._width - x_alpha % self._width
        self.is_moving = True

        obj = self.check_collision(x, y)

        if isinstance(obj, Wall):
            self.is_moving = False
        elif isinstance(obj, Coin):
            self._map_builder.game_objects.remove(obj)
            if obj.coin_type == "C":
                self._map_builder.get_player().score += 1
            elif obj.coin_type == "B":
                self._map_builder.get_player().score += 10
                self._map_builder.get_player().is_god = True

        if self.is_moving:
            self._y = y
            self._x = x

    def set_direction(self, key) -> None:
        """
        Setting the direction of the object
        :arg key: The key that the pressed
        :return: None
        """
        prev_direction = self.direction

        if key == pygame.K_UP:
            self.direction = Direction.UP
        elif key == pygame.K_DOWN:
            self.direction = Direction.DOWN
        elif key == pygame.K_LEFT:
            self.direction = Direction.LEFT
        elif key == pygame.K_RIGHT:
            self.direction = Direction.RIGHT

        self.auto_move()
        if not self.is_moving:
            self.direction = prev_direction
        else:
            for name in self.textures.keys():
                self.textures[name] = pygame.transform.rotate(self.textures[name], self.direction.value - prev_direction.value)

    def check_collision(self, x, y) -> GameObject or None:
        """
        Checking collision with walls
        :arg x: x coordinate
        :arg y: y coordinate
        :return: GameObject if collision with any game_object is true, None otherwise
        """
        collision_rect = pygame.Rect(x - self._width / 2, y - self._height / 2, self._width, self._height)
        for game_object in self._map_builder.game_objects:
            is_collision = collision_rect.colliderect(game_object.get_shape())
            if is_collision:
                return game_object
        return None


