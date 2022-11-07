import copy

animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}

# Perform a shallow copy
things = animals.copy()

# Perform a deep copy
# things = copy.deepcopy(animals)

print(id(things["teddy"]), things["teddy"])
print(id(animals["teddy"]), animals["teddy"])

print()

things["teddy"].append("toy")
print(things["teddy"])
print(animals["teddy"])
