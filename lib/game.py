import pygame

from lib.map.map_builder import MapBuilder
from lib.map.map_loader import MapLoader
from lib.objects.impl.pacman import PacMan


class Game:
    def __init__(self):
        self.filename = "./maps/default.txt"
        self.screen = None
        self.clock = None
        self.map_builder = None
        self.player = None

    def set_map(self, filename):
        """
        Set a map file
        :arg filename: The name of the map file
        :return: None
        """
        self.filename = filename

    def get_map(self) -> str:
        """
        Get a map file
        :return: filename string
        """
        return self.filename

    def set_player(self, player) -> None:
        """
        Set a player object
        :arg player: The player object
        :return: None
        """
        self.player = player

    def get_player(self) -> PacMan:
        """
        Get a player object
        :return: player object
        """
        return self.player

    def setup(self, width, height) -> None:
        """
        Sets up the game
        :arg width: width of the screen
        :arg height: height of the screen
        :return: None
        """
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        map_loader = MapLoader(self.filename)
        self.map_builder = MapBuilder(map_loader, self.screen)
        self.map_builder.build_map()
        self.player = self.map_builder.get_player()

    def run(self, fps) -> None:
        """
        Run the game
        :arg fps: FPS
        :return: None
        """
        running = True

        self.map_builder.render()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    self.player.set_direction(event.key)
            self.screen.fill("black")

            self.map_builder.update()
            self.map_builder.render()


            pygame.display.flip()

            self.clock.tick(fps)

        pygame.quit()
