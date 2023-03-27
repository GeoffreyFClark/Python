import sys
from heifer_generator import HeiferGenerator
from cow import Cow

# TODO: Add dragon and ice-dragon classes

def main():
    cow_objects = HeiferGenerator.get_cows()
    if len(sys.argv) == 2 and sys.argv[1] == '-l':
        cow_names = [cow.get_name() for cow in cow_objects]
        print(f"Cows available: {' '.join(cow_names)}")
    elif len(sys.argv) > 3 and sys.argv[1] == '-n':
        cow_name = sys.argv[2]
        cow_image = next((cow.get_image() for cow in cow_objects if cow.get_name() == cow_name), None)
        if cow_image is not None:
            cow_message = ' '.join(sys.argv[3:])
            print(cow_message)
            print(cow_image)
        else:
            print(f"Could not find {cow_name} cow!")

    else:
        cow_message = ' '.join(sys.argv[1:])
        print(cow_message)
        print(cow_objects[0].get_image())


if __name__ == '__main__':
    main()
