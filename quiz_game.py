print("Welcome to my computer quiz!")

playing = input("Do you want to play? (yes/no) ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")

score = 0

answer = input("Are you a good person? ")
if answer.lower() == "yes":
    print("Okay, good!")
    score += 1
else:
    print("Yikes! You gotta be a good person :/") 

answer = input("Are you a hard-working? ")
if answer.lower() == "yes":
    print("Okay, good!")
    score += 1
else:
    print("Yikes! You gotta work hard :/") 

answer = input("Are you a good at communication? ")
if answer.lower() == "yes":
    print("Okay, good!")
    score += 1
else:
    print("Yikes! You gotta improve your communication skills :/") 

answer = input("What is the capital of India? ")
if answer.lower() == "Delhi":
    print("Okay, good!")
    score += 1
else:
    print("Bruh! Imporve your G.K. :/") 

answer = input("Who is the president of India? ")
if answer.lower() == "draupathi murmu":
    print("Okay, good!")
    score += 1
else:
    print("You have to update yourself man! :/") 

print(f"Your got {score} questions correct!")

print(f"Your got {(score/4) * 100}%")