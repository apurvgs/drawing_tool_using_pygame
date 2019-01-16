import pygame
from pygame.locals import *

pos=0

def event_handler(game_display):
    #print(len(pygame.event.get()))
    global pos
    for event in pygame.event.get():
        #print(event)
        if event.type == MOUSEBUTTONUP:
            pos=1-pos
            mouse_position = pygame.mouse.get_pos()
            pygame.draw.line(game_display, (255, 255, 255), (mouse_position[0], mouse_position[1]),(mouse_position[0], mouse_position[1]))
            continue
        if event.type == pygame.MOUSEMOTION and pos:
            mouse_position = pygame.mouse.get_pos()
            pygame.draw.line(game_display, (255, 255, 255), (mouse_position[0], mouse_position[1]), (mouse_position[0], mouse_position[1]))
        if event.type == QUIT or (
             event.type == KEYDOWN and (
              event.key == K_ESCAPE or
              event.key == K_q
             )):
            pygame.quit()
            quit()


i=pygame.init()

game_display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Simple drawing tool')


while True:
    event_handler(game_display)
    pygame.display.update()
