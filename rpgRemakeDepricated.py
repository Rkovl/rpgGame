import pygame
import random
import os
import time

pygame.init()

clock = pygame.time.Clock()
fps = 60

#game window
bottom_panel = 0
screen_width = 1360
screen_height = 768 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Battle')


#load images ---------------------------------------------------------- BACKROUND-----------------------------------------------------
#background image
background_img = pygame.image.load('img/background/background.png').convert_alpha()
#panel image
# panel_img = pygame.image.load('img/Icons/panel.png').convert_alpha()

#function for drawing background
def draw_bg(img):
	screen.blit(img, (0, 0))


#function for drawing panel
# def draw_panel():
# 	screen.blit(panel_img, (0, screen_height - bottom_panel))


#define fonts------------------------------------------------------------ FONTS------------------------------------------------
healthFont = pygame.font.SysFont('Times New Roman', 26)
titleFont = pygame.font.SysFont('Times New Roman', 100)
buttonFont = pygame.font.SysFont('Times New Roman', 42)

#define colours
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

#create function for drawing text
def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))


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
        text = healthFont.render(f'{self.name} HP: {self.hp}/{self.maxhp}', True, 100)
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
        
  
#-----------------------------------------------------------------Main Menu--------------------------------------------       


def mainMenu():
    pygame.draw.rect(screen, black, (0, 0, screen_width, screen_height))
    draw_text("The Holy Ten", titleFont,white,screen_width/3,100)
    
    pygame.draw.rect(screen, white, (screen_width/3, screen_height/2, screen_width/5, screen_height/8))
    pygame.draw.rect(screen, white, (screen_width/3, screen_height/1.5, screen_width/5, screen_height/8))
    draw_text("Start", buttonFont,black,screen_width/3,screen_height/2)
    draw_text("Quit", buttonFont,black,screen_width/3,screen_height/1.5)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    pygame.display.update()
        
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

#---------------------------------------------------------------Game Screen -----------------------------------------------

while run :
    
    clock.tick(fps)
    
    draw_bg(background_img)
    
    mainMenu()
    # draw_panel()
    
    # hero.draw(350,400)
    
    # goblin.draw(1100,400)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()
    
pygame.quit()