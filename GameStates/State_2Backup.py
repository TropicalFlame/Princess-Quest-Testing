import pygame
pygame.init()

screen_width = 1920
screen_height = 1080

screen = pygame.display.set_mode((screen_width, screen_height))


sprite_right = [pygame.image.load("RightIdle1.png"),
                pygame.image.load("RightIdle2.png"),
                pygame.image.load("RightIdle3.png"),
                pygame.image.load("RightIdle4.png")]

sprite_left = [pygame.image.load("LeftIdle1.png"),
                pygame.image.load("LeftIdle2.png"),
                pygame.image.load("LeftIdle3.png"),
                pygame.image.load("LeftIdle4.png")]

sprite_up = [pygame.image.load("UpIdle1.png"),
                pygame.image.load("UpIdle2.png"),
                pygame.image.load("UpIdle3.png"),
                pygame.image.load("UpIdle4.png")]

sprite_down = [pygame.image.load("DownIdle1.png"),
                pygame.image.load("DownIdle2.png"),
                pygame.image.load("DownIdle3.png"),
                pygame.image.load("DownIdle4.png")]


current_direction = "down" 
current_sprites = sprite_down



background_image = pygame.image.load("BedRoom.png") #check
background_rec = background_image.get_rect(center = [screen_width//2, screen_height//2])



sprite_rect = sprite_right[0].get_rect()

sprite_rect.x = 885 #check
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