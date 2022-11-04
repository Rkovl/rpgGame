import pygame
import random
import os
import time

pygame.init()

clock = pygame.time.Clock()
fps = 60

#game window
bottom_panel = 0
screen_width = 1450
screen_height = 900 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Battle')


#load images
#background image
background_img = pygame.image.load('img/background/background.png').convert_alpha()
#panel image
# panel_img = pygame.image.load('img/Icons/panel.png').convert_alpha()


#define fonts
font = pygame.font.SysFont('Times New Roman', 26)

#define colours
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

#create function for drawing text
def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))


#function for drawing background
def draw_bg():
	screen.blit(background_img, (0, 0))


#function for drawing panel
# def draw_panel():
# 	screen.blit(panel_img, (0, screen_height - bottom_panel))


#-----------------------------------------------------------------CLASSES-------------------------------------------
class Units:
    def __init__(self,name,maxhp,power,armor,dodge,gold):
        self.name = name
        self.maxhp = maxhp
        self.hp = maxhp
        self.power = power
        self.armor = armor
        self.dodge = dodge
        self.gold = gold
        self.inventory = []
        img = pygame.image.load(f'img/units/{self.name}.jpg')
        self.image = pygame.transform.scale(img, (img.get_width() * 0.25, img.get_height() * 0.25))
        self.rect = self.image.get_rect()
        
     
    def draw(self, x, y):
        #character pic
        self.rect.center = (x, y)
        screen.blit(self.image, self.rect)
        #charcter hp display
        ratio = self.hp / self.maxhp
        pygame.draw.rect(screen, red, (x - 120, y - 225, 210, 30))
        pygame.draw.rect(screen, green, (x - 120, y - 225, 210 * ratio, 30))
        text = font.render(f'{self.name} HP: {self.hp}/{self.maxhp}', True, 100)
        screen.blit(text, (x - 120, y - 225))
        
        
        
    def attack(self,unit): 
        A = random.randint(1,100)
        if A < unit.dodge:
            print("The {} dodged!!".format(unit.name))
            return True
        else:
            damage = random.randint(int(self.power / 2), self.power)
            if damage > unit.armor:
                unit.hp -= (damage - unit.armor)  #damage to target of attacks hp based on power range
                print("The {} does {} damage.".format(self.name, damage - unit.armor))
            else:
                 unit.hp -= 1
                 print("The {} does 1 damage due to armor.".format(self.name))
            if unit.alive() == False:
                print(f"{unit.name} is dead.")
            return False
              
    def alive(self):
        if self.hp > 0:
            return True
        else:
            return False
        
    def status(self):
        print(f"""
{self.name}   -   {self.hp} health
{self.power} power  -   {self.armor} armor  -   {self.dodge} dodge
""")
        
        
#-----------------------------------------------------Units---------------------------------------------------     
hero = Units("Hero",10,5,0,10,0) 
goblin = Units("Goblin",10,5,0,10,0)      


#----------------------------------------------GUI-------------------------------------------------------
run = True
# while run:

# 	clock.tick(fps)

# 	#draw background
# 	draw_bg()

# 	#draw panel
# 	draw_panel()

#   hero.draw()
    

# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			run = False

# 	pygame.display.update()

# pygame.quit()

while run :
    
    clock.tick(fps)
    
    draw_bg()
    
    # draw_panel()
    
    hero.draw(350,400)
    
    goblin.draw(1100,400)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()
    
pygame.quit()