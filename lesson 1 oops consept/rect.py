import pygame
pygame.init()

#set dimentions of the screen
screen = pygame.display.set_mode((600,600))
screen.fill('white')
pygame.display.update()

class Rect():
    def __init__(self,x,y,width,height,color):
        self.rect_surf = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
    
    def draw(self):
        pygame.draw.rect(self.rect_surf,self.color,(self.x,self.y,self.width,self.height))

rect_1 = Rect(50,50,50,50,'red')
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    rect_1.draw()

    pygame.display.update()

pygame.quit()