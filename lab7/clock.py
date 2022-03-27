import pygame
import os
import datetime
import math
images = [r'images\Clock.jpg', r'images\Long hand.jpg', r'images\Short hand.jpg']
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
    
    w2, h2 = pic2.get_size()
    box2 = [pygame.math.Vector2(p) for p in [(0, 0), (w2, 0), (w2, -h2), (0, -h2)]]
    box2_rotate = [p.rotate(-(6 * now.second+180)) for p in box2]
    min_box2 = (min(box2_rotate, key=lambda p: p[0])[0], min(box2_rotate, key=lambda p: p[1])[1])
    max_box2 = (max(box2_rotate, key=lambda p: p[0])[0], max(box2_rotate, key=lambda p: p[1])[1])
    origin2 = (350 + min_box2[0], 350 - max_box2[1])
    image2 = pygame.transform.rotate(pic2, -(6 * now.second + 180))

    w3, h3 = pic3.get_size()
    box3 = [pygame.math.Vector2(p) for p in [(0, 0), (w3, 0), (w3, -h3), (0, -h3)]]
    box3_rotate = [p.rotate(-(6 * now.minute + 180)) for p in box3]
    min_box3 = (min(box3_rotate, key=lambda p: p[0])[0], min(box3_rotate, key=lambda p: p[1])[1])
    max_box3 = (max(box3_rotate, key=lambda p: p[0])[0], max(box3_rotate, key=lambda p: p[1])[1])
    origin3 = (350 + min_box3[0], 350 - max_box3[1])
    image3 = pygame.transform.rotate(pic3, -(6 * now.minute + 180))

    screen.blit(image2, origin2)
    screen.blit(image3, origin3)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True