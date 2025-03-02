#Step1- First I will make a dictionary of data including some popular place,persons
#Step 2-  import that dictionary here and try to select a random index from it
from Game_Data import higher_lower_data
import random
# Step 3- Make a function who select item randomly from dictionary

def Select_random_number():
    index = random.randint(0, len(higher_lower_data)-1)
    print(f"index of data point {index}")
    return index

def GetPlayer_input():
    Input_option= input("Guess which one have more followers \n Enter 'A' for first item and 'B' fro second item")
    Input_option=Input_option.lower()
    print(f"input: {Input_option}")
    if(Input_option not in ["a", "b"]):
        print("You enter wrong input try again: You loose" )
    else:
        print("you enter right entry")
        return Input_option

def Check_PlayerInput(input,item1, item2):
    if(input=='a'):
        if(item1["followers"]>item2["followers"]):
            print("you have selected the correct item1")
            return item1
        else:
            return False
    else:
        if (item1["followers"] < item2["followers"]):
            print("you have selected the correct item2")
            return item2
        else:
            return False
        #we will check if item1 have more followers than second or not
def Display_messages(item1,item2):
    print(f"  Guess who have more followers  ")
    print(f"  {item1["name"]} vs {item2["name"]}")

score=0
print("Welcome to higher-lower number game")
item1 =higher_lower_data[Select_random_number()]
# we will get two items to compare for the first time
item2 =higher_lower_data[Select_random_number()]
iswronged=False
while(iswronged ==False):
    Display_messages(item1, item2)
    player_input = GetPlayer_input()
    status = Check_PlayerInput(player_input, item1, item2)
    if not isinstance(status, bool):
        print("it is a list so it means you have pridicted the correct option")
        score += 1
        item1 = status
        item2 = higher_lower_data[Select_random_number()]
    else:
        print("You have guessed it wrong \n **************GAME END*****************")
        iswronged = True




#take user input to guess which one have more followers
# Check player input that if it is wrong or right
#if it is right we will get one more item and compare with the previous item which was right
#this process will be going till player give a wrong answere