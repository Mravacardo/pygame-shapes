import pygame

pygame.init()

screen = pygame.display.set_mode((600,700))
pygame.display.set_caption("Pygame shapes")


black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
screen.fill((0,25,255))
pygame.display.update()
while True:
   class Rect():
       def __init__(self,colour,dimentions):
           self.rect_surf = screen
           self.rect_colour = colour
           self.rect_dimentions = dimentions

       def draw(self):
           self.Draw_rect = pygame.draw.rect(self.rect_surf, self.rect_colour, self.rect_dimentions)

   greenRect=Rect(green,(50,20,100,100))
   redRect=Rect(red,(150,200,150,150))
   whiteRect=Rect(white,(300,400,200,200))
   greenRect.draw()
   whiteRect.draw()
   redRect.draw()
   for event in pygame.event.get():
       if event.type==pygame.QUIT:
           pygame.quit()
   pygame.display.update()
