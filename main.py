import pygame
import sys
import os
importtime


def load_image(name, colorkey=None):
    fullname = os.path.join('data', 'snake', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Player(pygame.sprite.Sprite):
    pass


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Змейка")

    size = WIDTH, HEIGHT = 1500, 700
    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255))
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    pygame.quit()
