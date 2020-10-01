import pygame
import sys
from settings import Settings
from board import Board


class ChessGame:

    def __init__(self):

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("2d Chess by Jason Chen")
        self.board = Board(self)

        self.square_selected = ()
        self.select_history = []

    def run_game(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_location = pygame.mouse.get_pos()
                    row = mouse_location[0] // self.settings.square_size
                    col = mouse_location[1] // self.settings.square_size
                    if self.square_selected == (row, col):
                        self.square_selected = ()
                        self.select_history = []
                    else:
                        self.square_selected = (row, col)
                        self.select_history.append(self.square_selected)

                    if len(self.select_history) == 2:
                        if self.board.board[self.select_history[0][1]][self.select_history[0][0]] == '--':
                            self.select_history[0] = self.square_selected
                            self.select_history.pop(1)
                        else:
                            self.board.move(self.select_history)
                            self.select_history = []
                            self.square_selected = ()

            self.screen.fill(self.settings.bg_color)
            self.board.draw_board()
            self.board.draw_piece()
            pygame.display.flip()




if __name__ == '__main__':

    ai = ChessGame()
    ai.run_game()

