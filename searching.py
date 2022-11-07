shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "albatross"
found_at = None

for index in range(len(shopping_list)):
    # print(index)
    if shopping_list[index] == item_to_find:
        found_at = index
        break

if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found.".format(item_to_find))

# for index in shopping_list:
#     print(index)
#
# for index in range(10):
#     print(index)

# potato = len("1234567")
# print(potato)
# print(type(potato))

# print(item_to_find[::-1])

# xyz = "pam" in item_to_find
# print(xyz)