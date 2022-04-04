import pygame
def draw(screen, index, start, end, size, color, shape):
    c1 = max(0, min(255,2*index-256))
    c2 = max(0, min(255,2*index))
    if color == "red":
        paint = (c2,c1,c1)
    if color == "green":
        paint = (c1,c2,c1)
    if color == "blue":
        paint = (c1,c1,c2)
    if color == "white":
        paint = (c2,c2,c2)
    if end[2] == -1:
        paint = ((0,0,0))
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    it = max(abs(dx), abs(dy))
    for i in range(it):
        progress = 1.0 * i / it
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * start[1])
        if shape == "circle":
            pygame.draw.circle(screen, paint, (x, y), size)
        elif shape == "rect":
            pygame.draw.rect(screen, paint, pygame.Rect(x - size, y - size, size * 2, size * 2))
def main():
    pygame.init()
    pygame.display.set_caption("Paint")
    screen = pygame.display.set_mode((600,600))
    clock = pygame.time.Clock()
    points = []
    erase = []
    shape = "circle"
    color = "red"
    mode = 1
    size = 15
    while True:
        screen.fill((0,0,0))
        pressed = pygame.key.get_pressed()
        alt = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl:
                    return
                if event.key == pygame.K_F4 and alt:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_1:
                    color = "red"
                elif event.key == pygame.K_2:
                    color = "green"
                elif event.key == pygame.K_3:
                    color = "blue"
                elif event.key == pygame.K_4:
                    color = "white"
                elif event.key == pygame.K_e:
                    mode *= -1
                if event.key == pygame.K_LEFT:
                    shape = "circle"
                elif event.key == pygame.K_RIGHT:
                    shape = "rect"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    size = min(200, size + 1)
                if event.button == 3:
                    size = max(1, size - 1)
            if event.type == pygame.MOUSEMOTION:
                pos = [event.pos[0]] + [event.pos[1]] + [mode]
                points.append(pos)
                points = points[-256:] 
        i = 0
        while i < len(points) - 1:
            draw(screen, i, points[i], points[i+1], size, color, shape)
            i += 1
        pygame.display.update()
        clock.tick(60)
main()