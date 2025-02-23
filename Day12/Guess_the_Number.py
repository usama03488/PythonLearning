from LogoArt import logo
import random
def get_GameMode():
    global GAME_MODE
    game_mode = input("Enter 'Easy' for easy mode or 'Hard' for hard mode").lower()
    if (game_mode == "easy"):
        GAME_MODE = 0
        tries = 10
        return tries
    else:
        GAME_MODE = 1
        tries = 5
        return tries
def set_GuessWord():
    global Guessing_number
    Guessing_number=random.randint(1,100)
def Get_GuessNumber():
    global Guessing_number
    guessed_number=input("Guess a number \n")
    guessed_number=int(guessed_number)
    if (guessed_number == Guessing_number):
        print("you win!!!")
    elif (Guessing_number-guessed_number>3):
        print("too low \n Try again")
        Guess_fail()
    elif(Guessing_number-guessed_number<-3):
        print("too high \n Try again")
        Guess_fail()
    else:
        print("close")
        Guess_fail()
def Guess_fail():
    global TRIES
    if (TRIES>1):
        TRIES -=1
        print(f"you have {TRIES} attempts left")
        Get_GuessNumber()
    else:
        print("you failed to guess the word")

Guessing_number=0
print(logo)
Game_MODE=-1
print("Welcome to number guessing game \n I am thinking of a number bwtween 1 to 100")
TRIES=get_GameMode()
print(f"You have {TRIES} to guess a number")
set_GuessWord()
Get_GuessNumber()
