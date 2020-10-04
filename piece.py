class Piece:

    def __init__(self, rank, team, y, x):
        self.rank = rank
        self.team = team
        self.x = x
        self.y = y
        self.num_moves = 0

    def get_rank(self):
        return self.rank

    def get_team(self):
        return self.team

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def generate_moves(self, board_state):
        return []


class King(Piece):

    def __init__(self, team, x, y):
        super().__init__('king', team, x, y)

    def generate_moves(self, board_state):
        return [(self.x - 1, self.y - 1), (self.x, self.y - 1), (self.x + 1, self.y - 1),
                (self.x - 1, self.y), (self.x + 1, self.y),
                (self.x - 1, self.y + 1), (self.x, self.y + 1), (self.x + 1, self.y - 1)]


class Queen(Piece):

    def __init__(self, team, x, y):
        super().__init__('queen', team, x, y)

    def generate_moves(self, board_state):
        temp_rook = Rook(self.team, self.y, self.x)
        temp_bishop = Bishop(self.team, self.y, self.x)
        possible_moves = temp_rook.generate_moves(board_state) + temp_bishop.generate_moves(board_state)
        print(possible_moves)
        return possible_moves


class Bishop(Piece):

    def __init__(self, team, x, y):
        super().__init__('bishop', team, x, y)

    def generate_moves(self, board_state):

        possible_moves = []

        directions = ((-1, -1), (-1, 1), (1, -1), (1, 1))
        for d in directions:
            for i in range(1, 8):
                end_row = self.x + d[0] * i
                end_col = self.y + d[1] * i
                if -1 < end_row < 8 and -1 < end_col < 8:
                    end_piece = board_state[end_col][end_row]
                    if end_piece is None:
                        possible_moves.append((end_row, end_col))
                    elif end_piece.team != self.team:
                        possible_moves.append((end_row, end_col))
                        break
                    else:
                        break
                else:
                    break

        print(possible_moves)
        return possible_moves


class Knight(Piece):

    def __init__(self, team, x, y):
        super().__init__('knight', team, x, y)

    def generate_moves(self, board_state):
        possible_moves = []

        directions = ((2, -1), (2, 1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2))

        for d in directions:
            end_row = self.x + d[0]
            end_col = self.y + d[1]
            if -1 < end_row < 8 and -1 < end_col < 8:
                end_piece = board_state[end_col][end_row]
                if end_piece is None:
                    possible_moves.append((end_row, end_col))
                elif end_piece.team != self.team:
                    possible_moves.append((end_row, end_col))

        return possible_moves


class Rook(Piece):

    def __init__(self, team, x, y):
        super().__init__('rook', team, x, y)

    def generate_moves(self, board_state):
        possible_moves = []
        directions = ((-1, 0), (0, -1), (1, 0), (0, 1))
        for d in directions:
            for i in range(1, 8):
                end_row = self.x + (d[0] * i)
                end_col = self.y + (d[1] * i)
                if -1 < end_row < 8 and -1 < end_col < 8:
                    end_piece = board_state[end_col][end_row]
                    if end_piece is None:
                        possible_moves.append((end_row, end_col))
                    elif self.team != end_piece.team:
                        possible_moves.append((end_row, end_col))
                        break
                    else:
                        break
                else:
                    break

        print(possible_moves)
        return possible_moves


class Pawn(Piece):

    def __init__(self, team, x, y):
        super().__init__('pawn', team, x, y)

    def generate_moves(self, board_state):

        possible_moves = []
        if self.team == 'b':
            if -1 < self.y + 1 < 8:
                if board_state[self.y + 1][self.x] is None:
                    possible_moves.append((self.x, self.y + 1))
                    if self.num_moves == 0:
                        possible_moves.append((self.x, self.y + 2))
            if 8 > self.y + 1 > -1 and 8 > self.x + 1 > -1:
                end_piece = board_state[self.y + 1][self.x + 1]
                if end_piece is not None and self.team != end_piece.team:
                    possible_moves.append((self.x + 1, self.y + 1))
            if 8 > self.y + 1 > -1 and 8 > self.x - 1 > -1:
                end_piece = board_state[self.y + 1][self.x - 1]
                if end_piece is not None and self.team != end_piece.team:
                    possible_moves.append((self.x - 1, self.y + 1))
        else:
            if -1 < self.y - 1 < 8:
                if board_state[self.y - 1][self.x] is None:
                    possible_moves.append((self.x, self.y - 1))
                    if self.num_moves == 0:
                        possible_moves.append((self.x, self.y - 2))
            if 8 > self.y - 1 > -1 and 8 > self.x - 1 > -1:
                end_piece = board_state[self.y - 1][self.x - 1]
                if end_piece is not None and end_piece.team != self.team:
                    possible_moves.append((self.x - 1, self.y - 1))
            if 8 > self.y - 1 > -1 and 8 > self.x + 1 > -1:
                end_piece = board_state[self.y - 1][self.x + 1]
                if end_piece is not None and self.team != end_piece.team:
                    possible_moves.append((self.x + 1, self.y - 1))

        return possible_moves
