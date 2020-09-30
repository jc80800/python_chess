import pygame
import sys
from settings import Settings
from board import Board
from piece import Piece

class ChessGame:

    def __init__(self):

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("2d Chess by Jason Chen")

        self.board = Board(self)

    def run_game(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.board.draw_board()
            pygame.display.flip()




if __name__ == '__main__':

    ai = ChessGame()
    ai.run_game()

