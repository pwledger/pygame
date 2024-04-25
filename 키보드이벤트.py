import pygame
import sys
from pygame.locals import QUIT

pygame.init()
w = 600
h = 600
Surface = pygame.display.set_mode((w,h))
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
# 키 동작 모양
keys= [0,0,0,0]
keyset = [0,0,0,0]
maxfps = 60


def 틀():
    pygame.draw.line(Surface, (255, 255, 255), (100, 0), (100, 600), 10)
    pygame.draw.line(Surface, (255, 255, 255), (500, 0), (500, 600), 10)
    pygame.draw.line(Surface, (255, 255, 255), (200, 560), (200, 600), 10)
    pygame.draw.line(Surface, (255, 255, 255), (300, 560), (300, 600), 10)
    pygame.draw.line(Surface, (255, 255, 255), (400, 560), (400, 600), 10)

def main():
    while True:
        Surface.fill((0,0,0))
        fps = FPSCLOCK.get_fps()
        if fps == 0:
            fps = maxfps
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    keyset[0] = 1
                if event.key == pygame.K_f:
                    keyset[1] = 1
                if event.key == pygame.K_j:
                    keyset[2] = 1
                if event.key == pygame.K_k:
                    keyset[3] = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    keyset[0] = 0
                if event.key == pygame.K_f:
                    keyset[1] = 0
                if event.key == pygame.K_j:
                    keyset[2] = 0
                if event.key == pygame.K_k:
                    keyset[3] = 0
        for i in range(4):
            keys[i] += (keyset[i] - keys[i]) / (2 * (maxfps /fps))
        for i in range(7):
            i += 1
            pygame.draw.rect(Surface, (0, 150 - (50 / 7) * i, 255 - ((200 / 7) * i)), (
            w / 2 - w / 8 + w / 32 - (w / 32) * keys[0], (h / 24) * 16 - (h / 30) * keys[0] * i, w / 16 * keys[0],
            (h / 35) / i))
        for i in range(7):
            i += 1
            pygame.draw.rect(Surface, (0, 150 - (50 / 7) * i, 255 - ((200 / 7) * i)), (
            w / 2 - w / 16 + w / 32 - (w / 32) * keys[1], (h / 24) * 16 - (h / 30) * keys[1] * i, w / 16 * keys[1],
            (h / 35) / i))
        for i in range(7):
            i += 1
            pygame.draw.rect(Surface, (0, 150 - (50 / 7) * i, 255 - ((200 / 7) * i)), (
            w / 2 + w / 32 - (w / 32) * keys[2], (h / 24) * 16 - (h / 30) * keys[2] * i, w / 16 * keys[2],
            (h / 35) / i))
        for i in range(7):
            i += 1
            pygame.draw.rect(Surface, (0, 150 - (50 / 7) * i, 255 - ((200 / 7) * i)), (
            w / 2 + w / 16 + w / 32 - (w / 32) * keys[3], (h / 24) * 16 - (h / 30) * keys[3] * i, w / 16 * keys[3],
            (h / 35) / i))


        틀()
        pygame.draw.rect(Surface, (255, 0, 0), rect)
        pygame.draw.rect(Surface, (255, 0, 0), rect1)
        rect[1] += 속도
        rect1[1] += 속도

        Surface.blit(message1, (10, 10))
        Surface.blit(message2, (10, 80))

        pygame.display.update()
        FPSCLOCK.tick(maxfps)

if __name__ == '__main__':
    main()