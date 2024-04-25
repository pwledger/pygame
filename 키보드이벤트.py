import pygame
import sys
from pygame.locals import QUIT

pygame.init()
w = 600
h = 600
Surface = pygame.display.set_mode((w,h))
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption("Test Window")

def 틀():
    pygame.draw.line(Surface, (255, 255, 255), (100, 0), (100, 600), 10)
    pygame.draw.line(Surface, (255, 255, 255), (500, 0), (500, 600), 10)
    pygame.draw.line(Surface, (255, 255, 255), (200, 560), (200, 600), 10)
    pygame.draw.line(Surface, (255, 255, 255), (300, 560), (300, 600), 10)
    pygame.draw.line(Surface, (255, 255, 255), (400, 560), (400, 600), 10)

def main():
    maxfps = 60
    keys = [0,0,0,0]
    keyset = [0,0,0,0]
    while True:
        fps = FPSCLOCK.get_fps()
        if fps == 0:
            fps = 60
        Surface.fill((0,0,0))
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
            keys[i] += (keyset[i]-keys[i]) / (2*(maxfps/fps))

        for i in range(7):
            i += 1
            pygame.draw.rect(Surface, (0, 150 - (50 / 7) * i, 255 - ((200 / 7) * i)), (
            w / 2 - w / 3 + w / 32 - (w / 32) * keys[0], (h / 16) * 16 - (h / 30) * keys[0] * i, w / 6 * keys[0],
            (h / 35) / i))
        for i in range(7):
            i += 1
            pygame.draw.rect(Surface, (0, 150 - (50 / 7) * i, 255 - ((200 / 7) * i)), (
            w / 2 - w / 6 + w / 32 - (w / 32) * keys[1], (h / 16) * 16 - (h / 30) * keys[1] * i, w / 6 * keys[1],
            (h / 35) / i))
        for i in range(7):
            i += 1
            pygame.draw.rect(Surface, (0, 150 - (50 / 7) * i, 255 - ((200 / 7) * i)), (
            w / 2 + w / 32 - (w / 32) * keys[2], (h /16) * 16 - (h / 30) * keys[2] * i, w / 6 * keys[2],
            (h / 35) / i))
        for i in range(7):
            i += 1
            pygame.draw.rect(Surface, (0, 150 - (50 / 7) * i, 255 - ((200 / 7) * i)), (
            w / 2 + w / 6 + w / 32 - (w / 32) * keys[3], (h / 16) * 16 - (h / 30) * keys[3] * i, w /6 * keys[3],
            (h / 35) / i))


        틀()
        pygame.display.update()
        FPSCLOCK.tick(maxfps)

if __name__ == '__main__':
    main()