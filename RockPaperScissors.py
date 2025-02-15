import random
Moves=["Rock","Paper","Scossors"]

Player_Move=int(input("Enter you move from 1 to 3 \n 1- Rock \n 2- Paper \n 3-Scissor \n"))
if(Player_Move>=0 and Player_Move<3):
    Computer_Move = random.randrange(0, 3)
    print(f"computer moves was {Computer_Move}")
    if Computer_Move != Player_Move:
        if ((Computer_Move == 0 and Player_Move == 1) or
                (Computer_Move == 1 and Player_Move == 2) or
                (Computer_Move == 2 and Player_Move == 0)):
             print("you win")
        else:
             print("you lose")
    else:
        print("Its a tie")
       #print("You Selected you move")









