import pygame


class Piece:

    def __init__(self, ai_game, x, y, image):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect()

        self.rect.centerx = x
        self.rect.centery = y

        self.dragging = False

    def draw(self):
        self.screen.blit(self.image, self.rect)


class King(Piece):

    def __init__(self, role, ai_game):
        if role == 'Black':
            super().__init__(ai_game, 405, 45, 'images/b_king.png')
        else:
            super().__init__(ai_game, 405, 675, 'images/w_king.png')


class Queen(Piece):

    def __init__(self, role, ai_game):
        if role == 'Black':
            super().__init__(ai_game, 315, 45, 'images/b_queen.png')
        else:
            super().__init__(ai_game, 315, 675, 'images/w_queen.png')


class Bishop(Piece):

    def __init__(self, role, ai_game, position):
        if role == 'Black':
            if position == 1:
                super().__init__(ai_game, 225, 45, 'images/b_bishop.png')
            else:
                super().__init__(ai_game, 495, 45, 'images/b_bishop.png')
        else:
            if position == 1:
                super().__init__(ai_game, 225, 675, 'images/w_bishop.png')
            else:
                super().__init__(ai_game, 495, 675, 'images/b_bishop.png')


class Knight(Piece):

    def __init__(self, role, ai_game, position):
        if role == 'Black':
            if position == 1:
                super().__init__(ai_game, 135, 45, 'images/b_knight.png')
            else:
                super().__init__(ai_game, 585, 45, 'images/b_knight.png')
        else:
            if position == 1:
                super().__init__(ai_game, 135, 675, 'images/w_knight.png')
            else:
                super().__init__(ai_game, 585, 675, 'images/w_knight.png')


class Rook(Piece):

    def __init__(self, role, ai_game, position):
        if role == 'Black':
            if position == 1:
                super().__init__(ai_game, 45, 45, 'images/b_rook.png')
            else:
                super().__init__(ai_game, 675, 45, 'images/b_rook.png')
        else:
            if position == 1:
                super().__init__(ai_game, 45, 675, 'images/w_rook.png')
            else:
                super().__init__(ai_game, 675, 675, 'images/w_rook.png')


class Pawn(Piece):

    def __init__(self, role, ai_game, position):
        if role == 'Black':
            super().__init__(ai_game, (90 * position) + 45, 135, 'images/b_pawn.png')
        else:
            super().__init__(ai_game, (90 * position) + 45, 585, 'images/w_pawn.png')















