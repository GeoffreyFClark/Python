import random

usernum = 0
while usernum < 30 or usernum > 70:
    usernum = int(input("Please enter a number between 30 to 70: "))
    if usernum <30:
        print("Your number is too low.")
    elif usernum >70:
        print("Your number is too high.")

counter = 0
for i in range(100):
    if random.randint(0,101) < usernum:
        counter+=1

#RandomNumList = [(random.randint(0,101)) for i in range(100)]

# counter = 0
# for a in RandomNumList:
#     if a < usernum:
#         counter+=1

print("100 random numbers have been generated, ranging from 0 to 100. {} of them are greater than the number you input.".format(counter))
# print("\nThe list of random numbers is: {}".format(RandomNumList))