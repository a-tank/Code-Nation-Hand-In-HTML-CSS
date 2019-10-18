##Text Based Adventure Game
##by Team 1 (BenC, AldT, TomL, TimE)
import random
import time

char_name = input(str("What's your name adventurer? "))

# HIT POINTS

hit_points = 20
import random

def d4_damage():
    damage = random.randint(1, 4)
    print('You have taken damage of {} hit points!'.format(damage))
    return damage

def d6_damage():
    damage = random.randint(1, 6)
    print('You have taken damage of {} hit points!'.format(damage))
    return damage

def d8_damage():
    damage = random.randint(1, 8)
    print('You have taken damage of {} hit points!'.format(damage))
    return damage

def dead_check(hp):
    if hp < 1:
        return (char_death())
    else:
        return (' ')
    
#use this for small damage recieved
def hp_loss_small(hp):
    return hp - d4_damage()
"""
print('Ouch!! That stung!')
hp = hp_loss_small(hp) 
print('You are now down to {} hit points.'.format(hp))
dead_check(hp)
"""

#use this for medium damage recieved
def hp_loss_medium(hp):
    return hp - d6_damage()
"""
print ("Arrgh!! That hurt!")
hp = hp_loss_medium(hp) 
print('You are now down to {} hit points.'.format(hp))
dead_check(hp)
"""

#use this for large damage recieved
def hp_loss_large(hp):
    return hp - d8_damage()
"""
print ("OWWWW!!! That really hurt!!")
hp = hp_loss_large(hp) 
print('You are now down to {} hit points.'.format(hp))
dead_check(hp)
"""


def title():
    print (" LOADING... PLEASE WAIT ")
    print ()
    time.sleep (1)
    print ("|<<<<<<<<<<<BEST ENJOYED IN FULL SCREEN!<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>DO IT NOW!!!!!>>>>>>>>>>>>>>>>>>>>>>>>>>>| ")
    time.sleep(1)
    print()
    time.sleep(1)
    print()
    time.sleep(1)
    print()
    print ("I hope you're ready for this...? ")
    print()
    time.sleep(2)
    print ("    ██████  ███▄    █  ▄▄▄       ██▀███  ▓█████  ▄▄▄▄    ██▀███   ██▓ ▄▄▄       ██▀███    ██████  ")
    time.sleep(2)
    print ("  ▒██    ▒  ██ ▀█   █ ▒████▄    ▓██ ▒ ██▒▓█   ▀ ▓█████▄ ▓██ ▒ ██▒▓██▒▒████▄    ▓██ ▒ ██▒▒██    ▒  ")
    time.sleep (1)
    print ("  ░ ▓██▄   ▓██  ▀█ ██▒▒██  ▀█▄  ▓██ ░▄█ ▒▒███   ▒██▒ ▄██▓██ ░▄█ ▒▒██▒▒██  ▀█▄  ▓██ ░▄█ ▒░ ▓██▄    ")
    time.sleep (1)
    print ("    ▒   ██▒▓██▒  ▐▌██▒░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄ ▒██░█▀  ▒██▀▀█▄  ░██░░██▄▄▄▄██ ▒██▀▀█▄    ▒   ██▒ ")
    time.sleep (1)
    print ("  ▒██████▒▒▒██░   ▓██░ ▓█   ▓██▒░██▓ ▒██▒░▒████▒░▓█  ▀█▓░██▓ ▒██▒░██░ ▓█   ▓██▒░██▓ ▒██▒▒██████▒▒ ")
    time.sleep (1)
    print ("  ▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░░▒▓███▀▒░ ▒▓ ░▒▓░░▓   ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░ ")
    time.sleep (1)
    print ("  ░ ░▒  ░ ░░ ░░   ░ ▒░  ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░▒░▒   ░   ░▒ ░ ▒░ ▒ ░  ▒   ▒▒ ░  ░▒ ░ ▒░░ ░▒  ░ ░ ")
    time.sleep (1)
    print ("  ░  ░  ░     ░   ░ ░   ░   ▒     ░░   ░    ░    ░    ░   ░░   ░  ▒ ░  ░   ▒     ░░   ░ ░  ░  ░   ")
    time.sleep (1)
    print ("        ░           ░       ░  ░   ░        ░  ░ ░         ░      ░        ░  ░   ░           ░   ")
    time.sleep (1)
    print ("                                                      ░                                           ")
    time.sleep (1)
    print ('by Team 1 (BenC, AldT, TomL, TimE)')
    time.sleep (3)
    print ()

