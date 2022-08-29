import pygame, sys, time, random

def parry():
    if parry_avaiable:
        enemy_rect.x -= 1
    
    
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Necromancers: The Game")
clock = pygame.time.Clock()

# Creating the background and ground
Background = pygame.Surface(screen.get_size())
Background.fill((0, 0, 255))
ground = pygame.Surface((640, 100))
ground.fill((255, 0, 255))

# Creating player 
player = pygame.Surface((50, 50))
player.fill((255, 0, 0))
player_rect = player.get_rect(midbottom = (100, 400))
player_gravity = 0
player_velocity = 5
parry_avaiable = False

# Creating enemy
enemy = pygame.Surface((50, 50))
enemy.fill((0, 255, 0))
enemy_rect = enemy.get_rect(midbottom = (400, 400))
enemy_parry_duration = 2000

#Create event
parry_timer = pygame.USEREVENT
pygame.time.set_timer(parry_timer, 1000)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #makes the game close when the x button is pressed
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE and player_rect.bottom >= 400: # Adds jumping via gravity
                player_gravity = -20
            if event.key == pygame.K_LSHIFT: # Adds Sprint
                player_velocity = 10
            if event.key == pygame.K_ESCAPE: #Closes the game
                pygame.quit()
                sys.exit()
                
        if event.type == pygame.KEYUP: #allows the player to stop sprinting
            if event.key == pygame.K_LSHIFT:
                player_velocity = 5
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            parry_avaiable = True
        if event.type == parry_timer:
            parry_avaiable = False
    parry()                   
    # Controls the player's movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.move_ip(-player_velocity, 0)
    if keys[pygame.K_RIGHT]:
        player_rect.move_ip(player_velocity, 0)
   
    # Jumping and gravity
    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 400: player_rect.bottom = 400
    
    # Drawing all the objects
    screen.blit(Background, (0, 0))
    screen.blit(ground, (0, 400))
    screen.blit(player, player_rect)
    screen.blit(enemy, enemy_rect)
    
    pygame.display.update()
    clock.tick(60)