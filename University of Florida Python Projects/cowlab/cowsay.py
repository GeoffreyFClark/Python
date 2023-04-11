import sys
from heifer_generator import HeiferGenerator
from cow import * 
from dragon import *
from ice_dragon import *


def main():
    cow_objects = HeiferGenerator.get_cows()
    if len(sys.argv) == 2 and sys.argv[1] == '-l':
        cow_names = [cow.get_name() for cow in cow_objects]
        print(f"Cows available: {' '.join(cow_names)}")
    elif len(sys.argv) > 3 and sys.argv[1] == '-n':
        cow_name = sys.argv[2]
        cow_object = next((cow for cow in cow_objects if cow.get_name() == cow_name), None)
        if isinstance(cow_object, Dragon) and not isinstance(cow_object, IceDragon):
            print(' '.join(sys.argv[3:]))
            print(cow_object.get_image())
            print("This dragon can breathe fire.")
        elif isinstance(cow_object, IceDragon):
            print(' '.join(sys.argv[3:]))
            print(cow_object.get_image())
            print("This dragon cannot breathe fire.")
        elif cow_object is not None:
            cow_message = ' '.join(sys.argv[3:])
            print(cow_message)
            print(cow_object.get_image())
        else:
            print(f"Could not find {cow_name} cow!")
    else:
        cow_message = ' '.join(sys.argv[1:])
        print(cow_message)
        print(cow_objects[0].get_image())


if __name__ == '__main__':
    main()
