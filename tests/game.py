import pygame
import sys

# Инициализация Pygame
pygame.init()

# Установка размеров экрана
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Отображение текста при нажатии клавиши F3")

# Установка цветов
black = (0, 0, 0)
white = (255, 255, 255)

# Создание объекта шрифта
font = pygame.font.Font(None, 36)  # Используется шрифт по умолчанию размером 36

# Переменная для отслеживания состояния клавиши F3
f3_pressed = False

# Основной цикл программы
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Обработка событий клавиш
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F3 and not f3_pressed:
                print("yes")
                f3_pressed = True
            elif event.key == pygame.K_F3 and f3_pressed:
                f3_pressed = False

    # Очистка экрана
    screen.fill(black)

    # Создание текстовой строки, если f3_pressed равен True
    if f3_pressed:
        text_surface = font.render("yes", True, white)
        text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text_surface, text_rect)

    # Обновление экрана
    pygame.display.flip()
