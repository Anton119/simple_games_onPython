import random 

user_wins = 0
computer_wins = 0
tie = 0


options = ["rock", "paper", "scissors"]


while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ")
    if user_input.upper() == "Q":
        break
        
    if user_input not in options:
        #means go back and ask a user untill "rps" answer is recieved 
        continue
        
    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")
        
    if user_input == "rock" and computer_pick == "scissors":
        user_wins +=1
        print("You won!")
                   
    elif user_input == "paper" and computer_pick == "rock":
        user_wins +=1
        print("You won!")
                
    elif user_input == "scissors" and computer_pick == "paper":
        user_wins +=1
        print("You won!")
    
    elif user_input == "rock" and computer_pick == "rock":
        print("Tie!")
        tie +=1 
        
    elif user_input == "paper" and computer_pick == "paper":
        print("Tie!")
        tie +=1    
    
    elif user_input == "scissors" and computer_pick == "scissors":
        print("Tie!")
        tie +=1 
            
            
    else:
        print("You lost!")
        computer_wins +=1
        
        
print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.") 
print("Ties:", tie, "times")  
print("Goodbye!")            
        
        
              