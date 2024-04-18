import pygame
import sys
from pygame.locals import QUIT

pygame.init()
Surface = pygame.display.set_mode((600,600))
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption("Test Window")

# 폰트
myfont = pygame.font.SysFont(None,25)
message1 = myfont.render("Score : ",True,(255,255,255))
message2 = myfont.render("Combo : ",True,(255,255,255))
# 사각형처음위치
rect = [105,0,90,40]
rect1 = [405,0,90,40]
속도 = 10

def 틀():
    pygame.draw.line(Surface, (255, 255, 255), (100, 0), (100, 600), 10)
    pygame.draw.line(Surface, (255, 255, 255), (500, 0), (500, 600), 10)
    pygame.draw.line(Surface, (255, 255, 255), (200, 560), (200, 600), 10)
    pygame.draw.line(Surface, (255, 255, 255), (300, 560), (300, 600), 10)
    pygame.draw.line(Surface, (255, 255, 255), (400, 560), (400, 600), 10)

def main():
    while True:
        Surface.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        틀()
        pygame.draw.rect(Surface, (255, 0, 0), rect)
        pygame.draw.rect(Surface, (255, 0, 0), rect1)
        rect[1] += 속도
        rect1[1] += 속도

        Surface.blit(message1, (10, 10))
        Surface.blit(message2, (10, 80))

        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()