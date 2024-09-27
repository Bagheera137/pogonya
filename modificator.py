import wrap


wrap.world.create_world(400, 600)
mario=wrap.sprite.add("mario-1-big",200,100,"stand")
tank1=wrap.sprite.add("battle_city_tanks",200,100,"tank_enemy_size1_green1")
pric = wrap.sprite.add("pacman", 200, 100, "player2")



def smena_costume(name,x,y,key):
    a = wrap.sprite.is_collide_point(name,x,y)
    if key==wrap.K_UP and a==True:
        wrap.sprite.set_costume_next(name)
    if key==wrap.K_DOWN and a==True:
        wrap.sprite.set_costume_prev(name)

def angle(name,x,y,key):
    a = wrap.sprite.is_collide_point(name, x, y)
    if key==wrap.K_RIGHT and a==True:
        ma=wrap.sprite.get_angle(name)
        wrap.sprite.set_angle(name,ma+10)
    if key==wrap.K_LEFT and a==True:
        ma=wrap.sprite.get_angle(name)
        wrap.sprite.set_angle(name, ma-10)



@wrap.on_key_down(wrap.K_DOWN,wrap.K_UP,wrap.K_RIGHT,wrap.K_LEFT)
def costum(key,pos_x,pos_y):
    smena_costume(tank1,pos_x,pos_y,key)
    smena_costume(mario,pos_x,pos_y,key)
    smena_costume(pric, pos_x, pos_y, key)
    angle(mario,pos_x,pos_y,key)
    angle(tank1, pos_x, pos_y, key)
    angle(pric , pos_x, pos_y, key)


@wrap.on_mouse_down(wrap.BUTTON_WHEELUP,wrap.BUTTON_WHEELDOWN)
def size(button,pos_x,pos_y):


    UP=button == wrap.BUTTON_WHEELUP
    DOWN=button == wrap.BUTTON_WHEELDOWN

    if  wrap.sprite.is_collide_point(pric, pos_x, pos_y):
        pers=pric
    elif wrap.sprite.is_collide_point(tank1, pos_x, pos_y):
        pers=tank1
    elif wrap.sprite.is_collide_point(mario, pos_x, pos_y):
        pers = mario
    else:
        return
    number = 0
    if UP:
        number=10
    if DOWN:
        number=-10
    tw = wrap.sprite.get_width_percent(pers)
    th = wrap.sprite.get_height_percent(pers)
    wrap.sprite.set_size_percent(pers, tw + number, th + number)















