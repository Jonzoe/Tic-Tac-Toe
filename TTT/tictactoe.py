# Import
from array import array
from queue import Empty
from tkinter.font import Font
import pygame
import time
from pygame.locals import *
import pygame.freetype
import random

# Sätter font
pygame.font.init()
FONT = pygame.font.SysFont("arial", 32)

# Definerar färger
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
# Width och Height på gridrutorna
WIDTH = 160
HEIGHT = 160

# Fönsterstorlek
WINDOW_SIZE = [500, 650]

# Margin mellan varje ruta
MARGIN = 5

# Vinnar variabeln
winner = False

# Skapar en 2D grid
box = 3
grid = []
for row in range(box):
    grid.append([])
    for column in range(box):
        grid[row].append(None)

# Printar griden i konsollen
for r in grid:
    print(r)

# Aktiverar pygame biblioteket
pygame.init()
 
# Sätter storleken på fönstret
screen = pygame.display.set_mode(WINDOW_SIZE)

# Bakgrundsfärg i fönstret
screen.fill(BLACK)
    
# Namnet på fönstret
pygame.display.set_caption("Tic Tac Toe")

# Variabel för hur snabbt fönstret uppdateras
clock = pygame.time.Clock()

# Random player
player = ["x", "o"][random.randint(0, 1)]

# Sätter uppdateringshastigheten
clock.tick(60)

# Laddar in bilder
x_img = pygame.image.load('C:/Users/emil.jonsson8/.vscode/Python/TTT/X.png')
o_img = pygame.image.load('C:/Users/emil.jonsson8/.vscode/Python/TTT/O.png')

# Gör om storleken på bilderna
x_img = pygame.transform.scale(x_img, (120,120))
o_img = pygame.transform.scale(o_img, (120,120))

# Loopar tills användaren klickar på X (stäng)
running = True

# Ritar griden
for row in range(3):
    for column in range(3):
        color = WHITE
        pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

# ----------------------
#         Main
# ----------------------
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.MOUSEBUTTONDOWN and winner == False:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Sätter column till maxvärdet ifall du klickar i marginalerna
            if column > 2:
                column = 2
            # Sätter row till maxvärdet ifall du klickar i marginalerna
            if row > 2:
                row = 2
            print("Click ", pos, "Grid coordinates: ", row, column)
            
            # Är det en tom ruta?
            if grid[row][column] == None:
                # Fyll rutan
                grid[row][column] = player
                # Ifall spelaren är 0 så printas X när man klickar
                if player == "x":
                    print("O turn")
                    screen.blit(x_img, (((column+1) * MARGIN + 18 + WIDTH * column), ((row+1) * MARGIN + 30 + HEIGHT * row)))
                    player = "o"
                    
 
                # Ifall spelaren är 1 så printas O när man klickar
                elif player == "o":
                    print("X turn")
                    screen.blit(o_img, (((column+1) * MARGIN + 18 + WIDTH * column), ((row+1) * MARGIN + 30 + HEIGHT * row)))
                    player = "x"
                    
            # Printar nya griden i konsollen   
            for r in grid:
                print(r)
        
        # Kollar vinnaren i x-led
        for row in range(0,3):
            if ((grid[row][0] == grid[row][1] == grid[row][2]) and (grid[row][0] != None) and winner == False):
                pygame.draw.line(screen, RED, (5, 80+row*170), (495, 80+row*170), width = 5)
                winner = True

        # Kollar vinnaren i y-led
        for column in range(0,3):
            if ((grid[0][column] == grid[1][column] == grid[2][column]) and (grid[0][column] != None) and winner == False):
                pygame.draw.line(screen, RED, (80+column*170, 5), (80+column*170, 495), width = 5)
                winner = True

        # Kollar vinnaren i vänster diagonal
        if ((grid[0][0] == grid[1][1] == grid[2][2]) and (grid[0][0] != None) and winner == False):
            pygame.draw.line(screen, RED, (5, 5), (495, 495), width = 5)
            winner = True

        # Kollar vinnaren i höger diagonal
        if ((grid[0][2] == grid[1][1] == grid[2][0]) and (grid[0][2] != None) and winner == False):
            pygame.draw.line(screen, RED, (5, 495), (495, 5), width = 5)
            winner = True

    # Skriver vems tur det är
    if winner == False:
        pygame.draw.rect(screen, BLACK, pygame.Rect(200, 550, 100, 50))
        text = FONT.render(player.upper() + "'s turn", True, RED)
        message = text.get_rect()
        message.center = (250, 570)
        screen.blit(text, message)
    else:
        if player == ("x"):
            text = FONT.render("O won!", True, RED)
        else:
            text = FONT.render("X won!", True, RED)
        pygame.draw.rect(screen, BLACK, pygame.Rect(200, 550, 100, 50))
        message = text.get_rect()
        message.center = (250, 570)
        screen.blit(text, message)
    
    pygame.display.flip()
pygame.quit()