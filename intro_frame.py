import pygame

from pygame.locals import * #import all I guess - key coordinates?

class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square, self).__init__() #access to sprite.spite?
        
        self.surf = pygame.Surface((25, 25))
        #surface
        self.surf.fill((0, 200, 255))
        self.rect = self.surf.get_rect()
        
#initialize
pygame.init()

# define dimensions of screen object
screen = pygame.display.set_mode((800, 600))

#instantiate all square objects
square1 = Square()
square2 = Square()
square3 = Square()
square4 = Square()

#loop running

gameOn = True

while gameOn:
    for event in pygame.event.get():
        
        #check for keydown
        if event.type == KEYDOWN:
            
            #if backspace pressed
            if event.key == K_BACKSPACE:
                gameOn = False
                
        elif event.type == QUIT:
            gameOn = False
    
    # where squares appear on the screen
    screen.blit(square1.surf, (40, 40))
    screen.blit(square2.surf, (40, 530))
    screen.blit(square3.surf, (730, 40))
    screen.blit(square4.surf, (730, 530))
    
    #update the display using flip
    pygame.display.flip()     