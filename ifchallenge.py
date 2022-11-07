name = input("What is your name? ")
age = int(input("Hi {}, how old are you? ".format(name)))

if 18 <= age <= 30:
    print("Welcome to the Holiday trip, {}!".format(name))
else:
    print("Sorry, you must be aged 18-30 for this Holiday trip.")

