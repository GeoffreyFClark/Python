shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]
another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))

print(another_list)
a = b = c = d = e = f = another_list
print(a)

print("Adding cream")
# shopping_list += ["cream"]
b.append("cream")
print(c)
print(d)

x = y = z = "abc"
y += "d"
print(x)
print(y)
print(id(x))
print(id(y))
print(id(z))