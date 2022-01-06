import pygame
from food import *
from snake import *

# Constants
SCALE = 20
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Pygame Window settup
pygame.init()
dis = pygame.display.set_mode((800, 600))
pygame.display.update()
pygame.display.set_caption('Snake game')
clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(), 36)

# Variables
gameOver = False
snake = Snake()
food = Food(snake.tail + [{"x": snake.getX(), "y":snake.getY()}])

# Main game Loop
while not gameOver:
  for event in pygame.event.get():
    
    # Allows the user to exit the game with the quit button
    if event.type == pygame.QUIT:
      gameOver = True

    # handles keypresses
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
      snake.setDir("UP")
    elif pressed[pygame.K_s]:
      snake.setDir("DOWN")
    elif pressed[pygame.K_a]:
      snake.setDir("LEFT")
    elif pressed[pygame.K_d]:
      snake.setDir("RIGHT")

  # Refreshs the location of the snake's head and tail
  snake.refreshSnake()
  dis.fill(BLACK)

  # draws the food
  pygame.draw.rect(dis, RED, [food.getX()*SCALE, food.getY()*SCALE, 20, 20])

  # draws the snake's head, the reason i draw two squares to give it the blocks effect
  pygame.draw.rect(dis, BLACK, [snake.getX()*SCALE, snake.getY()*SCALE, 20, 20])
  pygame.draw.rect(dis, WHITE, [snake.getX()*SCALE, snake.getY()*SCALE, 19, 19])

  # draws the snake's tail
  for cords in snake.tail:
    pygame.draw.rect(dis, BLACK, [cords["x"]*SCALE, cords["y"]*SCALE, 20, 20])
    pygame.draw.rect(dis, WHITE, [cords["x"]*SCALE, cords["y"]*SCALE, 19, 19])
   
  # If the snake touches the borders or part of it's tail, then it should reset
  if snake.getX() >= 40 or snake.getX() < 0 or snake.getY() >= 30 or snake.getY() < 0 or {"x": snake.getX(), "y": snake.getY()} in snake.tail:
    snake.resetSnake()

  # If Snake eats the food
  if snake.getX() == food.getX() and snake.getY() == food.getY():
    snake.incrementScore()
    food = Food(snake.tail + [{"x": snake.getX(), "y":snake.getY()}])

  # Displaying the score
  text_surface = font.render("Score: " + str(snake.getScore()), True, WHITE)
  dis.blit(text_surface, [0, 0])
  pygame.display.update()
  clock.tick(10)

pygame.quit()