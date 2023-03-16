numbers = [1, 45, 32, 12, 60]

for number in numbers:
    if number % 8 == 0:
        #reject list
        print("The numbers are unacceptable.")
        break
else:
    print("All those numbers are fine.")

    # elif number % 8 != 0:
    #     print("The number is acceptable")