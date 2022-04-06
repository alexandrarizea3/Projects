print("Welcome to my computer quiz!")
playing = input("Do you want to play? ") #we leave a space to allow typing
if playing.lower() != "yes": # .lower takes the string and makes all letters lower
    quit() #is used to exit a python program
print("Okay! Let's Play :)")
score = 0
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1  #increase the score if it's corect
else:
    print("Incorrect")
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect")
print("You got " + str(score) + " questions correct")
print("You got " + str((score / 3) * 100) + "%")
