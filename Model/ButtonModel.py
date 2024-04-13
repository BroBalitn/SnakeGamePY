import pygame

class Button():
    def __init__(self, toppos, rightpos, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (toppos,rightpos)
        self.clicked = False

    def btnpush(self,surface):
        action = False
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x,self.rect.y))

        return action