def char_death():
            print ()
            print ("          _,.-------.,_              " )
            print ("      ,;~'             '~;,          " )
            print ("    ,;                     ;,        " )
            print ("   ;                         ;       " )
            print ("  ,'                         ',      " )
            print (" ,;                           ;,     " )
            print (" ; ;      .           .      ; ;     " )
            print (" | ;   ______       ______   ; |     " )
            print (" |  `/~'     ~' . '~     '~\'  |     " )
            print (" |  ~  ,-~~~^~, | ,~^~~~-,  ~  |     " )
            print ("  |   |        }:{        |   |      " )
            print ("  |   l       / | \       !   |      " )
            print ("  .~  (__,.--' .^. '--.,__)  ~.      " )
            print ("  |     ---;' / | \ `;---     |      " )
            print ("   \__.       \/^\/       .__/       " )
            print ("    V| \                 / |V        " )
            print ("     | |T~\___!___!___/~T| |         " )
            print ("     | |`IIII_I_I_I_IIII'| |         " )
            print ("     |  \,III I I I III,/  |         " )
            print ("      \   `~~~~~~~~~~'    /          " )
            print ("        \   .       .    /           " )
            print ("          \.    ^    . /             " )
            print ("             ^~~~^~~~^               " )
            time.sleep(2)
            print ()
            print ()
            print ("__   _______ _   _   _   _   ___  _   _ _____  " )
            print ("\ \ / /  _  | | | | | | | | / _ \| | | |  ___| " )
            print (" \ V /| | | | | | | | |_| |/ /_\ \ | | | |__   " )
            print ("  \ / | | | | | | | |  _  ||  _  | | | |  __|  " )
            print ("  | | \ \_/ / |_| | | | | || | | \ \_/ / |___  " )
            print ("  \_/  \___/ \___/  \_| |_/\_| |_/\___/\____/   ")
            print ()
            print ("         ______ _____ ___________    " )
            print ("         |  _  \_   _|  ___|  _  \   " )
            print ("         | | | | | | | |__ | | | |   " )
            print ("         | | | | | | |  __|| | | |   " )
            print ("         | |/ / _| |_| |___| |/ /    " )
            print ("         |___/  \___/\____/|___/     " )
            print ()
            print ("R.I.P {} . You have failed, your rotting corpse will be picked over by tiny fae and your loved ones will never know what happened to you.".format(char_name))
            print()
            time.sleep(2)
            print()
            print ("Game developed by Team One, Code Nation, Altrincham: Ben_C, Ald_T, Tom_L, Tim_E" )
            time.sleep(4)
            play_game()


