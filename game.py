import random
score = 0
for x in range(1,4):
    

        
        player_num =random.randint(1 , 100) 
        computer_num =random.randint(1 , 100)

        print(f"your number:{player_num}")
        print(f" computer number:{computer_num}")
        print(f"round {x}")

        guess=input("do you think your number is 'higher' or 'lower' than the computer's number?").lower()

       
        if player_num > computer_num:
            if guess=="higher":
                print("congrats! your guess is correct")
                score+=1
            else:
                print("wrong guess") 
        elif player_num < computer_num:
            if guess=="lower":
                print("congrats! your guess is correct")
                score+=1
            else:
                print("wrong guess")
        else:
            print(f"it's a tie! the computer wins in case of tie")
        
print(f"\n Game over! your final score is {score}")


