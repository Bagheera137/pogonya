import random

import wrap
a=1
wrap.world.create_world(400, 600)
tank1=wrap.sprite.add("battle_city_tanks",200,100,"tank_enemy_size1_green1")
pric = wrap.sprite.add("pacman", 300, 200, "player2",False)
wrap.sprite.set_size(pric,15,15)
wrap.sprite.set_angle(pric, 0)
@wrap.always(2000)
def always():
    wrap.sprite.move_to(tank1,random.randint(10,390),random.randint(10,590))

@wrap.on_mouse_down
def click(pos_x,pos_y):
    a=wrap.sprite.is_collide_point(tank1,pos_x,pos_y)
    if a==True:
        wrap.sprite.set_costume_next(tank1)

@wrap.on_mouse_move
def move(pos_x,pos_y):
    wrap.sprite.move_to(pric,pos_x,pos_y)
@wrap.on_key_down(wrap.K_UP)
def size():
    global a
    h=wrap.sprite.get_height(pric)
    w=wrap.sprite.get_width(pric)
    if a==1:
        wrap.sprite.show(pric)
    if a==2 or a==3:
        wrap.sprite.set_size(pric,h+20,w+20)
    if a==4:
        wrap.sprite.hide(pric)
        wrap.sprite.set_size(pric, 15, 15)
        a=0

    a = a + 1
    print(h,w)
