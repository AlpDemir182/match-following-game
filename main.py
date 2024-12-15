import pygame
pygame.init()

screen = pygame.display.set_mode((600,600))
screen.fill("light blue")
pygame.display.update()

font = pygame.font.SysFont("Arial", 30)
candycrush = pygame.image.load("Match following game/candycrush.jpg")
ludo = pygame.image.load("Match following game/ludo.png")
subwaysurfers = pygame.image.load("Match following game/subwaysurfers.png")
templerun = pygame.image.load("Match following game/templerun.png")

screen.blit(candycrush, (125, 100))
screen.blit(ludo, (125, 200))
screen.blit(subwaysurfers, (125, 300))
screen.blit(templerun, (125, 400))

text = font.render("Ludo", True, "black")
text2 = font.render("Candy Crush", True, "black")
text3 = font.render("Subway Surfers", True, "black")
text4 = font.render("Temple Run", True, "black")

screen.blit(text, (300, 425))
screen.blit(text2, (300, 325))
screen.blit(text3, (300, 125))
screen.blit(text4, (300, 225))

pygame.display.update()


while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()

        if i.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen, "black", pos, 10, 0)
            pygame.display.update()

        elif i.type == pygame.MOUSEBUTTONUP:
            pos2 = pygame.mouse.get_pos()
            pygame.draw.line(screen, "red", pos, pos2, 5)
            pygame.draw.circle(screen, "red", pos2, 10, 0)
            pygame.display.update()