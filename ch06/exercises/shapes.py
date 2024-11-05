import pygame

pygame.init()
pygame.event.pump()
screen = pygame.display.set_mode((600, 600))

screen.fill("white")
pygame.display.flip()
pygame.draw.circle(screen, "black", [200, 350], 50)
pygame.draw.circle(screen, "white", [200, 350], 49)
pygame.display.flip
pygame.draw.circle(screen, "black", [200, 280], 35)
pygame.draw.circle(screen, "white", [200, 280], 34)
pygame.display.flip()
pygame.draw.circle(screen, "black", [200, 230], 25)
pygame.draw.circle(screen, "white", [200, 230], 24)
pygame.display.flip()
pygame.time.wait(1000)