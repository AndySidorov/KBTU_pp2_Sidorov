import pygame
import os
import datetime
images = [r'images\Clock.png', r'images\Long hand.png', r'images\Short hand.png']
for x in images:
    x = x.replace('/', os.sep).replace('\\', os.sep)
pygame.init()
screen = pygame.display.set_mode((700,700))
done = False
x = 1
pic1 = pygame.image.load(images[0])
pic2 = pygame.image.load(images[1])
pic3 = pygame.image.load(images[2])
while not done:
    screen.fill((255,255,255))
    screen.blit(pic1,(1,1))
    now = datetime.datetime.now()
    newpic2 = pygame.transform.rotate(pic2, -6*now.second)
    newpic3 = pygame.transform.rotate(pic3, -6*now.minute)
    rect2 = newpic2.get_rect(center = pic2.get_rect(center = (350,350)).center)
    rect3 = newpic3.get_rect(center = pic3.get_rect(center = (350,350)).center)
    screen.blit(newpic2, rect2)
    screen.blit(newpic3, rect3)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True