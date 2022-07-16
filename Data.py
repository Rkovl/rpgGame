# from hero_rpg import *

# enemylist = [Goblin]

# enemylist = [Enemy("Goblin",6,2), 
#                           Enemy("Zombie",20,1), 
#                           Enemy("Skeleton",2,10), 
#                           Enemy("Orc",12,4), 
#                           Enemy("Rat",1,1),
#                           ]

class Equipment:
    def __init__(self,name,description,cost):
        self.name = name
        self.description = description
        self.cost = cost
        
swordItem = Equipment("Sword of Strenght","This sword gives you +3 to power",15)
capeItem = Equipment("Cape of Swift Rat","This cape gives you +5 to dodge",15)
potionItem = Equipment("Healing Potion", "Instantly Gain 10 HP",10)

def sword(unit):
    unit.power = unit.power + 1
        
def cape(unit):
    unit.dodge = unit.dodge + 5
    
    
shopList = [
    swordItem,
    capeItem,
]