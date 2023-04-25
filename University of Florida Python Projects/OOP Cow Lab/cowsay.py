import sys
from heifer_generator import HeiferGenerator
from cow import * 
from file_cow import *
from dragon import *
from ice_dragon import *


def main():
    cow_objects = HeiferGenerator.get_cows()
    filecow_objects = HeiferGenerator.get_file_cows()
    if len(sys.argv) == 2 and sys.argv[1] == '-l':
        cow_names = [cow.get_name() for cow in cow_objects]
        filecow_names = [filecow.get_name() for filecow in filecow_objects]
        print(f"Cows available: {' '.join(cow_names)}")
        print(f"File cows available: {' '.join(filecow_names)}")
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
    elif len(sys.argv) > 3 and sys.argv[1] == '-f':
        filecow_name = sys.argv[2]
        filecow_object = next((filecow for filecow in filecow_objects if filecow.get_name() == filecow_name), None)
        if isinstance(filecow_object, Dragon) and not isinstance(filecow_object, IceDragon):
            print(' '.join(sys.argv[3:]))
            print(filecow_object.get_image())
            print("This dragon can breathe fire.")
        elif isinstance(filecow_object, IceDragon):
            print(' '.join(sys.argv[3:]))
            print(filecow_object.get_image())
            print("This dragon cannot breathe fire.")
        elif filecow_object is not None:
            filecow_message = ' '.join(sys.argv[3:])
            print(filecow_message)
            print(filecow_object.get_image())
        else:
            print(f"Could not find {filecow_name} cow!")
    else:
        cow_message = ' '.join(sys.argv[1:])
        print(cow_message)
        print(cow_objects[0].get_image())


if __name__ == '__main__':
    main()
