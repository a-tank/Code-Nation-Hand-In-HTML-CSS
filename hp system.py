#place these at the top of code

import random

hit_points = 20
d4_damage = random.randint(1, 4)
d6_damage = random.randint(1, 6)
d8_damage = random.randint(1, 8)

def dead_check():
    if hit_points < 1:
        return (char_death())
    else:
        return (' ')

#use this for small damage recieved

def hp_loss_small(hit_points):
    return hit_points - d4_damage
print ("That stung, your HP is now: ")
print (hp_loss_small(hit_points))
hit_points = hp_loss_small(hit_points)
print (dead_check())

#use this for medium damage recieved

def hp_loss_medium(hit_points):
    return hit_points - d6_damage
print ("That hurt, your HP is now: ")
print (hp_loss_medium(hit_points))
hit_points = hp_loss_medium(hit_points)
print (dead_check())

#use this for large damage recieved

def hp_loss_large(hit_points):
    return hit_points - d8_damage
print ("That really hurt, your HP is now: ")
print (hp_loss_large(hit_points))
hit_points = hp_loss_large(hit_points)
print (dead_check())

   
