import pygame

from lib.map.map_builder import MapBuilder
from lib.map.map_loader import MapLoader


class Game:
    def __init__(self):
        self.filename = "./maps/default.txt"
        self.screen = None
        self.clock = None
        self.map_builder = None
        self.player = None

    def set_map(self, filename):
        self.filename = filename

    def get_map(self):
        return self.filename

    def set_player(self, player):
        self.player = player

    def get_player(self):
        return self.player

    def setup(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        map_loader = MapLoader(self.filename)
        self.map_builder = MapBuilder(map_loader, self.screen)
        self.map_builder.build_map()

    def run(self, fps):
        running = True

        self.map_builder.render()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill("black")

            self.map_builder.render()

            pygame.display.flip()

            self.clock.tick(fps)

        pygame.quit()
