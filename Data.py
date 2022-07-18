# from hero_rpg import *

# enemylist = [Goblin]

# enemylist = [Enemy("Goblin",6,2), 
#                           Enemy("Zombie",20,1), 
#                           Enemy("Skeleton",2,10), 
#                           Enemy("Orc",12,4), 
#                           Enemy("Rat",1,1),
#                           ]
charge = 1



class Equipment:
    def __init__(self,name,description,cost):
        self.name = name
        self.description = description
        self.cost = cost
        
item1 = Equipment("Sword of Strenght","This sword gives you +1 to power",10)
item2 = Equipment("Cape of Swift Rat","This cape gives you +3 to dodge",10)
item3 = Equipment("Crystal Heart", "Gain 3 HP before combat encounter",10)
item4 = Equipment("Havels Armor", "This armor gives you +1 to armor",15)
item5 = Equipment("BloodThirster", "This sword gives you +1 to power per enemy fought",20)
bloodThirster = 0
item6 = Equipment("Midus's Crown", "This crown gives you +1 to gold per enemy encounter",20)

shopList = [
    item1,
    item2,
    item3,
    item4,
    item5,
    item6
]


def itemF1(unit):
    unit.power = unit.power + 1
        
def itemF2(unit):
    unit.dodge = unit.dodge + 3
    
def itemF3(unit):
    try:
        unit.maxHealth = unit.maxHealth + 3
    except:
        pass
    unit.health = unit.health + 3
    
def itemF4(unit):
    unit.armor = unit.armor + 1
    
def itemF5(unit):
    global bloodThirster
    bloodThirster += 1
    unit.power = unit.power + bloodThirster
    
def itemF6(unit):
    unit.gold = unit.gold + 1
