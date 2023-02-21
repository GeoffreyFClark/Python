from console_gfx import *


def option_menu():
    print("\n\nRLE Menu\n"
          "--------\n"
          "0. Exit\n"
          "1. Load File\n"
          "2. Load Test Image\n"
          "3. Read RLE String\n"
          "4. Read RLE Hex String\n"
          "5. Read Data Hex String\n"
          "6. Display Image\n"
          "7. Display RLE String\n"
          "8. Display Hex RLE Data\n"
          "9. Display Hex Flat Data\n")
    return int(input("Select a Menu Option: "))


def main():
    print("Welcome to the RLE image encoder!\n")
    print("Displaying Spectrum Image:")
    ConsoleGfx.display_image(ConsoleGfx.test_rainbow)

    option = 10
    image_data = []

    while option != 0:
        option = option_menu()
        if option == 0:
            pass
        elif option == 1:
            file_to_load = input("Enter name of file to load: ")
            image_data = ConsoleGfx.load_file(file_to_load)
        elif option == 2:
            image_data = ConsoleGfx.test_image
            print('Test image data loaded.')
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            pass
        elif option == 6:
            ConsoleGfx.display_image(image_data)
        elif option == 7:
            pass
        elif option == 8:
            pass
        elif option == 9:
            pass
        else:
            pass


main()