import pygame, sys, random

# Create player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Assets/player.png')
        self.rect = self.image.get_rect(midbottom = (80, 300))
        self.gravity = 0

    def player_input(self):
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_a]:
            self.rect.x -= 5
        if self.keys[pygame.K_d]:
            self.rect.x += 5
        if self.keys[pygame.K_w] and self.rect.bottom >= 300:
            self.gravity = -20

    def create_main_projectile(self):
        return Player_Projectile(self.rect.x,self.rect.y)
    
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

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, img1, img2):
        super().__init__()
        res_tup = (50,50)
        self.crosshair_img1 = pygame.transform.scale(pygame.image.load(img1).convert_alpha(), res_tup)
        self.crosshair_img2 = pygame.transform.scale(pygame.image.load(img2).convert_alpha(), res_tup)
        self.crosshair_list = (self.crosshair_img1, self.crosshair_img2)

    
        self.crosshair_idx = 0
        self.image = self.crosshair_list[self.crosshair_idx]
        self.rect = self.image.get_rect(center = (pygame.mouse.get_pos()))

        
    def crosshair_movement(self):
        self.crosshair_idx += 0.05
        if self.crosshair_idx >= len(self.crosshair_list): self.crosshair_idx = 0
        self.image = self.crosshair_list[int(self.crosshair_idx)]
        
        self.rect = self.image.get_rect(center = (pygame.mouse.get_pos()))
    def update(self):
        self.crosshair_movement()
        
class Player_Projectile(pygame.sprite.Sprite):
        def __init__(self,pos_x,pos_y):
            super().__init__() 
            self.image = pygame.image.load('Assets/projectile.png')
            self.rect = self.image.get_rect(midbottom = (pos_x+65, pos_y+35))
        def update(self):
            self.rect.x += 5  
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