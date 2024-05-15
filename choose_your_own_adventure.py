name=input("Player type your name: ")
print("Welcome",name,"on this adventure!")
print("-----------------------------------------")
answer=input("In front of you there are two roads one leads to the DEEP FOREST and the other leads to DESERT,which one will you choose? ").lower()

if answer == "deep forest":
    print("------------------------------------------------------------------")
    print("You come to a river,as ",name,"advanced forward to cross it,a crocodile plunged out of the river in front of you")
    answer=input("What will you do FIGHT or RUN? ").lower()
    if answer == "fight":
        print("------------------------------------------------------------------")
        print(name,"took out sword and swung it at the monster.The crocodile swiftly dodged and again plunged at",name)
        answer=input("Would you ATTACK or DODGE? ").lower()
        if answer == "attack":
            print("------------------------------------------------------------------")
            print(name,"created a fireball and blew the monster away!")
            print("After defeating the crocodile monster",name,"found two treasure chest,GOLD and SILVER")
            answer=input("which one will you choose? ").lower()
            if answer == "gold":
                print("------------------------------------------------------------------")
                print("On opening the golden chest,a portal opened from it and the monsters came out destroying everything")
                print("Player Lost")
                print("GAME OVER!")
                print("-----------------------------------------------------------------")
                quit() 
                
            elif answer == "silver":
                print("------------------------------------------------------------------")
                print("On opening the silver chest",name,"found various treasures!")
                print("Congratulations!",name,"Won!")
                print("*****************************************************************")
                quit()    
        elif answer == "dodge":
            print("------------------------------------------------------------------")
            print(name,"took out his shield and blocked the attack!")
            print("using his sword",name,"again attacked the crocodile monster and defeated it! ")
            print("Being defeated the monster left the river forever never to return.")
            print("The village was safe and sound the tyranny of the river monster had come to its end.")
            print("Congratulations!",name,"Won!")
            print("*****************************************************************")
            quit() 

        else:
            print("Not a valid option.You Lose")        
    elif answer == "run":
        print("------------------------------------------------------------------")
        print("You attempted to run, the crocodile was fast and caught",name)
        print("Player Lost")
        print("GAME OVER!")
        print("-----------------------------------------------------------------")
        quit() 
    else:
         print("Not a valid option.You Lose")
         quit()      
elif answer == "desert":
    print("------------------------------------------------------------------")
    print(name,"woke up in a parching desert,there was all only sand around",name,"saw an oasis ahead")
    answer=input("would you GO to it or Ignore it? ").lower()
    if answer == "go":
        print("------------------------------------------------------------------")
        print("You headed towards the oasis but suddenly the ground beneath you rumbled and a giant worm emerged! ")
        answer=input("Will you FIGHT or RUN? ").lower()
        if answer == "fight":
            print("------------------------------------------------------------------")
            print("The Worm monster overpowered",name,)
            print("Player Lost")
            print("GAME OVER!")
            print("-----------------------------------------------------------------")
            quit()
        elif answer == "run":
            print("------------------------------------------------------------------")
            print(name,"tried to run away but the giant worm caught",name)
            print("Player Lost")
            print("GAME OVER!")
            print("-----------------------------------------------------------------")
            quit()
    elif answer == "ignore":
        print("------------------------------------------------------------------")
        print(name,"ignored the oasis it was just a mirage")
        print("on going further",name,"met a group of desert travellers they took",name,"along to there destination.")
        print(name,"reached the town met his friends,they all celebrated the hero's return,the night sky of the desert sparkled with fireworks!")
        print("Congratulations!",name,"Won!")
        print("*****************************************************************")
        quit()
    else:
       print("Not a valid option.You Lose")
       quit()                    
else:
    print("Not a valid option.You Lose")
    quit()        