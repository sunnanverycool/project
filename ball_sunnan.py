import pygame
screen=pygame.display.set_mode((600,700))
a=1
b=1
screen.fill((123,234,213))
image=pygame.image.load('dino.png')
position=image.get_rect()
print(position)
while 1:
    position=position.move([a,b])
    screen.fill((123, 234, 213))
    screen.blit(image,position)
    if position.right>=600:
        a=-1
    if position.left <= 0:
        a = 1
    if position.top<=0:
        b=1
    if position.bottom>=700:
        b=-1
    pygame.display.update()
while 1:
    pass