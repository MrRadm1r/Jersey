import pygame
import numpy as np

# Создание изображения (800x600)
width, height = 800, 600
image_array = np.zeros((height, width, 3), dtype=np.uint8)

# Задание цвета пикселя
image_array[100, 200] = [255, 0, 0]  # Красный пиксель

# Преобразование NumPy массива в Pygame изображение
pygame_image = pygame.surfarray.make_surface(image_array)

# Пример отрисовки изображения на экране
pygame.init()
screen = pygame.display.set_mode((width, height))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    screen.blit(pygame_image, (0, 0))
    pygame.display.flip()

pygame.quit()