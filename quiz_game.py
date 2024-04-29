print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    print("Have a nice day ")
    quit()

print("Okay! Lets Play :)")
print("**************************************")
score=0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Hooray! Correct Answer ")
    score +=1
else:
    print("Oops! Wrong Answer")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Hooray! Correct Answer ")
    score +=1
else:
    print("Oops! Wrong Answer")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Hooray! Correct Answer ")
    score +=1
else:
    print("Oops! Wrong Answer")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Hooray! Correct Answer ")
    score +=1
else:
    print("Oops! Wrong Answer")            

print ("You got " + str(score) + " questions correct!") 
print ("You got " + str((score/4) *100) + "%")     