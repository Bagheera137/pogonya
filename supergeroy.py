import wrap

wrap.world.create_world(400, 600)
mario=wrap.sprite.add("mario-1-big",50,550,"stand")

@wrap.on_key_always(wrap.K_RIGHT,wrap.K_LEFT)
def move(keys):

    if wrap.K_RIGHT in keys:
        wrap.sprite.move(mario,10,0)
        wrap.sprite.set_reverse_x(mario,False)
        if wrap.sprite.get_right(mario)>400:
            wrap.sprite.move_right_to(mario,400)
    else:
        wrap.sprite.move(mario,-10,0)
        wrap.sprite.set_reverse_x(mario,True)
        if wrap.sprite.get_left(mario)<0:
            wrap.sprite.move_left_to(mario,0)
@wrap.on_key_down(wrap.K_SPACE)
def fly():
    wrap.sprite.set_costume(mario,"swim6")

@wrap.always
def move(pos_x,pos_y):
    wrap.sprite.move_at_angle_point(mario,pos_x,pos_y,10)
