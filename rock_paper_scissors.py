import random
user_wins=0
computer_wins=0
options=["rock","paper","scissors"]
game_time=0
while True: 
    ask_user=input("rock,paper,scissors or Q to quit :  ")
    if ask_user=="q":
        break
    if ask_user not in options:
        continue #we do continue because we just want to take what's we were asking for. and the program will ask each time till the users give the right input like rock or another options 
    random_number=random.randint(0,2)
    #rock:0,paper:1,scissors:2
    computer_pick=options[random_number]
    print("Computer picked",computer_pick+ ".")
   
    if ask_user=="rock" and computer_pick=="scissors"or ask_user=="paper" and computer_pick=="rock"or ask_user=="scissors" and computer_pick=="paper":
        print("You won")        
        user_wins+=1
        game_time+=1
        continue
    elif ask_user=="rock" and computer_pick=="rock"or ask_user=="paper" and computer_pick=="paper" or ask_user=="scissors" and computer_pick=="scissors":
     print("Equal!Nobody wins")
     computer_wins+=0 
     user_wins+=0
     game_time+=1
     print("You won ",user_wins,"times")
     print("Computer wins",computer_wins,"times")
     continue
    else:
        print("computer won")
        computer_wins+=1
        game_time+=1
    
    print("You won ",user_wins,"times")
    print("Computer wins",computer_wins,"times")
        
        

    
