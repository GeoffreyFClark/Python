choice = "-"
while choice != "0":
    if choice in "12345":
        print("You've chosen option {}.".format(choice))
    else:
        print("Please choose your choice from the list below.\n")
        print("""\t\t1. Learn Python\n
        2. Learn Java\n
        3. Go Swimming\n
        4. Eat Dinner\n
        5. Go to Bed\n
        0. Exit""")
    choice = input("Please choose an option:")