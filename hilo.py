import math

low = 1
high = 1000

low1 = low
high1 = high

depvar = high - low
numguessesreq = math.ceil(math.log(depvar,2))

print("Please think of a number between {} and {}".format(low, high))
input("I will guess it within {} tries. Press ENTER to start! ".format(numguessesreq))

guess = 0

while True:
    guess = low + (high - low)//2
    response = input("""I guess {}. Is your number higher or lower? 
    If the guess is correct, type "correct". """
                     .format(guess)).casefold()
    if response == "higher":
        low = guess
    elif response == "lower":
        high = guess
    elif response == "correct":
        break
    else:
        print("That is not a valid response.")
print("Haha, got it! One can guess any number in range = 2^x"
      " where x rounded up to the nearest whole number equals the max number of required guesses."
      "\nFor example, the range of {} to {} is {}.".format(low1, high1, depvar))
print("{}=2^x makes x = log base 2 of {}, which rounded up, equals {}".format(depvar, depvar,numguessesreq))