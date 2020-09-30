import pygame
from piece import King


class Board:

    def __init__(self, ai_game):

        self.screen = ai_game.screen
        self.size = 90
        self.board_length = 8
        self.board = []
        self.B_king = King('Black', ai_game)



    def draw_board(self):
        # board length, must be even
        cnt = 0
        for i in range(self.board_length):
            for z in range(self.board_length):
                # check if current loop value is even
                if cnt % 2 == 0:
                    pygame.draw.rect(self.screen, (96, 96, 86), [self.size * z, self.size * i, self.size, self.size])
                else:
                    pygame.draw.rect(self.screen, (139, 69, 19), [self.size * z, self.size * i, self.size, self.size])
                cnt += 1
            # since theres an even number of squares go back one value
            cnt -= 1

        self.B_king.draw()






