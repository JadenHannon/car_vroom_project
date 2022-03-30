# imports
import pygame, os, sys

# center pygame window on display
# technique found at https://stackoverflow.com/questions/5814125/how-to-designate-where-pygame-creates-the-game-window
os.environ['SDL_VIDEO_CENTERED'] = '2'

# initialize pygame
pygame.init()

# constants
WIDTH = 1440
HEIGHT = 900
FPS = 30

# RGB colors
white = (255, 255, 255)
black = (0, 0, 0)

# variables
image_count = 0 # counter for images
clock = pygame.time.Clock() # clock object
running = True
timer = 0

# load images into pygame
car_images = [
  pygame.image.load('./assets/jackson_1.png'),
  pygame.image.load('./assets/jackson_2.png')
]

# changes size of all images to fit screen
for i in range(len(car_images)):
  car_images[i] = pygame.transform.scale(car_images[i], (350, 350))

# set Window
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car!")
WINDOW.fill(white)

# set up your font
font = pygame.font.Font('./fonts/NotoSansJP-Regular.otf', 40)

# create your text
text = font.render('速い！', True, black, white)
text1 = font.render('Art: Sorin Jackson', True, black, white)
text2 = font.render('Animation:Luke Erdman & Jaden Hannon', True, black, white)
textRect = text.get_rect()
textRect1 = text1.get_rect()
textRect2 = text2.get_rect()

# position the text
textRect.center = (WIDTH // 2, HEIGHT // 10)
textRect1.center = (WIDTH // 2, HEIGHT // 6)
textRect2.center = (WIDTH // 2, HEIGHT // 4)

# display text
WINDOW.blit(text, textRect)
WINDOW.blit(text1, textRect1)
WINDOW.blit(text2, textRect2)
pygame.display.flip()

# draw shape function
def drawShape():
  global car_images
  global image_count
  if (image_count == 2):
    image_count = 0
  WINDOW.blit(car_images[image_count], (450, 350))
  pygame.display.flip()
  image_count += 1
  
# main animation Loop that will run for 10 seconds
while running and timer < 300:

  # upadate screen according to FPS value
  clock.tick(FPS)

  # update timer
  timer += 1

  # check if "X" is clicked by user 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()
      sys.exit()

  # call to drawShape function
  drawShape()
