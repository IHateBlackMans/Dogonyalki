from pygame import *
mv = display.set_mode((700, 500))
display.set_caption('БОБИК')
bg = transform.scale(image.load('cartinka.png'), (700,500))
sprite1 = transform.scale(image.load('svinka.png'), (150, 150))
sprite2 = transform.scale(image.load('zombienice.png'), (150,150))
x1 = 100
y1 = 300
x2 = 500
y2 = 300
while True:
    for e in event.get():
        if e.type == QUIT:
            exit()
    mv.blit(bg, (0,0))
    mv.blit(sprite1, (x1,y1))
    mv.blit(sprite2, (x2,y2))
    keys = key.get_pressed()
    if keys[K_a] and x1 > 0:
        x1 -= 3
    if keys[K_d] and x1 < 600:
        x1 += 3
    if keys[K_w] and y1 > 0:
        y1 -= 3
    if keys[K_s] and y1 < 400:
        y1 += 3
    if x1 < x2:
        x2 -= 2
    if x1 > x2:
        x2 += 2
    if y1 < y2:
        y2 -= 2
    if y1 > y2:
        y2 += 2
    display.update()
    time.delay(10)