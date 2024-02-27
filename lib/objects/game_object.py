import pygame


class GameObject:
    def __init__(self, x, y, width, height, map_builder):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._map_builder = map_builder
        self._shape = pygame.Rect(x, y, width, height)
        self.textures = dict()

    def get_shape(self) -> pygame.Rect:
        """
        Get the shape
        :return: the shape of the object
        """
        return self._shape

    def render(self, screen) -> None:
        """
        Render the object on the screen
        :arg screen: the screen
        :return: None
        """
        pass

    def load_texture(self, filename, name) -> None:
        """
        Load the texture
        :arg filename: the name of the texture file
        :arg name: the name that be using for the texture
        :return: None
        """
        self.textures[name] = pygame.image.load(filename)
        self.textures[name] = pygame.transform.scale(self.textures[name], (self._width, self._height))
