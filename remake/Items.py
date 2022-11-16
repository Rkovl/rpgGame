import random
import os
import time
from Units import *

# ############################################################################################ CLASS ##################################################################

class Equipment:
    def __init__(self,name,type,description,cost):
        self.name = name
        self.type = type
        self.description = description
        self.cost = cost
        
    
class IPO1(Equipment):
    def ability():
        Hero.xPower = Hero.xPower + 1
        
class IPO2(Equipment):
    def ability():
        Hero.xDodge = Hero.xDodge + 3
        
class IPP3(Equipment):
    def ability():
        if Hero.health + 3 > Hero.maxHealth:
            Hero.health = Hero.maxHealth
        else:
            Hero.health = Hero.health + 3
            
class IPO4(Equipment):
    def ability():
        Hero.xArmor = Hero.xArmor + 1
        
class IPA5(Equipment):
    def ability():
        Hero.xPower = Hero.xPower + 1
        
class IPP6(Equipment):
    def ability():
        Hero.gold = Hero.gold + 1
        
class ICCI7(Equipment):
    def ability():
        if Hero.health + 10 > Hero.maxHealth:
            Hero.health = Hero.maxHealth
        else:
            Hero.health = Hero.health + 10

        
item1 = IPO1("Sword of Strenght","out","git This sword gives you +1 to power",10)
item2 = IPO2("Cape of Swift Rat","out","This cape gives you +3 to dodge",10)
item3 = IPP3("Crystal Heart","pre", "Gain 3 HP before combat encounter",10)
item4 = IPO4("Havels Armor","out", "This armor gives you +1 to armor",15)
item5 = IPA5("BloodThirster","aft" "This sword gives you +1 to power per enemy defeated",20)
# bloodThirster = 0
item6 = IPP6("Midus's Crown","pre", "This crown gives you +1 to gold per enemy fought",20)
item7 = ICCI7("Health Pot","con in","A one time in combat use +10 health healing item ",10)

shopList = [
    item1,
    item2,
    item3,
    item4,
    item5,
    item6,
    item7
]


# def itemF1(unit):
#     unit.power = unit.power + 1
        
# def itemF2(unit):
#     unit.dodge = unit.dodge + 3
    
# def itemF3(unit):
#     try:
#         unit.maxHealth = unit.maxHealth + 3
#     except:
#         pass
#     unit.health = unit.health + 3
    
# def itemF4(unit):
#     unit.armor = unit.armor + 1
    
# def itemF5(unit):
#     global bloodThirster
#     bloodThirster += 1
#     unit.power = unit.power + bloodThirster
    
# def itemF6(unit):
#     unit.gold = unit.gold + 1
