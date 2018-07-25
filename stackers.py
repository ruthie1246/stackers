from sense_hat import SenseHat
from pygame.locals import *
import pygame
import time
#this script demonstrates how to create a class structure for gaming mode
sense = SenseHat()
sense.clear()

blue = (0, 0, 255)

class stack():
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((640, 480))
        self.gaming = True

    def startGame(self):
        pygame.time.set_timer(USEREVENT +1, 400)
        x = 0
        y = 7
        while self.gaming:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    sense.set_pixel(x-1, y, blue)
                    y -= 1                    
                    if y < 0:
                        self.gaming = False

                else:
                    sense.set_pixel(x, y, blue)
                    time.sleep(0.3)
                    sense.set_pixel(x, y, (0,0,0))
                    x += 1
                    if x == 8:
                        x = 0

if __name__ == "__main__":
    try:
        game = stack()
        game.startGame()
    except KeyboardInterrupt:
        sense.clear()
