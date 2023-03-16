letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1] #Starts at 25 (z) and goes back 1 step at a time to 0 (a), and excludes a
print(backwards)

backwards2 = letters[25:-27:-1]
backwards3 = letters[25::-1]
print(backwards2)
print(backwards3)

print(letters[0:26])
print(letters[0:])
print(letters)
backwards4 = letters[9999::-1]
print(backwards4)

backwards5 = letters[::-1]
print(backwards5)

#create slice to produce "qpo" "edcba" and the last 8 chars in reverse order
qpo = letters[-10:-13:-1]
edcba = letters[4::-1]
last8rev = letters[:-9:-1]

print(qpo, edcba, last8rev)
print(letters[16:13:-1], letters[-22::-1], letters[:17:-1])

print(letters[-1:])