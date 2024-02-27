from lib.objects.impl.coin import Coin
from lib.objects.impl.pacman import PacMan
from lib.objects.impl.wall import Wall


class MapBuilder:
    def __init__(self, map_loader, screen):
        self.map_loader = map_loader
        self.screen = screen
        self.game_objects = []
        self.movable_objects = []
        self.walls = []
        self.player = None
        self.start_h = 0.0
        self.start_w = 0.0

    def build_map(self) -> None:
        """
        Builds the map and create the objects
        :return: None
        """
        file_map = self.map_loader.load_map()
        height = len(file_map)
        width = len(file_map[0])
        w, h = self.screen.get_size()
        self.start_w = w / 2 - int(width / 2) * 20
        self.start_h = h / 2 - int(height / 2) * 20
        for (i, line) in enumerate(file_map):
            for (j, tile) in enumerate(line):
                x = j * 20 + self.start_w
                y = i * 20 + self.start_h
                if tile == 'W':
                    wall = Wall(x, y, 20, 20, self)
                    self.game_objects.append(wall)
                    self.walls.append(wall)
                elif tile == 'P':
                    pacman = PacMan(x + 10, y + 10, 20, 20, self)
                    self.game_objects.append(pacman)
                    self.movable_objects.append(pacman)
                    self.player = pacman
                elif tile == "C" or tile == "B":
                    size = 5 if tile == "C" else 10
                    coord = 7.5 if tile == "C" else 5
                    coin = Coin(x+coord, y+coord, size, size, self, tile)
                    self.game_objects.append(coin)

    def get_player(self) -> PacMan:
        """
        Gets the player
        :return: player
        """
        return self.player

    def render(self) -> None:
        """
        Renders the map
        :return: None
        """
        for game_object in self.game_objects:
            game_object.render(self.screen)

    def update(self) -> None:
        """
        Updates the movable objects
        :return: None
        """
        for movable_object in self.movable_objects:
            movable_object.auto_move()
