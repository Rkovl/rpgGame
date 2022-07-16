import random
import os
from Data import *
# THE HOLY TWENTY

############################################    CLASSES     #####################################################

class Units:
    def __init__(self,name,health,power,dodge,gold):
        self.name = name
        self.health = health
        self.power = power
        self.dodge = dodge
        self.gold = gold
        self.inventory = []
        
    def attack(self,unit): 
        A = random.randint(1,100)
        if A < unit.dodge:
            print("The {} dodged!!".format(unit.name))
            return True
        else:
            damage = random.randint(int(self.power / 2), self.power)
            unit.health -= damage   #damage to target of attacks health based on power range
            print("The {} does {} damage.".format(self.name, damage))
            if unit.alive() == False:
                print(f"{unit.name} is dead.")
            return False
        
       
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
        
    def status(self):
        print("{} has {} health and {} power.".format(self.name,self.health, self.power))
        
    def equip(self):
        if swordItem in self.inventory:
            sword(self)

        if capeItem in self.inventory:
            cape(self)
            
class Player(Units):
    pass           
            
class Enemy(Units):
    pass         
            
###########################################     COMBAT      ######################################################      
                       
def startCombat(Player,Enemy):
    global pcBaseHealth, pcBasePower, pcBaseDodge
    pcBaseHealth = Player.health
    pcBasePower = Player.power
    pcBaseDodge = Player.dodge
    Player.equip()
    Enemy.equip()
    
def combat(Player,Enemy):
    startCombat(Player,Enemy)
    while Enemy.alive() and Player.alive():
        Player.status()
        Enemy.status()
        print()
        print("What do you want to do?")
        print(f"1. fight {Enemy.name}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            os.system('clear')
            Player.attack(Enemy)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if Enemy.alive():
            Enemy.attack(Player)
    if Player.alive():
        Player.gold = Player.gold + Enemy.gold
        Player.health = pcBaseHealth
        Player.power = pcBasePower
        Player.Dodge = pcBaseDodge

def randomEnemy(enemylist):     
    return random.choice(enemylist)

Hero = Player("Hero",10,5,10,0)

enemylist = [Enemy("Goblin",6,2,20,5), 
                          Enemy("Zombie",20,1,5,5), 
                          Enemy("Skeleton",2,10,10,5), 
                          Enemy("Orc",12,4,5,10), 
                          Enemy("Rat",1,1,75,5),
                          ]

#########################################    PATHS     #############################################################

def shop():
    Hero.inventory.append(sword)
    print("shop enter")
    print(Hero.inventory)
    combat(Hero,randomEnemy(enemylist))
    # path()
def buff():
    pass
def risk():
    pass
def unknown():
    pass

#######################################     MAIN      ##############################################################

def main():
    os.system('clear')
    menuInput = input("""
Welcome 
1.) Start
2.) Load
3.) Exit 
    
    """)
    if menuInput == "1":
        start()
    elif menuInput == "2":
        pass
    elif menuInput == "3":
        quit()
    else:
        main()
           
def start():
    os.system('clear')
    path()
 


paths = {"combat":combat,
         "shop":shop,
         "buff":buff,
         "risk":risk,
         "unknown":unknown
}

 
def path():
    path1Name, path1Fun = random.choice(list(paths.items()))
    path2Name, path2Fun = random.choice(list(paths.items()))
    path3Name, path3Fun = random.choice(list(paths.items()))
    pathInput = input(f"""
Welcome 
1.) {path1Name}
2.) {path2Name}
3.) {path3Name} 
    
    """)
    if pathInput == "1":
        if path1Fun == combat:
            path1Fun(Hero,randomEnemy(enemylist))
        else:
            path1Fun()
    elif pathInput == "2":
        if path2Fun == combat:
            path2Fun(Hero,randomEnemy(enemylist))
        else:
            path2Fun()
    elif pathInput == "3":
        if path3Fun == combat:
            path3Fun(Hero,randomEnemy(enemylist))
        else:
            path3Fun()
    else:
        path()
        
        
main()


# Fight = Battle.combat(Hero,Goblin)

# print(Enemy.enemyList)


# class Skills:
#     pass


# def youLose():
#     pass

# def youWin():
#     pass
# equipment = []
# def checkequip
# sword = power + 1
# equpment if have sword + sword power
# kill = sword power + 1



# enemyList = {
#     "Goblin" : Enemy("Goblin",6,2),
#     "Zombie" : Enemy("Zombie",20,1),
#     "Skeleton" : Enemy("Skeleton",2,10),
#     "Orc" : Enemy("Orc",12,4),
#     "Rat" : Enemy("Rat",1,1),
# }