# RPG Game Part 1

## Step 1
Make a Hero class to store the health and power of the hero, and make a `Goblin` class to store the health and power of the goblin. Use a hero object in place of the variables `hero_health` and `hero_power` and use a goblin object in place of the variables `goblin_health` and `goblin_power` all through out the app.

## Step 2
Take the code for the hero attacking the goblin and extract it into a method (call it `attack`) of the `Hero` class. Replace the existing code with a call to the attack method. Hint: `attack` should take in the goblin (enemy) as a parameter: `hero.attack(goblin)`

## Step 3
Similarly, take the code for the goblin attacking the hero and extract it into a method (also call it `attack`) of the Goblin class. Replace the existing code with a call to the attack method. It should look like `goblin.attack(hero)`.

## Step 4
Refactor the while condition:

`while goblin.health > 0 and hero.health > 0:`

to

`while goblin.alive() and hero.alive():`

The health checks should be moved to within the alive methods of Hero and Goblin respectively.

## Step 5
Take the code for printing the health status of the hero and move it into a method called `print_status` of `Hero`. Do the same for the goblin.

## Step 6
Do you see a lot of duplicated or similar code between `Hero` and `Goblin`? What if you can share the duplicated code between them? You can by using inheritance! Create a new class called `Character` and make both `Hero` and `Goblin` inherit from it.

## Step 7
The alive methods on `Hero` and `Goblin` should be identical. Move it into `Character`, and remove them from `Hero` and `Goblin` - now they can simply inherit it from `Character`.

## Step 8: Bonus Challenge
The methods `attack` and `print_status` method in `Hero` and `Goblin` look almost identical, but not quite. Is it possible to move them into the `Character` class as well? Give it a try.

## Step 9: Bonus Challenge 2
Create a zombie character that cannot die and have it fight the hero instead of the goblin.


# RPG Game Part 2

Hero RPG Game: Part 2
You will base your game on version 7 of the game and make mods to the game.

## Characters
1. Make the hero generate double damage points during an attack with a probability of 20%
2. Make a new character called `Medic` that can sometimes recuperate 2 health points after being attacked with a probability of 20%
3. Make a character called `Shadow` who has only 1 starting health but will only take damage about once out of every ten times he is attacked.
4. Make a `Zombie` character that doesn't die even if his health is below zero
5. Come up with at least two other characters with their individual characteristics, and implement them.
6. Give each enemy a bounty. For example, the prize for defeating the `Goblin` is 5 coins, for the Wizard it is 6 coins.

## Items
1. Make a `SuperTonic` item to the store, it will restore the hero back to 10 health points.
2. Add an `Armor` item to the store. Buying an armor will add 2 armor points to the hero - you will add "armor" as a new attribute to hero. Every time the hero is attacked, the amount of hit points dealt to him will be reduced by the value of the armor attribute.
3. Add an `Evade` item to the store. Buying an "evade" will add 2 evade points to the hero - another new attribute on the Hero object. The more evade he has, the more probable that he will evade an enemy attack unscathed. For example: 2 evade points: 10% probably of avoiding attack, 4 evade points: 15% probability of avoiding attack. It should never be possible to reach 100% evasion though.
4. Come up with at least two other items with their unique characteristics and implement them. You can add more attributes to the hero or the characters.

## Bonus
1. Allow items to be used on the battle field. The hero can carry the items with him, and you have the option of choosing to use a tonic at any turn in a battle.
2. Make a `Swap` item, which when used on a battle field, will swap the power values of the two characters for one turn.
3. There is a bug in the store that allows the hero to buy items even if he has no coins. Fix this bug.