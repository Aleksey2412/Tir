import pygame
import random
import os

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
TARGET_RADIUS = 30

# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Тир")

# Загрузка звука
if os.path.exists("shot.wav"):
    shot_sound = pygame.mixer.Sound("shot.wav")
else:
    shot_sound = None


# Функция для создания новой мишени
def new_target():
    return {
        "x": random.randint(TARGET_RADIUS, WIDTH - TARGET_RADIUS),
        "y": random.randint(TARGET_RADIUS, HEIGHT - TARGET_RADIUS)
    }


target = new_target()
score = 0
running = True

# Игровой цикл
while running:
    screen.fill(WHITE)

    # Отрисовка мишени
    pygame.draw.circle(screen, RED, (target["x"], target["y"]), TARGET_RADIUS)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            dist = ((mx - target["x"]) ** 2 + (my - target["y"]) ** 2) ** 0.5
            if dist <= TARGET_RADIUS:
                if shot_sound:
                    shot_sound.play()
                score += 1
                target = new_target()

    # Обновление экрана
    pygame.display.flip()

# Завершение Pygame
pygame.quit()
