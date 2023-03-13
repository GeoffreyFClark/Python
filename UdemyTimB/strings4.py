#         012345678901234
parrot = "Norwegian Blue"
ABCs = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(ABCs[3:10])
print(ABCs[3:10:2])

number = "123456789012345678901234567890"
print(number[0:30:2])
print(number[0:30:3])
Every3rdNumber = number[0:99999:3]
print(Every3rdNumber)

number12345 = 12345
converted_number = str(number12345)
print(type(converted_number))
print(converted_number[::-1])
int(number12345)