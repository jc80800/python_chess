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


class Bishop(Piece):

    def __init__(self, team, x, y):
        super().__init__('bishop', team, x, y)


class Knight(Piece):

    def __init__(self, team, x, y):
        super().__init__('knight', team, x, y)


class Rook(Piece):

    def __init__(self, team, x, y):
        super().__init__('rook', team, x, y)

    def generate_moves(self, board_state):
        possible_moves = []
        x = 0
        y = 0
        while x < 8:
            possible_moves.append((x, self.y))
            possible_moves.append((self.x, y))
            x += 1
            y += 1
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
                if board_state[self.y + 1][self.x + 1] is not None:
                    possible_moves.append((self.x + 1, self.y + 1))
            if 8 > self.y + 1 > -1 and 8 > self.x - 1 > -1:
                if board_state[self.y + 1][self.x - 1] is not None:
                    possible_moves.append((self.x - 1, self.y + 1))
        else:
            if -1 < self.y - 1 < 8:
                if board_state[self.y - 1][self.x] is None:
                    possible_moves.append((self.x, self.y - 1))
                    if self.num_moves == 0:
                        possible_moves.append((self.x, self.y - 2))
            if 8 > self.y - 1 > -1 and 8 > self.x - 1 > -1:
                if board_state[self.y - 1][self.x - 1] is not None:
                    possible_moves.append((self.x - 1, self.y - 1))
            if 8 > self.y - 1 > -1 and 8 > self.x + 1 > -1:
                if board_state[self.y - 1][self.x + 1] is not None:
                    possible_moves.append((self.x + 1, self.y - 1))

        return possible_moves
