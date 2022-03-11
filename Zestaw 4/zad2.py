import pygame
import sys

pygame.init()


def main(x, y):
    clock = pygame.time.Clock()

    pygame.display.set_caption("Gra")

    pygame.mixer.music.load(r'music.mp3')
    pygame.mixer.music.play(-1)

    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    speed = [x, y]
    accel = [0, 9.81]
    time = 0.2

    image = pygame.image.load(r'moon.jpg')
    image = pygame.transform.scale(image, size)

    surf_center = (
        (width-image.get_width())/2,
        (height-image.get_height())/2
    )

    screen.blit(image, surf_center)

    ball = pygame.image.load(r'ball.gif')
    screen.blit(ball, (100, height/2))
    ballrect = ball.get_rect(center=(100, height/2))

    pygame.display.flip()

    if(speed[0] == 0 and speed[1] == 0):
        mode = 0
    elif(speed[1] > 0):
        speed[1] = -speed[1]
        mode = 1
        zero = False
    elif(speed[0] > 0):
        mode = 2
    else:
        speed[1] = -speed[1]
        mode = 3
        zero = False

    pygame.time.delay(1000)

    while True:
        clock.tick(60)
        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            sys.exit()

        if(mode == 0):
            speed[1] = speed[1]+accel[1]*time
        if(mode == 1):
            if(zero):
                speed[1] = speed[1]+accel[1]*time
            else:
                if(speed[1]-accel[1]*time < 0):
                    speed[1] = speed[1]+accel[1]*time
                else:
                    speed[1] = 0
                    zero = True
        if(mode == 2):
            speed[1] = speed[1]+accel[1]*time
        if(mode == 3):
            if(zero):
                speed[1] = speed[1]+accel[1]*time
            else:
                if(speed[1]-accel[1]*time < 0):
                    speed[1] = speed[1]+accel[1]*time
                else:
                    speed[1] = 0
                    zero = True

        ballrect = ballrect.move(speed)
        if ballrect.left < 0:
            speed[0] = -speed[0]
        if ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0:
            speed[1] = -speed[1]
        if ballrect.bottom > height:
            speed[1] = -speed[1]
            if(speed[1] > 0):
                speed[1] = 0
                mode = -1

        screen.blit(image, surf_center)
        screen.blit(ball, ballrect)
        pygame.display.flip()


if __name__ == '__main__':
    # Spadek swobodny
    main(0, 0)

    # Rzut pionowy
    # main(0, 35)

    # Rzut poziomy
    # main(14, 0)

    # Rzut ukoścny
    # main(15, 25)

    pygame.quit()
    sys.exit()
