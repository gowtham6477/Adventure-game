
from dicts.weapons_skills import *
from dicts.rooms import *
from dicts.utils import *
from dicts.monsters import give_monster
import combat, dungeon, sys

def main():
    sys.path.append(os.getcwd())
    set_console_size()
    me = Player('Bori', 10, WEAPONS[BOW])
    enemies = [give_monster('wolf') for i in range(3)]
    world = dungeon.Dungeon(me, ROOMS)
    world.cmdloop()

if __name__ == '__main__':
    main()  

