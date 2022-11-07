parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print("{0} is in {1}".format(letter, parrot))
else:
    print("I don't need that letter.")




activity = input("What would you like to do today? ")

if "cinema" not in activity.casefold():
    print("But I want to go to the cinema")
