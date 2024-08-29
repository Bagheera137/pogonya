import wrap

wrap.world.create_world(500,500)
pacman=wrap.sprite.add("pacman", 300,200,"player2")
blue=wrap.sprite.add("pacman",100,400,"enemy_ill_blue1",False)


@wrap.on_key_down(wrap.K_RIGHT,wrap.K_LEFT)
def sdvig(key):
    if key == wrap.K_RIGHT:
        a=wrap.sprite.get_angle(pacman)
        wrap.sprite.set_angle(pacman,a+20)
    else:
        a = wrap.sprite.get_angle(pacman)
        wrap.sprite.set_angle(pacman, a-20)


@wrap.on_key_always(wrap.K_UP)
def sdvig():
    wrap.sprite.move_at_angle_dir(pacman,20)
@wrap.on_mouse_move
def move(pos_x,pos_y):
    wrap.sprite.move_to(blue,pos_x,pos_y)
@wrap.on_mouse_down
def click():
    wrap.sprite.show(blue)
@wrap.on_mouse_up
def click():
    wrap.sprite.hide(blue)

@wrap.always(20)
def always():
    a=wrap.sprite.is_visible(blue)
    if a==True:
        bx = wrap.sprite.get_x(blue)
        by = wrap.sprite.get_y(blue)
        wrap.sprite.set_angle_to_point(pacman, bx, by)
        wrap.sprite.move_at_angle_dir(pacman,3)



