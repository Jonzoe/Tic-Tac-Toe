import pygame
import time
  
window = pygame.display.set_mode((400, 400))

background_colour = (255, 255, 255)
window.fill(background_colour)

pygame.display.set_caption("Tic Tac Toe")
pygame.display.flip()

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running == False