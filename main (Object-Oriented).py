import pygame, sys, random # Import pygame module
from classes import Crosshair, Player, Enemy, Player_Projectile # Import player module from player.py

pygame.init() # Initialize the pygame module
screen = pygame.display.set_mode((640, 480)) #set screen size
pygame.display.set_caption("Platformer") #set name on the game menu
clock = pygame.time.Clock() #set clock
game_active = True #set game active

# Create Groups
player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

Enemies = pygame.sprite.Group()
Enemies.add(Enemy())

crosshair = Crosshair('Assets/Crosshairs/init.png','Assets/Crosshairs/move.png')
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

player_projectile_group = pygame.sprite.Group()

#Create images
background = pygame.Surface(screen.get_size()) #create background surface
background.fill((255,255,255)) #fill surface with black

ground = pygame.Surface((640,300)) #create ground surface
ground.fill((255,0,255)) #fill surface with purple

#Intro Screen ADD LATER
#Animation Timers ADD LATER

#main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit() # If user clicked X on window # Close the game window
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            player_projectile_group.add(player.create_main_projectile())                

    # Render background elements
    screen.blit(background,(0,0))
    screen.blit(ground,(0,300))

    # Display player and player logic
    player_group.draw(screen)
    player_group.update()
      
    Enemies.draw(screen)
    Enemies.update()
    
    crosshair_group.draw(screen)
    crosshair_group.update()
    
    player_projectile_group.draw(screen)
    player_projectile_group.update()

	# Collision Detection ADD LATER 
    #INTRO SCREEN ADD LATER
    
    pygame.display.update()
    clock.tick(60)
    
