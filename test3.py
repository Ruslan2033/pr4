import pygame # імпорт бібліотеки Pygame
pygame.init()  # ініціалізація бібліотеки Pygame
import random
font = pygame.font.Font(None,24)
text = font.render("Tекст",True,(0,0,0))



window= pygame.display.set_mode((500, 500))  # створення вікна гри розміром 500x500 пікселів
window.blit(text,(40,40))
player1 = pygame.Rect(50,250,50,50)
player2 = pygame.Rect(150,250,50,50)
player3 = pygame.Rect(250,250,50,50)
player4 = pygame.Rect(350,250,50,50)

clock = pygame.time.Clock()  # створення об'єкту годинника для керування частотою кадрів
game = True  # змінна, що вказує, чи триває гра

while game:

    window.fill((255, 0, 0))  # заповнення вікна червоним кольором.
    pygame.draw.rect(window,(0,0,0),player1)
    pygame.draw.rect(window,(0,0,0),player2)
    pygame.draw.rect(window,(0,0,0),player3)
    pygame.draw.rect(window,(0,0,0),player4)

    for event in pygame.event.get():  # обробка подій гри.
        if event.type == pygame.QUIT:  # перевірка, чи не було натиснуто кнопку закриття вікна
            game = False  # завершення головного циклу гри
    clock.tick(30)  # встановлення частоти кадрів секунду
    pygame.display.update()  # оновлення 