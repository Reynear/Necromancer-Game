import pygame, sys, random # Import pygame module
from classes import Player, Enemy # Import player module from player.py

#Create a function to parry enemies


pygame.init() # Initialize the pygame module
screen = pygame.display.set_mode((640, 480)) #set screen size
pygame.display.set_caption("Platformer") #set name on the game menu
clock = pygame.time.Clock() #set clock
game_active = True #set game active

# Create Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

Enemies = pygame.sprite.Group()
Enemies.add(Enemy())

#Create images
background = pygame.Surface(screen.get_size()) #create background surface
background.fill((255,255,255)) #fill surface with black

ground = pygame.Surface((640,300)) #create ground surface
ground.fill((255,0,255)) #fill surface with purple

#Intro Screen ADD LATER

#Animation Timers ADD LATER
'''
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer,1500)
'''
#main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit() # If user clicked X on window # Close the game window
        
    #if game_active:
    # Render background elements
    screen.blit(background,(0,0))
    screen.blit(ground,(0,300))

    # Display player and player logic
    player.draw(screen)
    player.update()
       
    Enemies.draw(screen)
    Enemies.update()
	# Collision Detection ADD LATER
 
    #INTRO SCREEN ADD LATER
    
    pygame.display.update()
    clock.tick(60)
    
