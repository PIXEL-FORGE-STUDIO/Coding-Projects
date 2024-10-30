#   Imports And Variables
import random
import time
xp = 0
gold = 0
alive = "true"
#--------------------GAME------------------------#

#   Game Start
answer = input("Do you want to play? (yes/no) : ")
if answer.lower().strip() == "yes":
    time.sleep(0.5)
    #   Dirt Road
    answer = input("You found an old dirt road! Which way do you go? (left/right) : ").lower().strip()
    if answer == "left":
        #   Choice a (fight)
        start = "yes"
        if start == "yes":
            print("You encountered a zombie!")
            time.sleep(0.1)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("What do you do?")
            time.sleep(0.5)
            print("1. Punch it")
            time.sleep(0.2)
            print("2. Hit it with your stick")
            time.sleep(0.2)
            print("3. Run")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            time.sleep(1)
            chosen_num = input("Choice: ")
            if chosen_num == "1":
                chosen_option = "punch it."
            else:
                if chosen_num == "2":
                    chosen_option = "hit it with your stick."
                else:
                    if chosen_num == "3":
                        chosen_option = "run."
            time.sleep(0.1)
            print("You decide to", chosen_option)
            if chosen_num == "3":
                run_attempt = random.randint(1,5)
                if run_attempt == 5:
                    time.sleep(0.2)
                    print("You were attacked!")
                    time.sleep(0.1)
                    alive = false
                    print("GAME OVER")
                    print("Final XP:",xp)
                    print("Final GOLD:",gold)
                else:
                    time.sleep(0.2)
                    print("You escaped!")
                    time.sleep(0.1)
                    print("You won!")
                    time.sleep(0.1)
                    print("+5 XP")
                    xp = xp + 5
            elif chosen_num == "1":
                    punch_attempt = random.randint(1,3)
                    if punch_attempt == 1:
                        time.sleep(0.2)
                        print("You missed.")
                        time.sleep(0.1)
                        print("Your hand was bitten!")
                        time.sleep(0.1)
                        alive = false
                        print("GAME OVER")
                        print("Final XP:",xp)
                        print("Final GOLD:",gold)
                    else:
                        if punch_attempt == 2:
                            time.sleep(0.2)
                            print("It wasn't very effective.")
                            time.sleep(0.1)
                            print("You punch again")
                            punch_attempt = random.randint(1,2)
                            if punch_attempt == 1:
                                time.sleep(0.2)
                                print("You missed!")
                                time.sleep(0.15)
                                print("It grabbed you!")
                                time.sleep(0.1)
                                alive = false
                                print("GAME OVER")
                                print("Final XP:",xp)
                                print("Final GOLD:",gold)
                            else:
                                if punch_attempt == 2:
                                    time.sleep(0.15)
                                    print("You killed it!")
                                    time.sleep(0.1)
                                    print("You won!")
                                    time.sleep(0.1)
                                    print("+20 XP")
                                    xp = xp + 20
                                else:
                                    time.sleep(0.2)
                                    print("You killed it!")
                                    time.sleep(0.1)
                                    print("You won!")
                                    time.sleep(0.1)
                                    print("+10 XP")
                                    xp = xp + 10
            else:
                stick_attempt = random.randint(1,4)
                if stick_attempt == 4:
                    time.sleep(0.2)
                    print("You missed.")
                    time.sleep(0.1)
                    print("It jumped on you!")
                    time.sleep(0.1)
                    alive = false
                    print("GAME OVER")
                    print("Final XP:",xp)
                    print("Final GOLD:",gold)
                else:
                    time.sleep(0.2)
                    print("You killed it!")
                    time.sleep(0.1)
                    print("You won!")
                    time.sleep(0.1)
                    print("+20 XP")
                    xp = xp + 20
            if alive == "true":
                print("UNFINISHED")
    elif answer == "right":
        #   choice b (vill/tent)
        time.sleep(0.5)
        answer = input("You see a village and an abandoned tent, which do you go to? (vill/tent) : ").lower().strip()
        time.sleep(0.2)
        if answer == "vill":
            #   choice b-a
            print("Taveling")
            time.sleep(0.1)
            print("Taveling.")
            time.sleep(0.1)
            print("Taveling..")
            time.sleep(0.1)
            print("Taveling...")
            time.sleep(0.1)
            print("You arrive at the village, but find only a few people remain...")
            time.sleep(0.2)
            print("However, you find a lost bag of gold coins!")
            answer = input("Do you take it to buy supplies, or leave it for its owner? (steal/leave) : ").lower().strip()
            time.sleep(0.2)
            if answer == "steal":
                print("You take the gold, hoping to have enough money for a proper weapon or some dinner.")
                time.sleep(0.05)
                print("+25 GOLD")
                gold = gold + 25
                time.sleep(0.5)
                answer = input("Do you go to the weapon shop or the market to get food? (weapon/food) : ")
                if answer == "weapon":
                    time.sleep(0.3)
                    print("You walk to the nearby weapon shop to buy some gear.")
                    time.sleep(0.3)
                    print("(Blacksmith):")
                    time.sleep(0.4)
                    print("Welcome to my shop! Most swords and axes are pretty cheap, but the guns are quite expesive.")
                    time.sleep(0.2)
                    print("Well, don't be shy, go buy something!")
                    time.sleep(0.2)
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print("What will you buy :")
                    time.sleep(0.3)
                    print("1. A dull, rusty sword - 4G")
                    time.sleep(0.15)
                    print("2. A dull, rusty axe - 6G")
                    time.sleep(0.15)
                    print("3. A sharp, shiny sword - 10G")
                    time.sleep(0.15)
                    print("4. A sharp, shiny axe - 12G")
                    time.sleep(0.15)
                    print("5. An old, run down pistol - 18G")
                    time.sleep(0.15)
                    print("6. A beautiful, brand new rifle - 25G")
                    time.sleep(0.15)
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    answer = input("Choice : ")
                    if answer == "1":
                        print("You find a cheap old sword and purchase it.")
                        time.sleep(0.2)
                        print("(Blacksmith):")
                        time.sleep(0.4)
                        print("Goodbye!")
                    elif answer == "2":
                        print("You find a cheap old axe and purchase it.")
                        time.sleep(0.2)
                        print("(Blacksmith):")
                        time.sleep(0.4)
                        print("Goodbye!")
                    else:
                        if answer == "3":
                            print("You find a beautiful new sword and purchase it.")
                            time.sleep(0.2)
                            print("(Blacksmith):")
                            time.sleep(0.4)
                            print("Goodbye!")
                        elif answer == "4":
                            print("You find a beautiful new axe and purchase it.")
                            time.sleep(0.2)
                            print("(Blacksmith):")
                            time.sleep(0.4)
                            print("Goodbye!")
                        else:
                            if answer == "5":
                                print("You find a worn down pistol and purchase it.")
                                time.sleep(0.2)
                                print("(Blacksmith):")
                                time.sleep(0.4)
                                print("Goodbye!")
                            elif answer == "6":
                                print("You find a rifle with the same symbol as the sign outside the shop and purchase it.")
                                time.sleep(0.2)
                                print("(Blacksmith):")
                                time.sleep(0.2)
                                print("I just made that beauty myself last week. I hope you like it!")
                                time.sleep(0.4)
                                print("Goodbye!")
                            else:
                                time.sleep(0.3)
                                print("You awkwardly stare at the blacksmith, then turn around leave without saying a thing.")
                                time.sleep(0.2)
                                print("The blacksmith shoots you in the back of the head for your disrespect!")
                                time.sleep(0.05)
                                alive = false
                                print("GAME OVER")
                                print("Final XP:",xp)
                                print("Final GOLD:",gold)
                    if alive == "true":
                        print("A horde of zombies breaks through the city's safety wall!")
                        answer = input("Will you flee the city, or help fight the horde? (flee/fight) : ")
                        if answer == "flee":
                            print("You run from the attack, and sneak through the back gate.")
                            time.sleep(0.2)
                            print("You sprint into a dense jungle nearby, stopping to catch your breath.")
                            time.sleep(0.2)
                            print("When you finally turn around, you see you've already ran over two miles from the village!")
                            time.sleep(0.2)
                            print("You tear some branches off of trees and pluck large leaves from plants to build a little shelter.")
                            time.sleep(0.2)
                            print("However, it'll only last a short while...")
                            time.sleep(0.8)
                        elif answer == "fight":
                            print("You choose to help the guards fight off the horde!")
                        else:
                            print("WIP")
            elif answer == "leave":
                print("You simply wait until someone walks by, asking if you've seen his gold.")
                time.sleep(0.1)
                print("You show him the bag, and he thanks you.")
                time.sleep(0.1)
                print("He even gives you some of the gold as a reward!")
                time.sleep(0.05)
                print("+10 GOLD / +20 XP")
                xp = xp + 20
                gold = gold + 10
                print("MORE COMING SOON")
            else:
                print("You get caught reaching for the money and are put in jail")
                time.sleep(0.05)
                alive = false
                print("GAME OVER")
                print("Final XP:",xp)
                print("Final GOLD:",gold)
        elif answer == "tent":
            #   choice b-b (tent)
            time.sleep(0.2)
            print("You stay in the tent overnight...")
            time.sleep(0.15)
            print("But are awoken by scary noises!")
            zombie_or_bear = random.randint(1,2)
            time.sleep(0.1)
            if zombie_or_bear == 1:
                print("You see a zombie that fell off a cliff!")
                time.sleep(0.1)
                print("You suvived the night!")
                time.sleep(0.05)
                print("+20 XP")
                xp = xp + 20
                answer = input("Will you look for food in the field or collect sticks and stones in the forest? (food/collect) : ").lower().strip()
                if answer == "food":
                    #   choice b-b-a (food)
                    safe_or_snake = random.randint(1,2)
                    time.sleep(0.1)
                    if safe_or_snake == 1:
                        time.sleep(0.2)
                        print("While you are walking through the field, you accidentally step on a snake, so you bring it home to cook it.")
                        time.sleep(0.1)
                        print("You discover a small rabbit hiding in your tent, and start a fire to cook it and the snake you killed.")
                        time.sleep(0.1)
                        print("You fill your empty stomach with a warm meal.")
                        time.sleep(0.05)
                        print("+10 XP")
                        xp = xp + 10
                        print("MORE COMING SOON")
                    else:
                        print("While you are walking through the field, a snake jumps out and bites you!")
                        print("You stumble home with only a handful of berries, and chop off the bottom half of your leg to prevent the snake venom from spreading.")
                        print("-10 XP")
                        if xp >= 10:
                            xp = xp - 10
                            print("MORE COMING SOON")
                elif answer == "collect":
                    #   choice b-b-b (collect)
                    print("You wander into the forest to collect materials.")
                    print("You collect enough sticks and stones to fix the broken tent.")
                    print("You pluck a few juicy bugs of of a shrub to roast for dinner.")
                    print("MORE COMING SOON")
                else:
                    print("You run in circles and scream like a crazy person, until...")
                    time.sleep(0.15)
                    print("A wolf runs out of the forest and mauls you!")
                    time.sleep(0.05)
                    alive = false
                    print("GAME OVER")
                    print("Final XP:",xp)
                    print("Final GOLD:",gold)
            else:
                print("A bear jumps out at you!")
                time.sleep(0.1)
                print("You are torn to shreds!")
                time.sleep(0.05)
                alive = false
                print("GAME OVER")
                print("Final XP:",xp)
                print("Final GOLD:",gold)
        else:
            time.sleep(0.3)
            print("You stand there undicisively until...")
            time.sleep(0.15)
            zombie_or_starve = random.randint(1,2)
            if zombie_or_starve == 1:
                print("You get trampled by a horde of zombies!")
            else:
                print("You die of starvation!")
                alive = false
                print("GAME OVER")
                print("Final XP:",xp)
                print("Final GOLD:",gold)
    else:
        print("You got lost!")
        alive = false
        print("GAME OVER")
        print("Final XP:",xp)
        print("Final GOLD:",gold)
else:
    alive = false
    print("Too bad! I really wanted to play D:")
    
#   End of Script
if alive == "true":
    time.sleep(3)
    print(" ")
    print("I Hope You Had Fun! :D")
    time.sleep(20)
else:
    time.sleep(5)