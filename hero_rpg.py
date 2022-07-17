import random
import os
from Data import *
# THE HOLY TWENTY
lives = 20
############################################    CLASSES     #####################################################

class Units:
    def __init__(self,name,health,power,armor,dodge,gold):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
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
        if item1 in self.inventory:
            itemF1(self)

        if item2 in self.inventory:
            itemF2(self)
        
        if item3 in self.inventory:
            itemF3(self)
            
        if item4 in self.inventory:
            itemF4(self)
            
        if item5 in self.inventory:
            itemF5(self)
            
        if item6 in self.inventory:
            itemF6(self)
            
class Player(Units):
    pass           
            
class Enemy(Units):
    pass         

class Goblin(Enemy):
    def attack(self,unit): 
        A = random.randint(1,100)
        if A < unit.dodge:
            print("The {} dodged!!".format(unit.name))
            return True
        else:
            damage = random.randint(int(self.power / 4), self.power)
            unit.health -= damage   #damage to target of attacks health based on power range
            print("The {} does {} damage.".format(self.name, damage))
            if unit.alive() == False:
                print(f"{unit.name} is dead.")
            return False     

class Zombie(Enemy):
    def alive(self):
        if self.health > 0:
            return True
        else:
            A = random.randint(1,100)
            if A <= 10:
                self.health = 1
                return True
            else:
                return False

class Skeleton(Enemy):
    def attack(self,unit): 
        A = random.randint(1,100)
        if A < unit.dodge:
            print("The {} dodged!!".format(unit.name))
            return True
        else:
            B = random.randint(1,100)
            damage = random.randint(int(self.power / 2), self.power)
            unit.health -= damage   #damage to target of attacks health based on power range
            print("The {} does {} damage.".format(self.name, damage))
            if B <= 10:
                unit.health -= 1
                print(f"The {self.name}s attack splintered doing 1 additional damage")
            if unit.alive() == False:
                print(f"{unit.name} is dead.")
            return False   

class Orc(Enemy):
    def attack(self,unit): 
        A = random.randint(1,100)
        if A < unit.dodge:
            print("The {} dodged!!".format(unit.name))
            return True
        else:
            B = random.randint(1,100)
            if B <= 25:
                charge = 2
                print(f"The {self.name} is charging")
            else:
                damage = random.randint(int(self.power / 2), self.power)
                unit.health -= damage*charge   #damage to target of attacks health based on power range
                print("The {} does {} damage.".format(self.name, damage*charge))
                charge = 1
            if unit.alive() == False:
                print(f"{unit.name} is dead.")
            return False   

class Rat(Enemy):
    def attack(self,unit): 
        A = random.randint(1,200)
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
   
class Vampire(Enemy):
    def attack(self,unit): 
        A = random.randint(1,100)
        if A < unit.dodge:
            print("The {} dodged!!".format(unit.name))
            return True
        else:
            damage = random.randint(int(self.power / 4), self.power)
            unit.health -= damage   #damage to target of attacks health based on power range
            self.health = self.health + 2
            print("The {} does {} damage and healed 2.".format(self.name, damage))
            if unit.alive() == False:
                print(f"{unit.name} is dead.")
            return False 
   
class Boss(Enemy):
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

def bossCombat():
    combat(Hero,dLord)

def randomEnemy(enemylist):     
    return random.choice(enemylist)

Hero = Player("Hero",10,5,0,10,0)
dLord = Boss("Necromancer",50,10,5,25,100)

enemylist = [Goblin("Goblin",6,4,0,20,5), 
                          Zombie("Zombie",20,1,1,5,5), 
                          Skeleton("Skeleton",2,10,0,10,5), 
                          Orc("Orc",12,4,3,5,10), 
                          Rat("Rat",1,1,0,75,5),
                          Vampire("Vampire",8,3,0,25,10)
                          ]

#########################################    PATHS     #############################################################

def shop():
    os.system('clear')
    shopInput = input(f"""
Store
Gold: {Hero.gold}
1.) Enter
2.) Leave 
    
    """)
    if shopInput == "1":
        buy1 = random.choice(shopList)
        buy2 = random.choice(shopList)
        buy3 = random.choice(shopList)
        while buy1 == buy2 or buy1 == buy3 or buy2 == buy3:
            buy1 = random.choice(shopList)
            buy2 = random.choice(shopList)
        
            
        buyInput = input(f"""
Items
1.) {buy1.name} - {buy1.description} - ${buy1.cost}
2.) {buy2.name} - {buy2.description} - ${buy2.cost}
3.) {buy3.name} - {buy3.description} - ${buy3.cost}
    
    """)
        if buyInput == "1" and Hero.gold >= buy1.cost:
            Hero.inventory.append(buy1)
            Hero.gold - buy1.cost
        elif buyInput == "2" and Hero.gold >= buy2.cost:
            Hero.inventory.append(buy2)
            Hero.gold - buy2.cost
        elif buyInput == "3" and Hero.gold >= buy3.cost:
            Hero.inventory.append(buy3)
            Hero.gold - buy3.cost
        
        
    elif shopInput == "2":
        pass
    print(Hero.inventory)

def buff():
    os.system('clear')
    buffInput = input("""
Fountain of Youth
1.) Perma - Buff
2.) Heal
3.) Leave 
    
    """)
    if buffInput == "1":
        Hero.power = Hero.power + 2
    elif buffInput == "2":
        Hero.health = Hero.health + 5
    elif buffInput == "3":
        pass

def risk():
    os.system('clear')
    buffInput = input("""
Fountain of Youth
1.) Power for Health
2.) Health for Power
3.) Leave 
    
    """)
    if buffInput == "1":
        Hero.power = Hero.power + 2
        Hero.health = Hero.health - 5
    elif buffInput == "2":
        Hero.health = Hero.health + 5
        Hero.power = Hero.power - 2
    elif buffInput == "3":
        pass
    
def unknown():
    A = random.choice(list(paths.values()))
    if A == combat:
        A(Hero,randomEnemy(enemylist))
    else:
        A()

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
    counter= 0
    while counter <= 5:
        path()
        counter += 1
        
    bossCombat()
 


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




#TODO

# class Skills:
#     pass

# def youLose():*
#     pass

# def youWin():*
#     pass

#Max HP*

#Lives*

#Player to Enemy*

#more enemies

#fix paths*

#flavor text

#info Text*