def win_cond():
    print("You have vanquished the feral fae that reside in this hellish place.")
    print()
    time.sleep(1)
    print("You pile your pockets and pack full with gold, jewellery, finely crafted magical weapons and potions from the treasure stash, near the top you find a set of keys which must belong to the bar tender.")
    print()
    time.sleep(1)
    print("You take one final look around and are sure you’ve acquired all the riches this place has to offer.")
    print()
    time.sleep(1)
    print("You step onto the mandala of teeth and the same dizzying sensation hits you, you are transported back to the forest where you started.")
    print()
    time.sleep(1)
    print("You find your way limping back to “The Izzet Inn” and hand the keys back to the bar tender.")
    print()
    time.sleep(1)
    print("He looks at you, muddy, cut up and bleeding, holding out a ring of keys to him")
    print()
    time.sleep(1)
    print("“Hey thanks, but these aren’t my keys. I found my keys just after you’d left. I’d left them in my other apron. But you can still stay free if you’d like, hope you didn’t go to too much trouble on my account.”")
    print()
    time.sleep(1)
    print("You sigh, resisting the urge to murder the incompetent peasant where he stands.")
    print()
    time.sleep(1)
    print("You lean across the bar and take a bottle of something that looks strong and alcoholic, he looks like he’s about to protest but you shoot him a deathly glare and he shuts up.")
    print()
    time.sleep(1)
    print("Limping up to your room, you enter, it looks clean and welcoming, the bed is very soft and tempting.")
    print()
    time.sleep(1)
    print("You take off your pack, heavy with valuable items and recovered treasure, you suppose it wasn’t all bad. You strip off your battered armour and your shredded clothing.")
    print()
    time.sleep(1)
    print("Sat on your bed you start to pull dozens of tiny stingers, thorns and broken fae spear heads out of your skin cleaning the dozens of tiny wounds with the alcohol and drinking heavily as well.")
    print()
    time.sleep(1)
    print("You lay back and pull the covers over yourself.")
    print()
    time.sleep(1)
    print("You are quite pleased with your haul.")
    print()
    time.sleep(1)
    print("You’ve done well.")
    print ()
    print ()
    print ("  $$\     $$\  $$$$$$\  $$\   $$\       $$\      $$\ $$$$$$\ $$\   $$\  " )
    print ("  \$$\   $$  |$$  __$$\ $$ |  $$ |      $$ | $\  $$ |\_$$  _|$$$\  $$ | " )
    print ("   \$$\ $$  / $$ /  $$ |$$ |  $$ |      $$ |$$$\ $$ |  $$ |  $$$$\ $$ | " )
    print ("    \$$$$  /  $$ |  $$ |$$ |  $$ |      $$ $$ $$\$$ |  $$ |  $$ $$\$$ | " )
    print ("     \$$  /   $$ |  $$ |$$ |  $$ |      $$$$  _$$$$ |  $$ |  $$ \$$$$ | " )
    print ("      $$ |    $$ |  $$ |$$ |  $$ |      $$$  / \$$$ |  $$ |  $$ |\$$$ | " )
    print ("      $$ |     $$$$$$  |\$$$$$$  |      $$  /   \$$ |$$$$$$\ $$ | \$$ | " )
    print ("      \__|     \______/  \______/       \__/     \__|\______|\__|  \__| " )
    print ("                                                                         ")
    print ()
    print ()
    time.sleep(3)
    print ("CODING: " )
    print ()
    time.sleep(1)
    print ("MAIN CODE: ")
    print ()
    time.sleep(1)
    print ("BenC " )
    print ()
    time.sleep(1)
    print ("SECONDARY CODING:")
    print ()
    time.sleep(1)           
    print ("AldT " )
    print ()
    time.sleep(1)
    print ("TomL " )
    print ()
    time.sleep(1)
    print ("PRIMARY BUG HUNTER: " )
    print()
    time.sleep(1)
    print ("TomL " )
    print()
    time.sleep(1)
    print ("SECONDARY BUG HUNTERS: " )
    print()
    time.sleep(1)
    print ("TimE" )
    print()
    time.sleep(1)
    print ("AldT " )
    print()
    time.sleep(1)
    print ("BenC " )
    time.sleep(1)
    print()
    time.sleep(1)
    print()
    print ("STORY CREATION: " )
    print ()
    time.sleep(1)
    print ("Creative Director: ".upper())
    print()
    time.sleep(1)
    print ("AldT " )
    print ()
    time.sleep(1)
    print ("Creative inputs: ".upper())
    print()
    time.sleep(1)
    print ("BenC " )
    print()
    time.sleep(1)
    print ("TomL " )
    print ()
    time.sleep(1)
    print ("TimE " )
    time.sleep(1)
    print ("STORY: " )
    print()
    time.sleep(1)
    print ("Story boards and admin: ".upper())
    print()
    time.sleep(1)
    print ("TomL " )
    print()
    time.sleep(1)
    print ("TimE  " )
    print()
    time.sleep(1)
    print ("BenC " )
    print()
    time.sleep(1)
    print ("AldT " )
    print()
    time.sleep(1)
    print ("THANK YOU FOR PLAYING OUR FIRST EVER GAME " )
    time.sleep(5)
    play_game()


