# take words array and then I will pick random word after that i
import random
import Words_List
def take_Input():
    Entered_word=input(f"Enter word ")
    Search_word(Entered_word)


def Search_word(char):
    global guessed_chars
    for i in range(len(guessing_word)):  # Iterate using indices
        if char == guessing_word[i]:  # Corrected comparison syntax
            guess[i] = char
            guessed_chars +=1
            print(f"word guessed: {guess}")



    check_Gamestatus()
def check_Gamestatus():
    global tries,guessed_chars
    if guess==guessing_word:
        if guessed_chars==len(guessing_word):
            print("you won")
        else:

            take_Input()

    else:
        tries -= 1
        if tries==0:
            print("you loose")
        else:
            take_Input()



guessing_word=list(Words_List.word[random.randint(0,len(Words_List.word))])
guess=""
guess = list(guess)
guessed_chars=0
tries=12
for i in guessing_word:
    guess += "_"
take_Input()

