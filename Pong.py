## write pong in  python
import time
import os
import random
import sys
import pygame
from pygame.locals import *
# write the tikinter 800 x00 arcade gba window
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Pong')
# write the background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))
# write the font
font = pygame.font.Font(None, 36)
# generate the ai
class AI(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 50))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.centerx = 790
        self.rect.centery = 300
        self.speed = 10
    def update(self):
        if self.rect.centery < ball.rect.centery:
            self.rect.centery += self.speed
        if self.rect.centery > ball.rect.centery:
            self.rect.centery -= self.speed
            ## make the ball bounce
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.centery = 300
        self.speed = 10
        self.x_speed = 10
        self.y_speed = 10
    def update(self):
        self.rect.centerx += self.x_speed
        self.rect.centery += self.y_speed
        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.y_speed = -self.y_speed
        if self.rect.left <= 0 or self.rect.right >= 800:
            self.x_speed = -self.x_speed
        if self.rect.colliderect(player.rect):
            self.x_speed = -self.x_speed
        if self.rect.colliderect(ai.rect):
            self.x_speed = -self.x_speed
# write the player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 50))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.centerx = 10
        self.rect.centery = 300
        self.speed = 10
    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.rect.centery -= self.speed
        if key[pygame.K_s]:
            self.rect.centery += self.speed
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 600:
            self.rect.bottom = 600
# write the score
class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.image = self.font.render(str(self.score), 1, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.centery = 50
        ## make the ai for the score
class AIScore(Score):
    def __init__(self):
        Score.__init__(self)
        self.rect.centerx = 700
        self.rect.centery = 50
    def update(self):
        self.image = self.font.render(str(self.score), 1, (255, 255, 255))
        if ball.rect.left <= 0:
            ai.score += 1
            ball.rect.centerx = 400
            ball.rect.centery = 300
            ball.x_speed = -ball.x_speed
        if ball.rect.right >= 800:
            player.score += 1
            ball.rect.centerx = 400
            ball.rect.centery = 300
            ball.x_speed = -ball.x_speed
# write the main
def main():
    global screen, background, font, player, ai, ball, score
    screen.blit(background, (0, 0))
    player = Player()
    ai = AI()
    ball = Ball()
    score = Score()
    playersprites = pygame.sprite.RenderPlain((player))
    aisprites = pygame.sprite.RenderPlain((ai))
    ballsprites = pygame.sprite.RenderPlain((ball))
    scoresprites = pygame.sprite.RenderPlain((score))
    clock = pygame.time.Clock()
    while 1:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        screen.blit(background, (0, 0))
        playersprites.update()
        aisprites.update()
        ballsprites.update()
        scoresprites.update()
        playersprites.draw(screen)
        aisprites.draw(screen)
        ballsprites.draw(screen)
        scoresprites.draw(screen)

        # make the class for the score
        class AIScore(Score):
            def __init__(self):
                Score.__init__(self)
                self.rect.centerx = 700
                self.rect.centery = 50

            def update(self):
                self.image = self.font.render(str(self.score), 1, (255, 255, 255))
                if ball.rect.left <= 0:
                    ai.score += 1
                    ball.rect.centerx = 400
                    ball.rect.centery = 300
                    ball.x_speed = -ball.x_speed
                if ball.rect.right >= 800:
                    player.score += 1
                    ball.rect.centerx = 400
                    ball.rect.centery = 300
                    ball.x_speed = -ball.x_speed
        pygame.display.flip()

        ## make the ai when the ball misses the paddle at the edge of the screen the ai gets a point
        if ball.rect.left <= 0:
            ai.score += 1
            ball.rect.centerx = 400
            ball.rect.centery = 300
            ball.x_speed = -ball.x_speed
            ## if you get to the ais edge you get a point
        if ball.rect.right >= 800:
            player.score += 1
            ball.rect.centerx = 400
            ball.rect.centery = 300
            ball.x_speed = -ball.x_speed
if __name__ == '__main__': main()