import pygame, random

pygame.init()
dis = pygame.display.set_mode((800, 600))
pygame.display.update()
pygame.display.set_caption('Snake game')
clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(), 36)

gameOver = False
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)


scale = 20
snakeX = 19
snakeY = 14
xChange = 0
yChange = 0
score = 0
tail = []
foodX = random.randint(0, 39)
foodY = random.randint(0, 29)


while not gameOver:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      gameOver = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w] and yChange == 0:
      xChange = 0
      yChange = -1
    elif pressed[pygame.K_s] and yChange == 0:
      xChange = 0
      yChange = 1
    elif pressed[pygame.K_a] and xChange == 0:
      xChange = -1
      yChange = 0
    elif pressed[pygame.K_d] and xChange == 0:
      xChange = 1
      yChange = 0


  tail.append([snakeX, snakeY]) 
  if len(tail) > score:
    tail.pop(0)

  snakeX += xChange
  snakeY += yChange
   
  dis.fill(black)
  pygame.draw.rect(dis, red, [foodX*scale, foodY*scale, 20, 20])
  pygame.draw.rect(dis, black, [snakeX*scale, snakeY*scale, 20, 20])
  pygame.draw.rect(dis, white, [snakeX*scale, snakeY*scale, 19, 19])

  for cords in tail:
   pygame.draw.rect(dis, black, [cords[0]*scale, cords[1]*scale, 20, 20])
   pygame.draw.rect(dis, white, [cords[0]*scale, cords[1]*scale, 19, 19])
   if snakeX == cords[0] and snakeY == cords[1]:
    xChange = 0
    snakeX = 19
    snakeY = 14
    tail = []
    score = 0


  if snakeX >= 40 or snakeX < 0:
    xChange = 0
    snakeX = 19
    snakeY = 14
    tail = []
    score = 0

  if snakeY >= 30 or snakeY < 0:
    yChange = 0
    snakeX = 19
    snakeY = 14
    tail = []
    score = 0

  if snakeX == foodX and snakeY == foodY:
    score += 1 
    foodX = random.randint(0, 39)
    foodY = random.randint(0, 29)

  text_surface = font.render("Score: " + str(score), True, white)
  dis.blit(text_surface, [0, 0])
  pygame.display.update()
  clock.tick(10)

pygame.quit()