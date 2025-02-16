from os import system
from Logo import logo

def take_data():
    Name = input("What is your name?")
    bid_amount = int(input("enter your bid amount : $"))
    Auction_Dic[Name]=int(bid_amount)
    Iscompleted = input("Write 'yes' if there is any bidder remaining, and 'no' if there is not")
    check_status(Iscompleted)

def Find_Winner():
    maxamount=0
    person_name=""
    for key in Auction_Dic:
        if(maxamount<Auction_Dic[key]):
            maxamount=Auction_Dic[key]
            person_name=key
    print(f"Bid winner is {person_name} with the amount of {maxamount}")


def check_status(status):
    if status=="yes":
        print("\n"*30)
        #system("cls")
        take_data()
    else:
        Find_Winner()

Auction_Dic={}
print("Welcome to blind auction event")
print(logo)
take_data()