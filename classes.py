from urllib.parse import ParseResultBytes
import pygame, sys, random

# Create player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_surf = pygame.Surface((50, 50))
        self.image = self.player_surf
        self.rect = self.image.get_rect(midbottom = (80, 300))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= 5
        if keys[pygame.K_d]:
            self.rect.x += 5
        if keys[pygame.K_w] and self.rect.bottom >= 300:
            self.gravity = -20

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300: self.rect.bottom = 300

    def update(self):
        self.player_input()
        self.apply_gravity()
    	#self.animation_state()

#Create enemy classes
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        surface = pygame.Surface((50, 50))
        y_pos = 300
        self.image = surface
        self.rect = self.image.get_rect(midbottom = (400, y_pos))
    
    def parry(self):
        global parry 
        parry = False
        if parry:
            self.rect.x += 1
    def update(self):
        self.parry()

'''
class Obstacles(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        
        if type == "platform":
            self.image = pygame.Surface((100, 10))
            self.image.fill((255,0,0))
            self.rect = self.image.get_rect(midbottom = (random.randint(0,640), random.randint(0,300)))

        elif type == "coin":
            self.surf = pygame.Surface((50, 50))
            self.image = self.surf
            self.rect = self.image.get_rect(midbottom = (300, 300))
            
        else type == "heart":
            self.surf = pygame.Surface((50, 50))
            self.image = self.surf
            self.rect = self.image.get_rect(midbottom = (300, 300))
'''