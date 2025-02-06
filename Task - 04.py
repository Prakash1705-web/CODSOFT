import random

computer_selection = ["R","P","S"]

score = 0 

while True:
    computer_output = random.choice(computer_selection)
    user_selection = input("Enter your choice [ R / P / S ] : ")

    if user_selection == computer_output:
        print(f"Your Selection : {user_selection}")
        print(f"Computer Selection : {computer_output}")
        print("Result : Its a tie")
            
    elif user_selection == "R" and computer_output == "P":
        print(f"Your Selection : {user_selection}")
        print(f"Computer Selection : {computer_output}")
        print("Result : You lose")
        score -= 1
            
    elif user_selection == "R" and computer_output == "S":
        print(f"Your Selection : {user_selection}")
        print(f"Computer Selection : {computer_output}")
        print("Result : You win")
        score += 1
            
    elif user_selection == "P" and computer_output == "R":
        print(f"Your Selection : {user_selection}")
        print(f"Computer Selection : {computer_output}")
        print("Result : You win")
        score += 1
            
    elif user_selection == "P" and computer_output == "S":
        print(f"Your Selection : {user_selection}")
        print(f"Computer Selection : {computer_output}")
        print("Result : You lose")
        score -= 1
        
    elif user_selection == "S" and computer_output == "R":
        print(f"Your Selection : {user_selection}")
        print(f"Computer Selection : {computer_output}")
        print("Result : You lose")
        score -= 1
            
    elif user_selection == "S" and computer_output == "P":
        print(f"Your Selection : {user_selection}")
        print(f"Computer Selection : {computer_output}")
        print("Result : You win")
        score += 1 
            
    else:
        print("Invalid Input!")
            
    print(f"Your Score : {score}")
    print()
    ch = input("Do you want to play again [ Y / N ] : ")
    
    if ch == "N":
        break