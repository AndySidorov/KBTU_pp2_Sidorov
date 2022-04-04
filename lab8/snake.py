import pygame, sys, random, time
pygame.init()
pygame.display.set_caption("Snake")
screen = pygame.display.set_mode((500,400))
clock = pygame.time.Clock()
font = pygame.font.Font(None,72)
font1 = pygame.font.Font(None,32)
text = font.render("Game Over", True, (255,0,0))
text1 = font1.render("Score", True, (0,0,255))
text2 = font1.render("Level", True, (0,0,255))
score = 0
level = 0
n_walls = 2
FPS = 2
Over = False
class Snake:
    def __init__(self):
        self.body = [[10,10], [11,10], [12,10]]
        self.dx = -1
        self.dy = 0
    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.body[1][1] != self.body[0][1] - 1:
                    self.dy = -1
                    self.dx = 0
                if event.key == pygame.K_DOWN and self.body[1][1] != self.body[0][1] + 1:
                    self.dy = 1
                    self.dx = 0
                if event.key == pygame.K_RIGHT and self.body[1][0] != self.body[0][0] + 1:
                    self.dx = 1
                    self.dy = 0
                if event.key == pygame.K_LEFT and self.body[1][0] != self.body[0][0] - 1:
                    self.dx = -1
                    self.dy = 0
        for i in range (len(self.body)-1,0,-1):
            self.body[i][0] = self.body[i-1][0]
            self.body[i][1] = self.body[i-1][1]
        self.body[0][0] += self.dx
        self.body[0][1] += self.dy
        if self.body[0][0] == -1:
            self.body[0][0] = 19
        if self.body[0][0] == 20:
            self.body[0][0] = 0
        if self.body[0][1] == -1:
            self.body[0][1] = 19
        if self.body[0][1] == 20:
            self.body[0][1] = 0
    def draw(self,screen):
        x, y = self.body[0]
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(x * 20, y * 20, 20, 20))
        for q in self.body[1:]:
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(q[0] * 20, q[1] * 20, 20, 20))
    def append(self, food):
        self.body.append([food.x,food.y])
class Food:
    def __init__(self, S1, walls):
        self.x = random.randint(0,19)
        self.y = random.randint(0,19)
        i = 0
        u = 0
        while i < len(S1.body):
            while u < len(walls):
                if walls[u][0] == self.x and walls[u][1] == self.y:
                    self.x = random.randint(0,19)
                    self.y = random.randint(0,19)
                    u = 0
                else:
                    u += 1
            if S1.body[i][0] == self.x and S1.body[i][1] == self.y:
                i = 0
                self.x = random.randint(0,19)
                self.y = random.randint(0,19)
            else:
                i += 1
    def draw(self, screen):
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(self.x*20,self.y*20,20,20))
    def new(self, S1, walls):
        self.x = random.randint(0,19)
        self.y = random.randint(0,19)
        i = 0
        u = 0
        while i < len(S1.body):
            while u < len(walls):
                if walls[u][0] == self.x and walls[u][1] == self.y:
                    self.x = random.randint(0,19)
                    self.y = random.randint(0,19)
                    u = 0
                else:
                    u += 1
            if S1.body[i][0] == self.x and S1.body[i][1] == self.y:
                i = 0
                self.x = random.randint(0,19)
                self.y = random.randint(0,19)
            else:
                i += 1
def Wall(S1, F1, walls):
    x = random.randint(0,19)
    y = random.randint(0,19)
    i = 0
    u = 0
    while i < len(S1.body):
        while u < len(walls):
            if walls[u][0] == x and walls[u][1] == y:
                x = random.randint(0,19)
                y = random.randint(0,19)
                u = 0
            else:
                u += 1
        if (S1.body[i][0] == x and S1.body[i][1] == y) or (F1.x == x and F1.y == y):
            i = 0
            x = random.randint(0,19)
            y = random.randint(0,19)
        else:
            i += 1
    return [x,y]
def draw(i, screen):
    pygame.draw.rect(screen, (165,42,42), pygame.Rect(i[0]*20,i[1]*20,20,20))
def Grid(screen):
    for x in range(0, 400, 20):
        for y in range(0, 400, 20):
            pygame.draw.rect(screen, (60, 60, 60), pygame.Rect(x, y, 20, 20), 1)
S1 = Snake()
walls = []
F1 = Food(S1, walls)
walls.append(Wall(S1, F1, walls))
while True:
    screen.fill((0,0,0))
    Grid(screen)
    S1.move()
    S1.draw(screen)
    if S1.body[0][0] == F1.x and S1.body[0][1] == F1.y:
        score += 1
        F1.new(S1, walls)
        S1.append(F1)
    for i in range(1,len(S1.body)):
        if S1.body[0][0] == S1.body[i][0] and S1.body[0][1] == S1.body[i][1]:
            Over = True
    for i in walls:
        if S1.body[0][0] == i[0] and S1.body[0][1] == i[1]:
            Over = True
    if Over: 
        screen.fill((0,0,0))
        screen.blit(text,(250-text.get_width()//2,200-text.get_height()//2))
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()
    F1.draw(screen)
    level = score//4
    FPS = 2 + level
    if level == n_walls:
        n_walls += 2
        walls.append(Wall(S1,F1,walls))
    for i in walls:
        draw(i, screen)
    Score = font.render(str(score), True, (0,0,255))
    Level = font.render(str(level+1), True, (0,0,255))
    screen.blit(Score,(450-Score.get_width()//2,130-Score.get_height()//2))
    screen.blit(Level,(450-Level.get_width()//2,330-Level.get_height()//2))
    screen.blit(text1,(450-text1.get_width()//2,50-text1.get_height()//2))
    screen.blit(text2,(450-text2.get_width()//2,250-text2.get_height()//2))
    pygame.display.update()
    clock.tick(FPS)