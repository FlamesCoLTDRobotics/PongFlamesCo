## make pong
import pygame
import random
import numpy as np
import time

# Initialize the game 
pygame.init()
width, height = 500, 500
pygame.display.set_caption("Pong 1.0 by Blitz LTD")
screen = pygame.display.set_mode((height, width))

# Paddle A
paddle_a = pygame.Rect(0, 0, 10, 100)
paddle_a.center = (20, height / 2)

# Paddle B
paddle_b = pygame.Rect(0, 0, 10, 100)
paddle_b.center = (width - 20, height / 2)

# Ball
ball = pygame.Rect(0, 0, 10, 10)
ball.center = (width / 2, height / 2)

# Speed of the ball
ball_speed_x = 3 * random.choice((1, -1))
ball_speed_y = 3 * random.choice((1, -1))

# Color of the paddles and ball
color = (255, 255, 255)

# Font
font = pygame.font.Font(None, 50)

# Score
score_a = 0
score_b = 0

# Game loop
while True:
    # Slow down the code
    time.sleep(0.01)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Move the paddles with the mouse
    paddle_a.y = pygame.mouse.get_pos()[1]
    paddle_b.y = pygame.mouse.get_pos()[1]

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Bounce the ball if needed
    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1
    # Bounce the ball if hits the paddles
    if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
        ball_speed_x *= -1

    # Check if the ball is out of the screen
    if ball.left <= 0:
        score_b += 1
        ball_speed_x = 3 * random.choice((1, -1))
        ball_speed_y = 3 * random.choice((1, -1))
        ball.center = (width / 2, height / 2)
    if ball.right >= width:
        score_a += 1
        ball_speed_x = 3 * random.choice((1, -1))
        ball_speed_y = 3 * random.choice((1, -1))
        ball.center = (width / 2, height / 2)

    # Draw the score
    score_text = font.render(f"{score_a} : {score_b}", True, color)
    screen.blit(score_text, (width / 2 - score_text.get_width() / 2, 20))

    # Draw the game
    if ball.left <= 0 or ball.right >= width:
        ball_speed_x *= -1

    # Draw the game
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, color, paddle_a)
    pygame.draw.rect(screen, color, paddle_b)
    pygame.draw.ellipse(screen, color, ball)
    pygame.draw.aaline(screen, color, (width / 2, 0), (width / 2, height))
    pygame.display.flip()

    # Draw the score
    score_text = font.render(f"{score_a} : {score_b}", True, color)
    screen.blit(score_text, (width / 2 - score_text.get_width() / 2, 20))

    # Draw the game
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, color, paddle_a)
    pygame.draw.rect(screen, color, paddle_b)
    pygame.draw.ellipse(screen, color, ball)
    pygame.draw.aaline(screen, color, (width / 2, 0), (width / 2, height))
    pygame.display.flip()

    # Check if the game is over
    if score_a == 10:
        print("You win!")
        pygame.quit()
        exit()
    if score_b == 10:
        print("You lose!")

    # Draw the score
    score_text = font.render(f"{score_a} : {score_b}", True, color)
    screen.blit(score_text, (width / 2 - score_text.get_width() / 2, 20))

    # Draw the game
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, color, paddle_a)
    pygame.draw.rect(screen, color, paddle_b)
    pygame.draw.ellipse(screen, color, ball)
    pygame.draw.aaline(screen, color, (width / 2, 0), (width / 2, height))
    pygame.display.flip()

    # Check if the game is over
    if score_a == 10:
        print("You win!")
        pygame.quit()
        exit()
    if score_b == 10:
        print("You lose!")

    # Draw the score
    score_text = font.render(f"{score_a} : {score_b}", True, color)
    screen.blit(score_text, (width / 2 - score_text.get_width() / 2, 20))

    # Draw the game
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, color, paddle_a)
    pygame.draw.rect(screen, color, paddle_b)
    pygame.draw.ellipse(screen, color, ball)
    pygame.draw.aaline(screen, color, (width / 2, 0), (width / 2, height))
    pygame.display.flip()

    # Check if the game is over
    if score_a == 10:
        print("You win!")
        pygame.quit()
        exit()
    if score_b == 10:
        print("You lose!")
        pygame.quit()
        exit()
        pygame.quit()
        exit()
