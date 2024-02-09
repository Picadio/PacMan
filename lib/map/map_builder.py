import pygame

from lib.objects.impl.wall import Wall


class MapBuilder:
    def __init__(self, map_loader, screen):
        self.map_loader = map_loader
        self.screen = screen
        self.game_objects = []
        self.movable_objects = []
        self.player = None
        self.start_h = 0.0
        self.start_w = 0.0

    def build_map(self):
        file_map = self.map_loader.load_map()
        height = len(file_map)
        width = len(file_map[0])
        w, h = self.screen.get_size()
        self.start_w = w / 2 - int(width / 2) * 20
        self.start_h = h / 2 - int(height / 2) * 20
        for (i, line) in enumerate(file_map):
            for (j, tile) in enumerate(line):
                if tile == 'W':
                    wall = Wall(j * 20 + self.start_w, i * 20 + self.start_h, 20, 20)
                    self.game_objects.append(wall)

    def render(self):
        for game_object in self.game_objects:
            game_object.render(self.screen)