def r5_choice(hp):
    print('Your current hp is {}'.format(hp))
    print ("With snarls and battle cries the faeries launch themselves at you...")
    print ("1. Draw your sword and charge in bravely.")
    print ("2. Use a torch from the wall and your hipflask of rum to try and burn them.")
    print ("3. Run away from the swarm.")
    r5_query=input("Danger abounds, what's your response? ")
    def r5_opt1(hp):
        print ("The battle is long and hard, but you overcome the swarm of evil little creatures, slicing and thrusting with your weapon you down them one at a time. " )
        print()
        time.sleep(1)
        print ("OWWWW!!! That really hurt!!")
        hp = hp_loss_large(hp) 
        print('You are now down to {} hit points.'.format(hp))
        dead_check(hp)
        print ("Every fae you cleave out of the air is immensely satisfying, their black ichor soaks the walls and floors, they lay twitching and dead. " )
        print()
        time.sleep(1)
        print ("However they have done much damage to you with their stabbing spears and venomous stingers. " )
        print()
        time.sleep(1)
        print ("You are bleeding heavily. " )
        win_cond()
    def r5_opt2(hp):
        print ("You quickly grab a torch from the wall, it burns hot and true. " )
        print()
        time.sleep(1)
        print ("You take a big gulp from your hip flask, but instead of swallowing you spit it out, engulfing many of the faeries in burning alcohol. " )
        print()
        time.sleep(1)
        print ("Their hair-thin wings sizzle and fry under the heat and they fall out of  the sky screaming and burning. " )
        print()
        time.sleep(1)
        print ("The remaining faeries panic and try to climb high into the air. " )
        print()
        time.sleep(1)
        print ("You take another draught and try again, burning several more. " )
        print()
        time.sleep(1)
        print ("This seems effective, you burn the last couple out of the air with the last slug of your rum then angrily stamp up and down on their writhing burning bodies. " )
        print()
        time.sleep(1)
        print ("The small creatures give a satisfying crunch as you crush them beneath the heel of your sturdy leather boots. " )
        win_cond()
    def r5_opt3(hp):
        print ("You turn tail and flee, but the small fae are far to quick and catch you, you feel agony in your leg as one of their spears is driven into your achilles tendon. " )
        print()
        time.sleep(1)
        print ("You fall to the ground, the faeries swarm you, you try to bat them away with your hands but you are too slow. " )
        print()
        time.sleep(1)
        print ("With a thousand tiny stab wounds you are slowly murdered by the fae. " )
        print()
        time.sleep(1)
        print ("They will add your items to their collection of treasure and use your teeth for their ritual magics. " )
        char_death()
    if r5_query == "1":
        r5_opt1(hp)
    elif r5_query == "2":
        r5_opt2(hp)
    elif r5_query == "3":
        r5_opt3(hp)
    elif r5_query == "4":
        r5_opt4(hp)

def room_5(hp):
    print ("You open the door and peek inside. There is a large room, on the floor lay many skeletons of fellow explorers, some dressed in armour, some in wizards robes. All of the skulls are missing their teeth. There is a large pile of shiny coins, gems, jewellery and other expensive looking items at the foot of a statue of a huge faerie. " )
    time.sleep(1)
    print()
    print ("In the middle of the room is a large amethyst geode, cut in half, some sort of magical image is broadcast in the centre of it, you notice it is you from behind, they have been watching you all this time. " )
    time.sleep(1)
    print()
    print ("There are about a dozen malevolent faeries sat around on the floor laughing hysterically and pointing at you as you realise this whole torturous dungeon has been just a means of entertainment to them, a way to harvest teeth and gold from unwary or unlucky adventurers. " )
    time.sleep(1)
    print()
    print ("There is another mandala, the same as you entered, but this one is made from hundreds of pulled teeth placed in intricate arcane circles. " )
    time.sleep(1)
    print()
    print ("The tiny fae creatures stop laughing and pick up small wooden spears the size of knitting needles. " )
    time.sleep(1)
    print()
    print ("They buzz into the air with a high pitched sound like a thousand hungry mosquitoes. " )
    time.sleep(1)
    print()
    r5_choice(hp)

##Room 4 - the pit ##
def room_4(hp):
        print ("You followed the chuckling fairy through the door at the end. He flies away, but you can still hear his laughter tinkling in the distance. ")
        print ()
        time.sleep(2)
        print ("This room has a small ledge you are standing on, in front of you is a huge pit. ")
        print ()
        time.sleep(2)
        print ("Eighty foot across, there are two small six inch wide ledges on either side leading from where you stand to the door opposite with a torch burning on it and a rotted looking rope bridge ahead. ")
        print ()
        time.sleep(2)
        r4_choice(hp)

