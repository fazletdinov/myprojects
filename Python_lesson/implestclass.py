from hero import Hero
# ========= main ========
myhero1 = Hero("bomjur", 5, "orc")
myhero2 = Hero("sharik", 10, "gnome")

myhero1.show_hero()
myhero1.level_up()
myhero1.move()
myhero2.show_hero()
myhero2.level_up()
myhero2.move()
myhero1.set_health(60)
myhero1.show_hero()