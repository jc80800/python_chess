import pygame
from piece import *


class Board:

    def __init__(self, ai_game):

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.size = self.settings.square_size
        self.board_length = 8

        self.board = [
            ['b_rook', 'b_knight', 'b_bishop', 'b_queen', 'b_king', 'b_bishop', 'b_knight', 'b_rook'],
            ['b_pawn', 'b_pawn', 'b_pawn', 'b_pawn', 'b_pawn', 'b_pawn', 'b_pawn', 'b_pawn'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--'],
            ['w_pawn', 'w_pawn', 'w_pawn', 'w_pawn', 'w_pawn', 'w_pawn', 'w_pawn', 'w_pawn'],
            ['w_rook', 'w_knight', 'w_bishop', 'w_queen', 'w_king', 'w_bishop', 'w_knight', 'w_rook']
            ]

        self.pieces = ['w_king', 'b_king', 'w_queen', 'b_queen',
                       'w_bishop', 'b_bishop', 'w_knight', 'b_knight',
                       'w_rook', 'b_rook', 'w_pawn', 'b_pawn']
        self.IMAGES = {}
        for piece in self.pieces:
            self.IMAGES[piece] = pygame.transform.scale(pygame.image.load('images/' + str(piece) + '.png'),
                                                        (self.size, self.size))

    def draw_board(self):
        cnt = 0
        for i in range(self.board_length):
            for j in range(self.board_length):
                if cnt % 2 == 0:
                    pygame.draw.rect(self.screen, (96, 96, 86), [self.size * j, self.size * i, self.size, self.size])
                else:
                    pygame.draw.rect(self.screen, (139, 69, 19), [self.size * j, self.size * i, self.size, self.size])
                cnt += 1
            cnt -= 1

    def draw_piece(self):
        for i in range(self.board_length):
            for j in range(self.board_length):
                piece = self.board[i][j]
                if piece != '--':
                    self.screen.blit(self.IMAGES[piece], (self.size * j, self.size * i, self.size, self.size))

    def move(self, select_history):
        initial_coordinate = select_history[0]
        initial_x = initial_coordinate[0]
        initial_y = initial_coordinate[1]

        destination = select_history[1]
        destination_x = destination[0]
        destination_y = destination[1]

        piece = self.board[initial_y][initial_x]
        self.board[destination_y][destination_x] = piece
        self.board[initial_y][initial_x] = '--'










