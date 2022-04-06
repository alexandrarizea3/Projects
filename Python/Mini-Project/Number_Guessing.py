import random #This module implements pseudo-random number generators for various distributions

top_of_range = input("Type a number: ")
if top_of_range.isdigit(): #if it's a number (1,2,3...): true if it's a number
    # "25" -> 25 : int("25") => 25
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0, top_of_range) #if we add int after rand it can include 50
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue #brings as back to the very top of the loop
    if user_guess == random_number:
        print("You got it!")
        break
    else:
        if user_guess > random_number:
            print("You were above the number!")
        else:
            print("You were below the number!")
print("You got it in " + str(guesses) + " guesses")