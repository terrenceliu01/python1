import pygame
import time
import turtle

pygame.font.init()
screen = pygame.display.set_mode((800,600))
background = (0, 0, 0)
screen.fill((background))
myfont = pygame.font.Font(None, 90)
f = open("./turtle/names.txt","r")
names = []
for line in f:
    # for word in line.split():
    names.append(line)

flag = True
index = 0
while flag:
    text = myfont.render(names[index],1,(0,255,0))
    screen.blit(text, (50,300))
    pygame.display.update()
    time.sleep(0.1)
    screen.fill((background))
    pygame.display.update()
    index +=1
    if index >=len(names):
        index = 0

pygame.display.quit()