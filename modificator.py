import wrap


wrap.world.create_world(400, 600)
mario=wrap.sprite.add("mario-1-big",50,550,"stand")
tank1=wrap.sprite.add("battle_city_tanks",200,100,"tank_enemy_size1_green1")
pric = wrap.sprite.add("pacman", 300, 200, "player2")



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
    angle(pric, pos_x, pos_y, key)








