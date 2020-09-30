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

    def draw(self):
        self.screen.blit(self.image, self.rect)


class King(Piece):

    def __init__(self, role, ai_game):
        if role == 'Black':
            super().__init__(ai_game, 405, 45, 'images/b_king.png')