def r4_opt4(hp):
        print ("Using your rope and grapnel as a safety line and tying your pack to the other end, you carefully but steadily make your way around the edge of the chasm. ")
        time.sleep(1)
        print()
        print ("Success, you've made it across safely to the other side. Your pack is somewhere below you in the depths, but the line has not snapped. You begin to pull. ")
        time.sleep(1)
        print()
        print ("You retrieve your pack. Everything appears to be there, and it's that little bit more travel worn. Not so much stone washed, as cliff bashed... ")
        time.sleep(1)
        print()
        print ("You proceed to the next room... ")
        room_5(hp)

def r4_opt1(hp):
        print ("You carefully make your way across the bridge, listening to the ominous creaking of it's rigging under strain.")
        time.sleep(1)
        print (".")
        time.sleep(1)
        print (".")
        time.sleep(1)
        print (".")
        time.sleep(1)
        print (".")
        time.sleep(1)
        print (".")
        print ("You heard a sound like a guitar string snapping, you could almost swear there's also the sound of a faery voice calling your name in the distance... " )
        time.sleep(1)
        print (char_name)
        time.sleep(3)
        print (char_name)
        time.sleep(1)
        print (char_name)
        time.sleep (1)
        print ("The rope bridge snaps, you cling on to the shreds of fibre to no avail. With great force you swing into the wall. ")
        print ()
        time.sleep(2)
        print ("Your head bounces off the side of the chasm with a wet crack. Everything goes black. ")
        time.sleep(1)
        print (".")
        time.sleep(1)
        print (".")
        time.sleep(1)
        print ("{} is with us no more... ".format(char_name))
        char_death()

def r4_opt2(hp):
        print ("You edge along the path to the left, pressing yourself against the wall, it is quite dark in the room and you slip on some moss. You try to regain your balance but your pack sends you off balance and you plumet into the pit ")
        time.sleep (2)
        r4_falling(hp)

def r4_opt3(hp):
        print ("You go to the right hand path, you take your time and slowly edge along the narrow ledge, it feels like an eternity but you half way through you get the urge to look down, you know you shouldn’t but you can’t help yourself. You look down into the blackness and vertigo hits you, you loose your balance and fall into the pit")
        time.sleep (2)
        r4_falling(hp)

##Room 4 options ##
def r4_choice(hp):
    print('Your current hp is {}'.format(hp))
    print ("How do you want to proceed?" )
    print ("1. Chance the rope bridge " )
    print ("2. Try the path to the left " )
    print ("3. Try the path to the right " )
    print ("4. Use something from your pack " )
    r4_query = input ()
    if r4_query == "1":
            r4_opt1 (hp)
    elif r4_query == "2":
            r4_opt2 (hp)
    elif r4_query == "3":
            r4_opt3 (hp)
    elif r4_query == "4":
            r4_opt4 (hp)
    else:
        print ("Invalid input, try again " )
        r4_choice(hp)

