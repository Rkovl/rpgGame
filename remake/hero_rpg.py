import random
import os
import time
from Units import *
# from Items import *
# THE HOLY TEN
lives = 10
charge = 1
############################################    CLASSES     #####################################################

  
###########################################     COMBAT      ######################################################      
                       
def startCombat(Player,Enemy):
    global pcBasePower, pcBaseDodge, pcBaseArmor
    pcBasePower = Player.power
    pcBaseDodge = Player.dodge
    pcBaseArmor = Player.armor
    Player.equip()
    Enemy.equip()
    
def combat(Player,Enemy):
    startCombat(Player,Enemy)
    while Enemy.alive() and Player.alive():
        Player.status()
        Enemy.status()
        print()
        print("What do you want to do?")
        print(f"1. Fight {Enemy.name}")
        print("2. Use Healing Pot")
        print("3. do nothing")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            os.system('clear')
            Player.attack(Enemy)
        elif raw_input == "2":
            useItem(Player)                
        elif raw_input == "3":
            pass
        else:
            print("Invalid input {}".format(raw_input))

        if Enemy.alive():
            Enemy.attack(Player)
    
    if Player.alive():
        Player.gold = Player.gold + Enemy.gold
        Player.power = pcBasePower
        Player.dodge = pcBaseDodge
        Player.armor = pcBaseArmor
        Player.inventory.append(Enemy.inventory)
        print("You pick up and item or gold the enemy had")
        time.sleep(1.5)
    else:
        youDied(lives)

def bossCombat():
    combat(Hero,dLord)
    if Hero.alive:
        youWin()
    else:
        print("ERROR")

def randomEnemy(enemylist):     
    return random.choice(enemylist)

def useItem(Player):
    if item7 in Player.inventory:
        C = 0
        for A in Player.inventory:
            if A == item7:
                if (Player.health + 10) > Player.maxHealth:
                    B = Player.maxHealth - Player.health
                    Player.health = Player.health + B
                    print("You Healed")
                    del Player.inventory[C]
                    break;
                else:
                    Player.health = Player.health + 10
                    print("You Healed")
                    del Player.inventory[C]
                    break;
            C += 1
    else:
        print("You have no healing pots in inventory")



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
    Hero.status()
    buffInput = input(f"""

                      
              _,-'  \   
             /\     _\ 
            /__\_,-'   
   .(       
   /%/)
  (%(%))
 .-'..`-.
 `-'.'`-'   
 
A safe place to stay
1.) Train (random buff)
2.) Rest (Heal to {Hero.maxHealth})
3.) Leave 
    
    """)
    if buffInput == "1":
        A = random.randint(1,5)
        if A == 1:
            Hero.power = Hero.power + 2
            print("You Feel Stonger +2 Power")
        if A == 2:
            Hero.dodge = Hero.dodge + 6
            print("You Feel Faster +6 Dodge")
        if A == 3:
            Hero.armor = Hero.armor + 1
            print("You Feel You Can Take Anything +1 Armor")
        if A == 4:
            Hero.health = Hero.health + 5
            Hero.maxHealth = Hero.maxHealth + 5
            print("You Feel Healthy +5 HP and Max HP")
        if A == 5:
            Hero.gold = Hero.gold + 10
            print("You Feel Lucky +10 Gold Found")
        time.sleep(1.5)
    elif buffInput == "2":
        if Hero.health < Hero.maxHealth:
            Hero.health = Hero.maxHealth
    elif buffInput == "3":
        pass

def risk():
    os.system('clear')
    Hero.status()
    buffInput = input(f"""

                      . .        .
    .                ` ' `               *
                 .'''. ' .'''.                   *
  .                .. ' ' ..      .
             *    '  '.'.'  '              .
                  .'''.'.'''.
                 ' .''.'.''. '
                   . . : . .
                 _'___':'___'_ 
                (_____________)
                    (     )
                    _)   (_   
                   (_______)
You something ominous but powerful from this fountain
1.) Drink?
2.) Leave 
    
    """)
    
    if buffInput == "1":
        A = random.randint(1,4)
        if A == 1:
            Hero.power = Hero.power + 4
            print("+4 Power")
        if A == 2:
            Hero.dodge = Hero.dodge + 10
            print("+10 Dodge")
        if A == 3:
            Hero.armor = Hero.armor + 2
            print("+2 Armor")
        if A == 4:
            Hero.health = Hero.health + 10
            Hero.maxHealth = Hero.maxHealth + 10
            print("+10 HP and Max HP")
        C = 0
        D = True
        while C < 20 and D == True:
            B = random.randint(1,4)
            if A == 1 and Hero.power > 3:
                Hero.power = Hero.power - 2
                print("-2 Power")
                D = False
            if A == 2 and Hero.dodge > 6:
                Hero.dodge = Hero.dodge - 6
                print("-6 Dodge")
                D = False
            if A == 3 and Hero.armor > 1:
                Hero.armor = Hero.armor - 1
                print("-1 Armor")
                D = False
            if A == 4 and Hero.health > 6:
                Hero.health = Hero.health - 5
                Hero.maxHealth = Hero.maxHealth - 5
                print("-5 HP and Max HP")
                D = False
            C += 1
        time.sleep(1.5)
    elif buffInput == "2":
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


