import pygame, math
def main():
    pygame.init()
    pygame.display.set_caption("Paint")
    screen = pygame.display.set_mode((800,600))
    layer = pygame.Surface((800,600))
    clock = pygame.time.Clock()
    x1 = 0
    y1 = 0
    pressed = False
    mode = ""
    color = (0,0,0)
    size = 10
    while True:
        x2 = x1
        y2 = y1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if mode == "erase" or mode == "square" or mode == "rt":
                    screen.blit(layer,(0,0))
                if event.key == pygame.K_p:
                    mode = "pen"
                elif event.key == pygame.K_LEFT:
                    mode = "erase"
                    layer.blit(screen,(0,0))
                elif event.key == pygame.K_r:
                    mode = "rect"
                elif event.key == pygame.K_c:
                    mode = "circle"
                elif event.key == pygame.K_RIGHT:
                    mode = "square"
                    layer.blit(screen,(0,0))
                elif event.key == pygame.K_KP_0:
                    mode = "rt"
                    layer.blit(screen,(0,0))
                elif event.key == pygame.K_t:
                    mode = "tr"
                elif event.key == pygame.K_q:
                    mode = "rhombus"
                if event.key == pygame.K_1:
                    color = (255,0,0)
                elif event.key == pygame.K_2:
                    color = (0,255,0)
                elif event.key == pygame.K_3:
                    color = (0,0,255)
                elif event.key == pygame.K_4:
                    color = (255,255,255)
                elif event.key == pygame.K_5:
                    color = (0,0,0)
                if event.key == pygame.K_UP and size < 100:
                    size += 10
                elif event.key == pygame.K_DOWN and size > 10:
                    size -= 10
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pressed = True
                    if mode == "rect" or mode == "circle" or mode == "tr" or mode == "rhombus":
                        q1 = x2
                        q2 = y2
                        layer.blit(screen,(0,0))
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    pressed = False
            if event.type == pygame.MOUSEMOTION:
                x2 = event.pos[0]
                y2 = event.pos[1]
        if pressed and mode == "pen":
            pygame.draw.line(screen, color, (x1,y1), (x2,y2))
        if not pressed and mode == "erase":
            screen.blit(layer,(0,0))
            pygame.draw.circle(screen, color, (x2, y2), size)
        if pressed and mode == "erase":
            pygame.draw.circle(screen, color, (x2, y2), size)
            layer.blit(screen,(0,0))
        if pressed and mode == "rect":
            screen.blit(layer,(0,0))
            pygame.draw.rect(screen, color, pygame.Rect(min(q1,x2), min(q2,y2), abs(q1-x2), abs(q2-y2)))
        if pressed and mode == "circle":
            screen.blit(layer,(0,0))
            pygame.draw.circle(screen, color, (q1,q2), math.sqrt((q1-x2)**2+(q2-y2)**2))
        if not pressed and mode == "square":
            screen.blit(layer,(0,0))
            pygame.draw.rect(screen, color, pygame.Rect(x2 - size, y2 - size, size*2, size*2))
        if pressed and mode == "square":
            pygame.draw.rect(screen, color, pygame.Rect(x2 - size, y2 - size, size*2, size*2))
            layer.blit(screen,(0,0))
        if not pressed and mode == "rt":
            screen.blit(layer,(0,0))
            pygame.draw.polygon(screen, color, [(x2,y2-size),(x2-size*math.sqrt(3)/2,y2+size/2),(x2+size*math.sqrt(3)/2,y2+size/2)])
        if pressed and mode == "rt":
            pygame.draw.polygon(screen, color, [(x2,y2-size),(x2-size*math.sqrt(3)/2,y2+size/2),(x2+size*math.sqrt(3)/2,y2+size/2)])
            layer.blit(screen,(0,0))
        if pressed and mode == "tr":
            screen.blit(layer,(0,0))
            pygame.draw.polygon(screen, color, [(q1,q2),(x2,y2),(2*q1-x2,y2)])
        if pressed and mode == "rhombus":
            screen.blit(layer,(0,0))
            pygame.draw.polygon(screen, color, [(q1,y2),(x2,q2),(q1,2*q2-y2),(2*q1-x1,q2)])
        x1 = x2
        y1 = y2
        pygame.display.update()
        clock.tick(60)
main()