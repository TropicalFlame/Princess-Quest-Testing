import pygame
from subprocess import call

pygame.init()

screen_width = 1920
screen_height = 1080

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Princess Quest")

image_path = "Assets/Title.png"
try:
    image = pygame.image.load(image_path)
except pygame.error as e:
    print(f"Unable to load image: {image_path}. Error: {e}")
    pygame.quit()
    exit()

def Background(image):
    size = pygame.transform.scale(image, (1600, 900))
    screen.blit(size, (120, 67.5))

clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        call(["python", "GameStates/State_2.py"])

    screen.fill((0, 0, 0)) 

    Background(image)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
