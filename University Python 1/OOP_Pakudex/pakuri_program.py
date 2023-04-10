import pakudex as pakudex_module


def menu_options(opt, pakudex_object):
    if opt == "1":
        if pakudex_object.get_size() == 0:
            print("No Pakuri in Pakudex yet!\n")
            return
        else:
            print("Pakuri In Pakudex:")
            for i in range(pakudex_object.get_size()):
                print(f"{i+1}. {pakudex_object.get_species_array()[i]}")
                print("")
            return
    elif opt == "2":
        name = input("Enter the name of the species to display: ")
        species_list = pakudex_object.get_species_array()
        if species_list is None or name not in species_list:
            print("Error: No such Pakuri!\n")
            return
        elif name in species_list:
            print("")
            print(f"Species: {name}")
            attack, defense, speed = pakudex_object.get_stats(name)
            print(f"Attack: {attack}")
            print(f"Defense: {defense}")
            print(f"Speed: {speed}\n")
            return
    elif opt == "3":
        if len(pakudex_object.pakuri) >= pakudex_object.capacity:
            print("Error: Pakudex is full!\n")
            return
        name = input("Enter the name of the species to add: ")
        add_status = pakudex_object.add_pakuri(name)
        if add_status:  # if add_status returns True
            print(f"Pakuri species {name} successfully added!\n")
        elif add_status is False:
                print("Error: Pakudex already contains this species!\n")
        return
    elif opt == "4":
        name = input("Enter the name of the species to evolve: ")
        if name in pakudex_object.get_species_array():
            status = pakudex_object.evolve_species(name)
            if status:
                print(f"{name} has evolved!\n")
        else:
            print("Error: No such Pakuri!\n")
    elif opt == "5":
        pakudex_object.sort_pakuri()
        print("Pakuri have been sorted!\n")
    elif opt == "6":
        print("Thanks for using Pakudex! Bye!")
        return False
    else:
        print("Unrecognized menu selection!\n")
        return


def menu():
    print("Pakudex Main Menu\n"
          "-----------------\n"
          "1. List Pakuri\n"
          "2. Show Pakuri\n"
          "3. Add Pakuri\n"
          "4. Evolve Pakuri\n"
          "5. Sort Pakuri\n"
          "6. Exit\n")
    choice = input("What would you like to do? ")
    return choice


def main():
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    while True:
        max_capacity = input("Enter max capacity of the Pakudex: ")
        try:
            max_capacity = int(max_capacity)
        except:
            print("Please enter a valid size.")
            continue
        if isinstance(max_capacity, int) and max_capacity > 0:
            pakudex_object = pakudex_module.Pakudex(max_capacity)
            break
        else:
            print("Please enter a valid size.")

    a = True
    while a is not False:
        a = menu_options(menu(), pakudex_object)


if __name__ == "__main__":
    main()
