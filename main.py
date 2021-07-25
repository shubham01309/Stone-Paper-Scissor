import random


attempts = 0

while (attempts<=10):

    lst = ["Stone","Paper","Sessior"]
    x = random.choice(lst)

    print("enter your choice Stone or Paper or Sessior")
    your_choice = input()

    print(your_choice + "=" + x)

    if your_choice == "Sessior" and x =="Stone":
        print("computer wins")
        
    elif your_choice == "Sessior" and x =="Paper":
        print("you wins")
        
    elif your_choice == "Sessior" and x =="Sessior":
        print("draw!!!")
        

    if your_choice == "Stone" and x =="Paper":
        print("computer wins")
       
    elif your_choice == "Stone" and x =="Sessior":
        print("you wins")
        
    elif your_choice == "Stone" and x =="Stone":
        print("draw!!!")
      

    if your_choice == "Paper" and x =="Sessior":
        print("computer wins")
       
    elif your_choice == "Paper" and x =="Stone":
        print("you wins")
        
    elif your_choice == "Paper" and x =="Paper":
        print("draw!!!")
        
    else:
        print("invalid input")
        continue

    print("\nNo. of guesses left: {}".format(10 - attempts))
    attempts = attempts + 1

    if attempts>10:
        print("game over")
    
        