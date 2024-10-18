import pygame
pygame.init()

screen_width = 1920
screen_height = 1080

screen = pygame.display.set_mode((screen_width, screen_height))


sprite_right = [pygame.image.load("Assets/Char/Right/RightIdle1.png"),
                pygame.image.load("Assets/Char/Right/RightIdle2.png"),
                pygame.image.load("Assets/Char/Right/RightIdle3.png"),
                pygame.image.load("Assets/Char/Right/RightIdle4.png")]

sprite_left = [pygame.image.load("Assets/Char/Left/LeftIdle1.png"),
                pygame.image.load("Assets/Char/Left/LeftIdle2.png"),
                pygame.image.load("Assets/Char/Left/LeftIdle3.png"),
                pygame.image.load("Assets/Char/Left/LeftIdle4.png")]

sprite_up = [pygame.image.load("Assets/Char/Up/UpIdle1.png"),
                pygame.image.load("Assets/Char/Up/UpIdle2.png"),
                pygame.image.load("Assets/Char/Up/UpIdle3.png"),
                pygame.image.load("Assets/Char/Up/UpIdle4.png")]

sprite_down = [pygame.image.load("Assets/Char/Down/DownIdle1.png"),
                pygame.image.load("Assets/Char/Down/DownIdle2.png"),
                pygame.image.load("Assets/Char/Down/DownIdle3.png"),
                pygame.image.load("Assets/Char/Down/DownIdle4.png")]

current_direction = "down" 
current_sprites = sprite_down

background_image = pygame.image.load("Assets/BedRoom.png")

sprite_rect = sprite_right[0].get_rect()

sprite_rect.x = 885 
sprite_rect.y = 465

speed = 8

frame_rate = 10

background_x = 295
background_y = 95

current_frame = 0

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        current_direction = "up"
        current_sprites = sprite_up
        current_frame += 0.2
        background_y += speed
    if keys[pygame.K_s]:
        current_direction = "down"
        current_sprites = sprite_down
        current_frame += 0.2
        background_y -= speed
    if keys[pygame.K_a]:
        current_direction = "left"
        current_sprites = sprite_left
        current_frame += 0.2
        background_x += speed
    if keys[pygame.K_d]:
        current_direction = "right"
        current_sprites = sprite_right
        current_frame += 0.2
        background_x -= speed

    screen.fill((0, 0, 0))

    if current_frame >= len(current_sprites):
        current_frame = 0
    if current_frame == 4:
        current_frame = 0

    screen.blit(background_image, [background_x, background_y])
    screen.blit(current_sprites[int(current_frame)], sprite_rect)

    pygame.display.flip()

    clock.tick(30)