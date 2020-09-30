import pygame
from piece import *


class Board:

    def __init__(self, ai_game):

        self.screen = ai_game.screen
        self.size = 90
        self.board_length = 8

        self.B_king = King('Black', ai_game)
        self.W_king = King('White', ai_game)
        self.B_queen = Queen('Black', ai_game)
        self.W_queen = Queen('White', ai_game)
        self.B_bishop = Bishop('Black', ai_game, 1)
        self.W_bishop = Bishop('White', ai_game, 1)
        self.B_knight = Knight('Black', ai_game, 1)
        self.W_knight = Knight('White', ai_game, 1)
        self.B_rook = Rook('Black', ai_game, 1)
        self.W_rook = Rook('White', ai_game, 1)
        self.B_bishop2 = Bishop('Black', ai_game, 2)
        self.W_bishop2 = Bishop('White', ai_game, 2)
        self.B_knight2 = Knight('Black', ai_game, 2)
        self.W_knight2 = Knight('White', ai_game, 2)
        self.B_rook2 = Rook('Black', ai_game, 2)
        self.W_rook2 = Rook('White', ai_game, 2)
        self.pawn = []

        for i in range(8):
            self.pawn.append(Pawn('Black', ai_game, i))
        for i in range(8):
            self.pawn.append(Pawn('White', ai_game, i))








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
        self.W_king.draw()
        self.B_queen.draw()
        self.W_queen.draw()
        self.B_bishop.draw()
        self.W_bishop.draw()
        self.B_knight.draw()
        self.W_knight.draw()
        self.B_rook.draw()
        self.W_rook.draw()
        self.B_bishop2.draw()
        self.W_bishop2.draw()
        self.B_knight2.draw()
        self.W_knight2.draw()
        self.B_rook2.draw()
        self.W_rook2.draw()
        for i in self.pawn:
            i.draw()







