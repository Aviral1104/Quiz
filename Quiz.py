print("Welcome to my computer Quiz!!")

score= 0

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("Chal hatt!!")
    quit()
else: 
    print("Okay!! Let's play :)")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    score= score + 1
    print("Correct!")
    print("score->", score)
else:
    print("Incorrect......(bruhh, itna nahi pataa)")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    score= score +1
    print("Correct!")
    print("score->", score)
else:
    print("Incorrect......(bruhh, itna nahi pataa)")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    score= score +1
    print("Correct!")
    print("score->", score)
else:
    print("Incorrect......(bruhh, itna nahi pataa)")

answer = input("What does ROM stand for? ")
if answer.lower() == "read only memory":
    score= score +1
    print("Correct!")
    print("score->", score)
else:
    print("Incorrect......(bruhh, itna nahi pataa)")

answer = input("What does HTTP stand for? ")
if answer.lower() == "hyper text transfer protocol":
    score= score +1
    print("Correct!")
    print("score->", score)
    print("total score->", score, "/ 5")
else:
    print("Incorrect......(bruhh, itna nahi pataa)")
    print("total score", score, " / 5")
