available_parts = ["Computer",
                   "Monitor",
                   "Keyboard",
                   "Mouse",
                   "HDMI Cable",
                   "DVD Drive"
                   ]
valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
#for i in range(1, len(available_parts) + 1):
    #valid_choices.append(str(i))
# print(valid_choices)

current_choice = "-"
computer_parts = []  # create an empty list

while current_choice != "0":
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            computer_parts.remove(chosen_part)
            print("Removing {}".format(current_choice))
        else:
            computer_parts.append(chosen_part)
            print("Adding {}".format(current_choice))
        print("Your list now contains: {}".format(computer_parts))
    else:
        print("Please add options from the list below:")
        for number, part in enumerate(available_parts, 1):
            print("{0}: {1}".format(number, part))
    current_choice = input()

print(computer_parts)