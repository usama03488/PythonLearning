#Step1- First I will make a dictionary of data including some popular place,persons
#Step 2-  import that dictionary here and try to select a random index from it
from Game_Data import higher_lower_data
import random
# Step 3- Make a function who select item randomly from dictionary

def Select_random_number():
    index = random.randint(0, len(higher_lower_data))
    return index

print("Welcome to higher-lower number game")
item1 =higher_lower_data[Select_random_number()]
item1_name=item1["name"]
item1_follower=item1["followers"]
print(f"Compare1 {item1_name} and his followers are {item1_follower} ")