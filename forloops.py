parrot = "Norwegian Blue"

for character in parrot:
    print(character)



number = "9,223;372:036 854,775;807"
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)



quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

Uppercaseletters = ""

for character in quote:
    if character.isupper():
        Uppercaseletters = Uppercaseletters + character

print(Uppercaseletters)