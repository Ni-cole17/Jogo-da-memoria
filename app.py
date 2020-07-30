import sys
print(sys.path)
import pygame
import game_config as gc
from animal import Animal
from time import sleep

from pygame import display, event, image

def find_index(x,y):
    row = y // gc.IMAGE_SIZE
    col = x // gc.IMAGE_SIZE
    index = row * gc.NUM_TITLES_SIDE + col
    return index

pygame.init()

display.set_caption('Jogo da Memória')

screen = display.set_mode((512,512))

matched = image.load('other_assets/matched.png')
###msg = "No matched!!!"

running = True
tiles = [Animal(i) for i in range(0, gc.NUM_TITLES_TOTAL)]
current_images = []

while running:
    current_events = event.get()

    for e in current_events:
        if e.type == pygame.QUIT:
            running = False

        if e.type == pygame.KEYDOWN:
            if e.key ==  pygame.K_ESCAPE:
                running = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            index = find_index(mouse_x,mouse_y)
            current_images.append(index)
            if len(current_images) > 2:
                current_images = current_images[2:]


    screen.fill((255,255,255))

    total_skipped = 0

    for i,tile in enumerate(tiles):
        images_i = tile.image if tile.index in current_images else tile.box
        if not tile.skip:
            screen.blit(images_i, (tile.col * gc.IMAGE_SIZE + gc.MARGIN, tile.row * gc.IMAGE_SIZE + gc.MARGIN))
        else:
            total_skipped +=1
    
    if len(current_images) == 2:
        idx1, idx2 = current_images
        if (tiles[idx1].name == tiles[idx2].name) and (idx1 != idx2):
            tiles[idx1].skip = True
            tiles[idx2].skip = True
            sleep(0.3)
            screen.blit(matched, (0,0))
            display.flip()
            sleep(0.3)
            current_images = []
        ###else:
        ##    screen.blit(msg, (0,0))
        ##    display.flip()
        ##    sleep(0.3)

    if total_skipped == len(tiles):
        running = False

    display.flip()

print("Até Logo!!")