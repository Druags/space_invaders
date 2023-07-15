import pygame
import random

# Настройки окна
WIDTH = 500
HEIGHT = 500
FPS = 60

# Настройка цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Инициализация
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Время
lastTime = 0
currentTime = 0

main_character_img = pygame.image.load('image/razorinv.png')
main_character_rect = main_character_img.get_rect(top=400, left=200)

# захватчики
invader_img = pygame.image.load('image/invaderinv.png')
invaders = []  # в списке будут храниться все захватчики
invader_cd = 2000  # с такой очередёностью(миллисекунды) появляются захватчики
invader_last_time = 0  # последнее время появления захватчика
current_time = 0  # текущее время в игре

# Пули
wb = 2
hb = 5
bullet_img = pygame.image.load("image/bullet.png")
bullets = []
isShot = False

speed = 5
moving = ''
running = True
while running:
    screen.fill('black')
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False

    # создание пришельцев
    current_time = pygame.time.get_ticks()
    if current_time-invader_last_time>invader_cd:
        invaders.append(invader_img.get_rect(topleft=(random.randint(0, WIDTH-70),-50)))
        invader_last_time = current_time

    for invader in invaders:
        screen.blit(invader_img, invader)
        invader.top+= 5

    keys = pygame.key.get_pressed()
    # передвижение
    if keys[pygame.K_LEFT]:
        main_character_rect.left -= speed
    elif keys[pygame.K_RIGHT]:
        main_character_rect.left += speed
    # стрельба
    if keys[pygame.K_SPACE]:
        isShot = True

    if isShot:
        bullets.append(pygame.Rect(main_character_rect.left, main_character_rect.top, wb, hb))
        isShot = False

    for bullet in bullets:
        bullet.top -= 10
        screen.blit(bullet_img, bullet)
        if bullet.bottom < 0:
            bullets.remove(bullet)

    screen.blit(main_character_img, main_character_rect)
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()