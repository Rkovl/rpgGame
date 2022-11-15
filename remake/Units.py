import random
import os
import time
from Items import *

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
            if damage > unit.armor:
                unit.health -= (damage - unit.armor)  #damage to target of attacks health based on power range
                print("The {} does {} damage.".format(self.name, damage - unit.armor))
            else:
                 unit.health -= 1
                 print("The {} does 1 damage due to armor.".format(self.name))
            if unit.alive() == False:
                print(f"{unit.name} is dead.")
            return False
              
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
        
    def status(self):
        print(f"""
{self.name}   -   {self.health} health
{self.power} power  -   {self.armor} armor  -   {self.dodge} dodge
""")
        
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
    def __init__(self,name,health,power,armor,dodge,gold,maxHealth):          
        super(Player,self).__init__(name,health,power,armor,dodge,gold)
        self.maxHealth = maxHealth

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
            if damage > unit.armor:
                unit.health -= (damage - unit.armor)  #damage to target of attacks health based on power range
                print("The {} does {} damage.".format(self.name, damage - unit.armor))
            else:
                 unit.health -= 1
                 print("The {} does 1 damage due to armor.".format(self.name))
            if unit.alive() == False:
                print(f"{unit.name} is dead.")
            return False     

class Zombie(Enemy):
    def alive(self):
        if self.health > 0:
            return True
        else:
            A = random.randint(1,100)
            if A <= 25:
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
            if damage > unit.armor:
                unit.health -= (damage - unit.armor)  #damage to target of attacks health based on power range
                print("The {} does {} damage.".format(self.name, damage - unit.armor))
            else:
                 unit.health -= 1
                 print("The {} does 1 damage due to armor.".format(self.name))
            if B <= 10:
                unit.health -= 1
                print(f"The {self.name}s attack splintered doing 1 additional damage")
            if unit.alive() == False:
                print(f"{unit.name} is dead.")
            return False   

class Orc(Enemy):
    def attack(self,unit): 
        global charge
        A = random.randint(1,100)
        if A < unit.dodge:
            print("The {} dodged!!".format(unit.name))
            return True
        else:
            B = random.randint(1,100)
            if B <= 25 and charge == 1:
                charge = charge + 1
                print(f"The {self.name} is charging")
            else:
                damage = random.randint(int(self.power / 2), self.power)
                if (damage*charge) > unit.armor:
                    unit.health -= ((damage*charge) - unit.armor)  #damage to target of attacks health based on power range
                    print("The {} does {} damage.".format(self.name, damage - unit.armor))
                    charge = 1
                else:
                    unit.health -= (1)
                    print("The {} does 1 damage due to armor.".format(self.name))
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
            damage = random.randint(int(self.power), self.power)
            if damage > unit.armor:
                unit.health -= (damage - unit.armor)  #damage to target of attacks health based on power range
                print("The {} does {} damage.".format(self.name, damage - unit.armor))
            else:
                 unit.health -= 1
                 print("The {} does 1 damage due to armor.".format(self.name))
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
            if damage > unit.armor:
                unit.health -= (damage - unit.armor)  #damage to target of attacks health based on power range
                print("The {} does {} damage.".format(self.name, damage - unit.armor))
                self.health = self.health + 2
            else:
                 unit.health -= 1
                 print("The {} does 1 damage due to armor.".format(self.name))
                 self.health = self.health + 2
            if unit.alive() == False:
                print(f"{unit.name} is dead.")
            return False 
   
class Boss(Enemy):
    pass


Hero = Player("Hero",10,5,0,10,0,10)
dLord = Boss("Necromancer",50,10,5,25,100)

enemylist = [Goblin("Goblin",6,4,0,20,5), 
                          Zombie("Zombie",6,1,1,5,5), 
                          Skeleton("Skeleton",4,10,0,10,5), 
                          Orc("Orc",12,4,3,5,10), 
                          Rat("Rat",1,1,0,80,5),
                          Vampire("Vampire",7,3,0,25,10)
                          ]