def r4_falling(hp):
    print ()
    time.sleep (1)
    print (".")
    time.sleep (1)
    print (".")
    print ()
    time.sleep (1)
    print (".")
    time.sleep (1)
    print (".")
    print ()
    time.sleep (1)
    print (".")
    time.sleep (1)
    print (".")
    print ()
    time.sleep (1)
    print (".")
    time.sleep (1)
    print ("You are still falling!")
    time.sleep(1)
    print (".")
    time.sleep(1)
    print (".")
    print ()
    time.sleep(1)
    print (".")
    time.sleep(1)
    print (".")
    print ()
    time.sleep(1)
    print ("You are still falling!")
    time.sleep(1)
    print (".")
    time.sleep(1)
    print (".")
    time.sleep(1)
    print (".")
    time.sleep(1)
    print (".")
    print ()
    time.sleep(1)
    print (".")
    time.sleep(1)
    print ( )
    print ("   /     " )
    print (" `\_\    " )
    print ("     \   " )
    print ("    /O\  " )
    print ()
    time.sleep(2)
    print ("Oddly, just before you hit the bottom of the chasm you feel a surge of energy and suddenly teleport to the top, only to fall again in an endless cycle. ")
    time.sleep(3)
    print ("You are still falling!")
    print ("What do you want to do? ")
    print ("1: Reach out for the side of the chasm ")
    print ("2: Panic! ")
    print ("3: Use a parachute ")
    print ("Or maybe you should try option 4? ")
    r4f_query = input()

    def r4f_opt1(hp):
            print ("You can't quite reach the edge. You continue falling. ")
            print ()
            r4_falling(hp)
    def r4f_opt2(hp):
            print ("You scream, soil yourself, and vomit. None of this helps. You continue falling. ")
            print ()
            print('Nooo!!! Your level optimism drops')
            hp = hp_loss_small(hp) 
            print('You are now down to {} hit points.'.format(hp))
            dead_check(hp)
            r4_falling(hp)
    def r4f_opt3(hp):
            print ("You forgot to pack a parachute. However you do have a towel. Using it as a parachute slows your descent slightly, but you have no control. ")
            print ()
            print ("You continue falling, just a little slower. ")
            print ()
            r4_falling(hp)
    def r4f_opt4(hp):
            print ("You rummage through your pack, you pull out your trusty climbing rope and grppling hook.")
            print()
            time.sleep(1)
            print ("After a few missed attempts you manage to catch the grapnel on to the edge by the door where you entered. ")
            print ()
            print ("You climb to the relative safety of the ledge, but you have progressed no further. ")
            print ()
            room_4(hp)

    if r4f_query == "1":
            r4f_opt1 (hp)
    elif r4f_query == "2":
            r4f_opt2 (hp)
    elif r4f_query == "3":
            r4f_opt3 (hp)
    elif r4f_query == "4":
            r4f_opt4 (hp)
    else:
        print ("Invalid input, try again " )
        r4f_query(hp)

##Room 3 options ##
def r3_choice(hp):
        print('Your current hp is {}'.format(hp))
        print ("What would you like to do? ")
        print ("1. Try to chop your way through the branches and vines inhabitting the corridor ")
        print ("2. Back out of the room ")
        print ("3. Try to rush through the corridor hoping the brambles don't get you ")
        print ("4. Copy the fae creature " )
        r3_query = input ()
        time.sleep (1)
        def r3_opt1(hp):
            print ("You take out your wood axe and try to chop a path through the brambles. ")
            print ()
            print ("Arrgh!! That hurt!")
            hp = hp_loss_medium(hp) 
            print('You are now down to {} hit points.'.format(hp))
            dead_check(hp)
            time.sleep (1)
            room_4(hp)
        def r3_opt2(hp):
            print ("You edge out of the room backwards as you go backwards the thorns recede to the edge of the room again. You are back at the enterance to the room. ")
            print ()
            time.sleep (1)
            r3_choice()
        def r3_opt3(hp):
            print ("You try to outrun the brambles, you dash forwards to the door, but they lash out and capture you, you struggle forwards with the briar thorns tearing at your clothing and flesh, you manage to make it to the door..." )
            print ()
            time.sleep(2)
            print ("You are bleeding from a hundred small cuts and bruises, the thorns wrap around you and peel the flesh from your bones. You are trapped, bleeding...")
            print ()
            time.sleep (1)
            print ("The thorns tear you apart. " )
            char_death()
        def r3_opt4(hp):
            print ("You walk backwards, chuckling at how ridiculous you must look. The Branches and thorns pay you no heed. " )
            time.sleep(1)
            room_4(hp)


        if r3_query == "1":
            r3_opt1(hp)
        elif r3_query == "2":
            r3_opt2(hp)
        elif r3_query == "3":
            r3_opt3(hp)
        elif r3_query == "4":
            r3_opt4(hp)
        else:
            print ("Invalid input, try again " )
            r3_choice(hp)

##Room 3 - Corridor ##
def room_3(hp):
        print ("As you look into this room you realise it is in fact a long corridor with a door at the far end. " )
        print()
        time.sleep(1)
        print("Like the previous rooms it appears to have been grown from tree roots and branches. ")
        print ()
        time.sleep (1)
        print ("You notice a small faerie in the middle of the room, it’s the one you chased through the forest and still has the brooch. ")
        print ()
        time.sleep (1)
        print ("It laughs at you and flies backwards to a door on the other side of the long room, it flies through a small hole in the door that closes behind it. ")
        print ()
        time.sleep (1)
        print ("You look around and see there are thick brambles around the edge of the room. As you step into the room the brambles seem to draw closer with each step. " )
        print()
        time.sleep(1)
        print("They appear to be reaching out to you, you are near the middle of the room and the brambles are nearly at your feet. ")
        time.sleep (1)
        r3_choice(hp)

