import random
import os
import time



class Equipment:
    def __init__(self,name,type,description,cost):
        self.name = name
        self.type = type
        self.description = description
        self.cost = cost
        
item1 = Equipment("Sword of Strenght","out","git This sword gives you +1 to power",10)
item2 = Equipment("Cape of Swift Rat","out","This cape gives you +3 to dodge",10)
item3 = Equipment("Crystal Heart","pre", "Gain 3 HP before combat encounter",10)
item4 = Equipment("Havels Armor","out", "This armor gives you +1 to armor",15)
item5 = Equipment("BloodThirster","aft" "This sword gives you +1 to power per enemy fought",20)
bloodThirster = 0
item6 = Equipment("Midus's Crown","pre", "This crown gives you +1 to gold per enemy encounter",20)
item7 = Equipment("Health Pot","out in","A one time in combat use +10 health healing item ",10)

shopList = [
    item1,
    item2,
    item3,
    item4,
    item5,
    item6,
    item7
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
