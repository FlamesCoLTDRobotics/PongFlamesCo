## write the gui 800x800
import pygame
## write 800 x800 pygame
pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Pong [V1.0A] By Susana P Haltmann")
## write the game boy screen

## write the score on the top
font = pygame.font.Font(None, 74)
score = 0

## make it for the ai and the player
score2 = 0

## write the ball
ball = pygame.Rect(400,400,20,20)

## write the player
player = pygame.Rect(10,400,20,100)

## write the ai
ai = pygame.Rect(770,400,20,100)

## write the line
line = pygame.Rect(400,0,20,800)

## write the ball movement
ball_speed_x = 10
ball_speed_y = 10
## write the player movement
player_speed = 0
## write the ai movement
ai_speed = 0
## write the game loop
running = True
while running:
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,255,255), ball)
    pygame.draw.rect(screen, (255,255,255), player)
    pygame.draw.rect(screen, (255,255,255), ai)
    pygame.draw.rect(screen, (255,255,255), line)
    score_text = font.render(str(score), 1, (255,255,255))
    screen.blit(score_text, (10,10))
    score_text2 = font.render(str(score2), 1, (255,255,255))
    screen.blit(score_text2, (700,10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_speed -= 5
            if event.key == pygame.K_s:
                player_speed += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_speed += 5
            if event.key == pygame.K_s:
                player_speed -= 5
    ## write the ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    ## write the player movement
    player.y += player_speed
    ## write the ai movement
    ai.y += ai_speed
    ## write the ball bounce
    if ball.top <= 0 or ball.bottom >= 800:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= 800:
        ball_speed_x *= -1
    ## write the player bounce
    if player.top <= 0:
        player.top = 0
    if player.bottom >= 800:
        player.bottom = 800
    ## write the ai bounce
    if ai.top <= 0:
        ai.top = 0
    if ai.bottom >= 800:
        ai.bottom = 800
    ## write the ball bounce off the player
    if ball.colliderect(player):
        ball_speed_x *= -1
    ## write the ball bounce off the ai
    if ball.colliderect(ai):
        ball_speed_x *= -1
    ## write the score
    if ball.left <= 0:
        score += 1
        score_text = font.render(str(score), 1, (255,255,255))
    if ball.right >= 800:
        score2 += 1
        score_text2 = font.render(str(score2), 1, (255,255,255))
    pygame.display.flip()