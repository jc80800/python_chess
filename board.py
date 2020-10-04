import pygame
from piece import *
from moves import *


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

        self.board_object = []
        self.board_row = []
        for i in range(self.board_length):
            for j in range(self.board_length):
                if self.board[i][j] == '--':
                    self.board_row.append(None)
                else:
                    temp = self.board[i][j]
                    rank = temp[2::]
                    if rank == 'rook':
                        self.board_row.append(Rook(temp[0], i, j))
                    elif rank == 'knight':
                        self.board_row.append(Knight(temp[0], i, j))
                    elif rank == 'bishop':
                        self.board_row.append(Bishop(temp[0], i, j))
                    elif rank == 'queen':
                        self.board_row.append(Queen(temp[0], i, j))
                    elif rank == 'pawn':
                        self.board_row.append(Pawn(temp[0], i, j))
                    else:
                        self.board_row.append(King(temp[0], i, j))
            self.board_object.append(self.board_row)
            self.board_row = []

        self.pieces = ['w_king', 'b_king', 'w_queen', 'b_queen',
                       'w_bishop', 'b_bishop', 'w_knight', 'b_knight',
                       'w_rook', 'b_rook', 'w_pawn', 'b_pawn']
        self.IMAGES = {}
        for piece in self.pieces:
            self.IMAGES[piece] = pygame.transform.scale(pygame.image.load('images/' + str(piece) + '.png'),
                                                        (self.size, self.size))

        self.moves_made = []

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
                piece = self.board_object[i][j]
                if piece is not None:
                    string = piece.get_team() + '_' + piece.get_rank()
                    self.screen.blit(self.IMAGES[string], (self.size * j, self.size * i, self.size, self.size))

    def move(self, select_history):
        initial_coordinate = select_history[0]
        initial_x = initial_coordinate[0]
        initial_y = initial_coordinate[1]

        destination = select_history[1]
        destination_x = destination[0]
        destination_y = destination[1]

        piece = self.board_object[initial_y][initial_x]
        destination_piece = self.board_object[destination_y][destination_x]

        move_made = Moves(initial_x, initial_y, destination_x, destination_y, piece, destination_piece)
        self.moves_made.append(move_made)

        possible_moves = piece.generate_moves(self.board_object)
        position = (destination_x, destination_y)
        if isinstance(piece, Queen):
            print(position)
        if position in possible_moves:
            piece.set_x(destination_x)
            piece.set_y(destination_y)
            self.board_object[destination_y][destination_x] = piece
            self.board_object[initial_y][initial_x] = None
            piece.num_moves += 1
        else:
            print("Can't")

    def undo_move(self):
        if len(self.moves_made) == 0:
            pass
        else:
            undo_move = self.moves_made.pop()
            self.board_object[undo_move.destination_y][undo_move.destination_x] = undo_move.destination_piece
            self.board_object[undo_move.initial_y][undo_move.initial_x] = undo_move.initial_piece

            if self.board_object[undo_move.destination_y][undo_move.destination_x] is None:
                pass
            else:
                dest_piece = self.board_object[undo_move.destination_y][undo_move.destination_x]
                dest_piece.set_x(undo_move.destination_x)
                dest_piece.set_y(undo_move.destination_y)

            if self.board_object[undo_move.initial_y][undo_move.initial_x] is None:
                pass
            else:
                init_piece = self.board_object[undo_move.initial_y][undo_move.initial_x]
                init_piece.set_x(undo_move.initial_x)
                init_piece.set_y(undo_move.initial_y)
                init_piece.num_moves -= 1
