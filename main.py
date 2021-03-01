# импортируем модули
import pygame
import sys
import os
import random


def load_image(name):
    fullname = os.path.join("data", name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


# класс главного игрока
class Ship(pygame.sprite.Sprite):
    image_ship = load_image("ship.png")

    def __init__(self, sprite):
        super().__init__(sprite)
        self.image = Ship.image_ship
        self.rect = self.image.get_rect()
        self.rect.x = 410
        self.rect.y = 500

    def update(self, change):
        global x
        # проверка на то, чтобы игрок не заходил за границы
        if change > 0 and self.rect.x < 786:
            self.rect.x += change
            x += change
        elif change < 0 and self.rect.x > 10:
            self.rect.x += change
            x += change


# класс метеоритов
class Enemy(pygame.sprite.Sprite):
    image_enemy = load_image("meteor.png")

    def __init__(self, all_sprite):
        super().__init__(all_sprite)
        self.image = Enemy.image_enemy
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(10, 830)
        self.rect.y = -44

    def update(self):
        self.rect.y += 5


# класс для выстрелов
class Shot(pygame.sprite.Sprite):
    image_shot = pygame.transform.scale(load_image("shot.png"), (20, 50))

    def __init__(self, all_sprite, x1):
        super().__init__(all_sprite)
        self.image = Shot.image_shot
        self.rect = self.image.get_rect()
        self.rect.x = x1
        self.rect.y = 500

    def update(self, sprite):
        self.rect.y -= 10
        # проверка на пересечение пуль и метеоритов
        enemy1 = pygame.sprite.spritecollideany(self, sprite)
        if enemy1:
            self.kill()
            enemy1.kill()


SCORE = 0  # счет в игре
x = 448  # начальное положение луча (пули)


class Star(pygame.sprite.Sprite):
    image_star = pygame.transform.scale(load_image("star.png"), (30, 30))

    def __init__(self, all_sprite):
        super().__init__(all_sprite)
        self.image = Star.image_star
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(10, 830)
        self.rect.y = -44

    def update(self, sprite):
        global SCORE
        self.rect.y += 3
        # проверка на пересечение игрока и звезд
        star = pygame.sprite.spritecollideany(self, sprite)
        if star:
            self.kill()
            SCORE += 1


def main():
    global x
    pygame.init()
    pygame.display.set_caption("Space wars")
    # pygame.mouse.set_visible(False)

    size = width, height = 900, 600
    screen = pygame.display.set_mode(size)
    fon = pygame.transform.scale(load_image("fon.jpg"), (width, height))  # фон игры
    screen.blit(fon, (-1, 0))

    Ship_sprite = pygame.sprite.Group()
    ship = Ship(Ship_sprite)

    Enemy_sprite = pygame.sprite.Group()
    Enemy(Enemy_sprite)

    Shot_sprite = pygame.sprite.Group()

    Star_sprite = pygame.sprite.Group()

    fps = 60
    clock = pygame.time.Clock()

    flg = False
    key = None
    change = None
    i = 1
    a = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    change = -5
                    key = event.key
                    flg = True
                elif event.key == pygame.K_d:
                    change = 5
                    key = event.key
                    flg = True
            elif event.type == pygame.KEYUP:
                if event.key == key:
                    flg = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Shot(Shot_sprite, x)
        if flg:
            Ship_sprite.update(change)

        for i in range(int(i)):
            Enemy(Enemy_sprite)
            Star(Star_sprite)

        i += a
        a += 1 / 20000

        screen.blit(fon, (-1, 0))
        clock.tick(fps)

        Enemy_sprite.update()
        Shot_sprite.update(Enemy_sprite)
        Star_sprite.update(Ship_sprite)

        Star_sprite.draw(screen)
        Ship_sprite.draw(screen)
        Enemy_sprite.draw(screen)
        Shot_sprite.draw(screen)

        if pygame.sprite.spritecollideany(ship, Enemy_sprite):
            return finish()

        font = pygame.font.Font(None, 30)
        string_rendered = font.render(f"Счет: {SCORE}", 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        intro_rect.top = 570
        intro_rect.x = 10
        screen.blit(string_rendered, intro_rect)

        pygame.display.flip()
    pygame.quit()


# начальный экран
def start():
    im("fon2.jpg")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return main()
                elif event.key == pygame.K_RETURN:
                    return training1()
        pygame.display.flip()
    pygame.quit()


# заставка в конце игры
def finish():
    global SCORE
    im("fon5.jpg", SCORE)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return start()
        pygame.display.flip()
    pygame.quit()


# обучение
def training1():
    im("fon1.jpg")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return training2()
        pygame.display.flip()
    pygame.quit()


def training2():
    im("fon3.jpg")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return training3()
        pygame.display.flip()
    pygame.quit()


def training3():
    im("fon4.jpg")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return start()
        pygame.display.flip()
    pygame.quit()


def im(name, r=None):
    pygame.init()
    pygame.display.set_caption("Space wars")
    # pygame.mouse.set_visible(False)

    size = width, height = 900, 600
    screen = pygame.display.set_mode(size)
    fon = pygame.transform.scale(load_image(name), (width, height))
    screen.blit(fon, (-1, 0))

    if r is not None:
        font = pygame.font.Font(None, 100)
        string_rendered = font.render(f"{r}", 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        intro_rect.top = 320
        intro_rect.x = 410
        screen.blit(string_rendered, intro_rect)


start()