## Room 1 options ##
def r1_choice(hp):
    print('You currently have {} hp'.format(hp))
    print ("Which way do you want to go? ")
    print ("'n' for North" )
    print ("'e' for East" )
    print ("'s' for South" )
    print ("'w' for West" )
    r1_query = input()
    if r1_query == "e" or r1_query == "E":
        room_2(hp)
    elif r1_query == "s" or r1_query == "S":
        room_3(hp)
    elif r1_query == "n" or r1_query == "N":
        print ("You inspect the wall to the north, it appears to be made of tree roots tightly woven by growth. There is no way through. ")
        time.sleep(2)
        r1_choice(hp)
    elif r1_query == "w" or r1_query == "W":
        print ("You inspect the western wall, it appears to be made of roots tightly woven by growth. There is no way through. ")
        time.sleep(2)
        r1_choice(hp)
    else:
        print ("Invalid input, try again " )
        r1_choice(hp)

##Room 2 options ##
def r2_choice(hp):
    r2_query = input ("How will you deal with the hornets? " )
    def r2_opt1(hp):
            print ("They are too small, and too fast to slash at. They sting you remorselessly, forcing you back the way you came. ")
            print ()
            print('Ouch!! That stung!')
            hp = hp_loss_small(hp) 
            print('You are now down to {} hit points.'.format(hp))
            dead_check(hp)
            time.sleep (2)
            r1_choice(hp)
    def r2_opt2(hp):
            print ("They seem unbothered by the fire, you manage to burn a few but they sting you horribly. You are forced to flee back the way you came. ")
            print ()
            print ("Arrgh!! That hurt!")
            hp = hp_loss_medium(hp) 
            print('You are now down to {} hit points.'.format(hp))
            dead_check(hp)
            time.sleep (2)
            r1_choice(hp)
    def r2_opt3(hp):
            print ("You unhook your trusty frying pan from your pack, a vital piece of equipment for any traveller, its wide shape is perfect for swatting wasps. A few manage to sting you but you manage to swat most of them away from you before they hurt you too badly. You slam the door closed and manage to close most of the wasps in the empty room. ")
            time.sleep(2)
            r1_choice(hp)
    def r2_opt4():
            print ("Sensibly you close the door and run away before they can get to you. " )
            r1_choice(hp)

    if r2_query == "1":
        r2_opt1(hp)
    elif r2_query == "2":
        r2_opt2(hp)
    elif r2_query == "3":
        r2_opt3(hp)
    elif r2_query == "4":
        r2_opt4(hp)
    else:
        print ("Invalid input, try again " )
        r2_choice(hp)

##Room 2 - wasps ##
def room_2(hp):
        print ("You have chosen to go through the eastern door, it is unlocked but stiff. You give it a hard push and stumble through. ")
        print('Your current hp is {}'.format(hp))
        print ()
        time.sleep (1)
        print("   '     ,  ,  " )
        print("    ', , '   " )
        print("       ''     _---.    ..;%%%;, ." )
        print("         '' .',  ,  .==% %%%%%%% ' . " )
        print("           ~@, %%%   =%% %%%%%%;  ; ;-_   " )
        print("           %; %%%%%  .;%;%%%@%p ---; _  '-_     " )
        print("           %; %%%%% __;%%;p/; O        --_ '-,_    " )
        print("            q; %%% /v \;%p ;%%%%%;--__    ''-__'-._    " )
        print("            //\\/ // \  % ;%%%%%%%;',/%\_  __  ''-_'\_    " )
        print("            \  / //   \/   ;%% %; %;/\%%%%;;;;\    '- _\    " )
        print("               ,'             %;  %%;  %%;;'  ';%       -\-_    " )
        print("          -=\=/             __%    %%;_ |;;    %%%\          \    " )
        print("                          _/ _=      \==_;;,_ %%%; % -_      /    " )
        print("                         / /-          =%- ;%%%%; %%;  \--__/    " )
        print("                        //=             ==%-%%;  %; %    " )
        print("                        /             _=_-  d  ;%; ;%;  :F_P:    " )
        print("                        \            =,-     d%%; ;%%;    " )
        print("                                    //        %  ;%%;    " )
        print("                                   //          d%%%/    " )
        print("                                    \           %%/    " )
        print("                                                 V ")
        print()
        time.sleep(1)
        print ("As you push the stiff door open, you hear a sound like a dozen sheets of paper tearing at once, followed by a furious buzzing noise. There was a wasps nest built on the other side of the door and you have torn it in half. Dozens of angry yellow hornets buzz around you. What will you try and do? ")
        print ("1: Draw your sword and attack the wasps ")
        print ("2: Light a torch and wave it at them ")
        print ("3: Use your frying pan to swat them? ")
        r2_choice(hp)