_________          _______             _______  _               _________ _______  _       
\__   __/|\     /|(  ____ \  |\     /|(  ___  )( \   |\     /|  \__   __/(  ____ \( (    /|
   ) (   | )   ( || (    \/  | )   ( || (   ) || (   ( \   / )     ) (   | (    \/|  \  ( |
   | |   | (___) || (__      | (___) || |   | || |    \ (_) /      | |   | (__    |   \ | |
   | |   |  ___  ||  __)     |  ___  || |   | || |     \   /       | |   |  __)   | (\ \) |
   | |   | (   ) || (        | (   ) || |   | || |      ) (        | |   | (      | | \   |
   | |   | )   ( || (____/\  | )   ( || (___) || (____/\| |        | |   | (____/\| )  \  |
   )_(   |/     \|(_______/  |/     \|(_______)(_______/\_/        )_(   (_______/|/    )_)
                                                                                           

1.) Start
2.) Load 
3.) Exit 

""")
    if menuInput == "1":
        start()
    elif menuInput == "2":
        start()
    elif menuInput == "3":
        quit()
    else:
        quit()

           
def start():
    os.system('clear')
    counter = 0
    print("Welcome Mighty Hero \nA Necromance has been ravaging the lands turning fallen warriors into his minions.\nI wish you better than the ones before you")
    time.sleep(1)
    while counter <= 7:
        path()
        counter += 1
        
    bossCombat()
 


paths = {"I Feel ominous presence over there":combat,
         "There Seems to be a building set up over there":shop,
         "I feel a good about this path":buff,
         "The path looks shaky over there":risk,
         "The road is quite plan":unknown
}

 
def path():
    os.system('clear')
    path1Name, path1Fun = random.choice(list(paths.items()))
    path2Name, path2Fun = random.choice(list(paths.items()))
    path3Name, path3Fun = random.choice(list(paths.items()))
    pathInput = input(f"""
Choose Your Path 
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
        quit()

  
def youDied(lives):
    playerToEnemy()
    print(lives)
    lives -= 1
    if lives == 9:
        print("Right Before the final blow the enemy pause...")
        time.sleep(4)
        print("Your enemy offers you his hand in friendship")
        time.sleep(3)
        print("and stabs you into bits.... Good thing there was 10 of you")
        time.sleep(5)
        restart()
    elif lives >= 1:
        print("another one dead huh")
        time.sleep(2)
        restart()
    else:
        youLose()
 
def playerToEnemy():
    if lives == 10:
        dpc1 = Enemy("The First Warrior",Hero.maxHealth,Hero.power,Hero.armor,Hero.dodge,Hero.gold)
        for A in range(len(Hero.inventory)):
            dpc1.inventory.append(Hero.inventory[A])
        enemylist.append(dpc1)
    elif lives == 9:
        dpc2 = Enemy("The Second Warrior",Hero.maxHealth,Hero.power,Hero.armor,Hero.dodge,Hero.gold)
        for A in (len(Hero.inventory)):
            dpc2.inventory.append(Hero.inventory[A])
        enemylist.append(dpc2)
    elif lives == 8:
        dpc3 = Enemy("The Third Warrior",Hero.maxHealth,Hero.power,Hero.armor,Hero.dodge,Hero.gold)
        for A in (len(Hero.inventory)):
            dpc3.inventory.append(Hero.inventory[A])
        enemylist.append(dpc3)
    elif lives == 7:
        dpc4 = Enemy("The Forth Warrior",Hero.maxHealth,Hero.power,Hero.armor,Hero.dodge,Hero.gold)
        for A in (len(Hero.inventory)):
            dpc4.inventory.append(Hero.inventory[A])
        enemylist.append(dpc4)
    elif lives == 6:
        dpc5 = Enemy("The Fifth Warrior",Hero.maxHealth,Hero.power,Hero.armor,Hero.dodge,Hero.gold)
        for A in (len(Hero.inventory)):
            dpc5.inventory.append(Hero.inventory[A])
        enemylist.append(dpc5)
    elif lives == 5:
        dpc6 = Enemy("The Sixth Warrior",Hero.maxHealth,Hero.power,Hero.armor,Hero.dodge,Hero.gold)
        for A in (len(Hero.inventory)):
            dpc6.inventory.append(Hero.inventory[A])
        enemylist.append(dpc6)
    elif lives == 4:
        dpc7 = Enemy("The Seventh Warrior",Hero.maxHealth,Hero.power,Hero.armor,Hero.dodge,Hero.gold)
        for A in (len(Hero.inventory)):
            dpc7.inventory.append(Hero.inventory[A])
        enemylist.append(dpc7)
    elif lives == 3:
        dpc8 = Enemy("The Eighth Warrior",Hero.maxHealth,Hero.power,Hero.armor,Hero.dodge,Hero.gold)
        for A in H(len(Hero.inventory)):
            dpc8.inventory.append(Hero.inventory[A])
        enemylist.append(dpc8)
    elif lives == 2:
        dpc9 = Enemy("The Ninth Warrior",Hero.maxHealth,Hero.power,Hero.armor,Hero.dodge,Hero.gold)
        for A in (len(Hero.inventory)):
            dpc9.inventory.append(Hero.inventory[A])
        enemylist.append(dpc9)
  
def restart():
    global Hero, dLord
    Hero = Player("Hero",10,5,0,10,0,10)
    dLord = Boss("Necromancer",50,10,5,25,100)
    start()
  
def youLose():
     print("you suck lol")

def youWin():
    print("you won ya")    
        
main()




#TODO

# class Skills:
#     pass


#more enemies

#more paths

#flavor text

#info Text*

#different Starts

#new game plus

#more items