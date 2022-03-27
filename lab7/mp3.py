import pygame
import os
songs = [r'music\Foo Fighters - The Pretender.mp3', 
r'music\Gorillaz - Feel Good Inc.mp3', r'music\Linkin Park - New Divide.mp3', 
r'music\Nirvana - Come As You Are.mp3', r'music\Queen - Another One Bites The Dust.mp3']
for x in songs:
    x = x.replace('/', os.sep).replace('\\',os.sep)
def play_next():
    global songs
    songs = songs[1:] + [songs[0]]
    pygame.mixer.music.load(songs[0])
    pygame.mixer.music.play()
def play_prev():
    global songs
    songs = [songs[len(songs)-1]]+songs[0:len(songs)-1] 
    pygame.mixer.music.load(songs[0])
    pygame.mixer.music.play()
pygame.init()
screen = pygame.display.set_mode((375,425))
done = False
clock = pygame.time.Clock()
font = pygame.font.Font(None, 75)
text1 = font.render("UP", False, (128,128,128))
text2 = font.render("DOWN", False, (128,128,128))
text3 = font.render("RIGHT", False, (128,128,128))
text4 = font.render("LEFT", False, (128,128,128))
SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load(songs[0])
pygame.mixer.music.play()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pygame.mixer.music.unpause()
            if event.key == pygame.K_DOWN:
                pygame.mixer.music.pause()
            if event.key == pygame.K_LEFT:
                play_prev()
            if event.key == pygame.K_RIGHT:
                play_next()
        if event.type == SONG_END:
            play_next()
        pygame.draw.line(screen, (0,0,153), (135, 50), (135,365), 10)
        pygame.draw.polygon(screen, (128,128,128), [(60,50),(60,100),(85,75)])
        pygame.draw.line(screen, (128,128,128), (60, 140), (60,190), 10)
        pygame.draw.line(screen, (128,128,128), (80, 140), (80,190), 10)
        pygame.draw.line(screen, (128,128,128), (50, 250), (80,250), 10)
        pygame.draw.polygon(screen, (128,128,128), [(80,225),(80,275),(105,250)])
        pygame.draw.line(screen, (128,128,128), (75, 340), (105,340), 10)
        pygame.draw.polygon(screen, (128,128,128), [(75,315),(75,365),(50,340)])
        screen.blit(text1, (250 - text1.get_width() // 2, 75 - text1.get_height() // 2))
        screen.blit(text2, (250 - text2.get_width() // 2, 170 - text2.get_height() // 2))
        screen.blit(text3, (250 - text3.get_width() // 2, 255 - text3.get_height() // 2))
        screen.blit(text4, (250 - text4.get_width() // 2, 340 - text4.get_height() // 2))
        pygame.display.flip()
        clock.tick(10)