##Room 1 - Entrance ##
def room_1(hp):
    print ("You find yourself in a dingy room with two sturdy looking doors.")
    print ()
    time.sleep (1)
    print ("There is a door to the SOUTH, and another to the EAST. ")
    print ()
    time.sleep (1)
    print ("The walls to the NORTH and WEST appear to be organic. ")
    print ()
    time.sleep (1)
    r1_choice(hp)

def play_game():
    hp = 20
    title()
    print ("You {}, are a travelling adventurer, you make a living by exploring the world and seeing wonderful and strange places and dealing with the inhabitants. ".format(char_name))
    print ()
    time.sleep (3)
    print ("You’ve come to a small hamlet called “Clearfields”, it is a cozy little place with a small road stop tavern. You decide to take a rest and book a room. ")
    print ()
    time.sleep (3)
    print ("You approach the building, a stone house with two floors and a sign that reads “The Izzet Inn” hanging outside. The bartender is a large man with a welcoming attitude and a big smile. ")
    print ()
    time.sleep (3)
    print ("As you ask for a room he says ''I’m afraid I can’t get into any of the rooms at the moment. We’ve been plagued by a spree of thefts lately and they’ve taken my keyring.'' ")
    print ()
    time.sleep (3)
    print ("''You look like the type that likes a good mystery, and I’ve seen many of you adventuring types pass through in my time here.'' ")
    print()
    time.sleep(3)
    print ("''I’ll let you stay for a week for free, with all you can drink access to my taproom; IF you can bring back my keyring.'' ")
    print ()
    time.sleep (3)
    print ("''I can’t afford to get all the locks replaced, and the nearest smithy that’s good enough to make them is twenty miles south of here anyway.'' " )
    print()
    time.sleep(3)
    print ("You agree to his offer, while you are tired from your travels you’ve never turned down an offer to an open bar. You put your pack of gear back on and head out to find some more information. ")
    print ()
    time.sleep (3)
    print ("You ask around town and some people tell you that the thieves are nasty little faeries from the forest. They are said to like shiny things and have been known to even steal teeth from locals in their sleep.  ")
    print ()
    time.sleep (3)
    print ("You aren’t sure how much you believe, as the locals seem quite superstitious. ")
    print ()
    time.sleep (3)
    print ("But you adventure out into the local forest to have a look around, and soon you see resting on a flower is a small humanoid form with pallid white skin, long black hair and dragon fly wings sprouting from its back. ")
    print ()
    time.sleep (3)
    print ("Instead of legs it seems to have the lower half of a wasp, four insect like legs and a black and yellow thorax ending in an inch-long sting that looks like it might be venomous. ")
    print ()
    time.sleep (3)
    print ("The faerie is laying next to a small golden brooch. It notices you quickly, picks up the broach and takes to the air. ")
    print()
    time.sleep(3)
    print ("You chase it for about two minutes and it goes to a clearing, the sun shines through the forest canopy and in the very centre is a ring of mushrooms and moss, growing in strange patterns almost like a mandala. ")
    print()
    time.sleep(3)
    print ("You watch as the faerie lands in the centre of the ring and disappears. You decide to try and follow it, as you step into the fae circle you feel light headed and your surroundings disappear. ")
    print()
    time.sleep(1)
    print ("Your stomach twists and you black out for a moment.")
    print()
    time.sleep(4)
    print ("You catch your balance and your brain fog clears. You see that you are standing in a strange room. ")
    time.sleep(2)
    print ()
    print ("The walls seem to be created from tree roots and branches, twisted together by wild magic to create some sort of structure. Being trapped inside it, you can only guess at the size or purpose. ")
    print ()
    time.sleep(1)
    room_1(hp)
    
hp = 20    
play_game()

