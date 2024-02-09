from lib.game import Game

if __name__ == '__main__':
    game = Game()
    game.setup(1280, 720)
    game.run(60)
