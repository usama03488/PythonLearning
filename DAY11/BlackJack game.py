import random
def Assign_card():
    Cars_Numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'Ace']
    #card = Cars_Numbers[random.randint(0, 13)]
    #OR
    card=random.choice(Cars_Numbers)
    #val = Cars_score[Cars_Numbers[card]]
    return card

def calculate_score(cards,card_scores):
    score=0
    for card in cards:
       #print(f"card is {type(card)}")
       value=str(card)
       score +=card_scores[value]

    return score
def Check_result(playerscore,dealerscore):
    if(playerscore<21 and playerscore<dealerscore):
        return False
    elif(playerscore<21 and playerscore>dealerscore):
        return True
    elif(playerscore ==21 and playerscore>dealerscore):
        return True
    else:
        return False
def Player_Turn():
    step = input("Enter Y to get a card and N to hold")
    if (step == 'Y'):
        card3 = Assign_card()
        return card3
    else:
        print("you are not gettin any card")
        return
def Dealer_Turn():
    value=0
    if (value == 0):
        card3 = Assign_card()
        return card3
    else:
        print("Dealer is not getting any card")

Cards_score= {'1':1,
             '2':2,
             '3':3,
             '4':4,
             '5':5,
             '6':6,
             '7':7,
             '8':8,
             '9':9,
             '10':10,
             'J':10,
             'Q':10,
             'K':10,
             'Ace':10}

Holding_cards=[]
Holding_cards.append(Assign_card())
Holding_cards.append(Assign_card())

Dealer_card=[]
Dealer_card.append(Assign_card())
Dealer_card.append(Assign_card())
print(f"print card calues {Holding_cards[0]} and {Holding_cards[1]}")
Player_score=calculate_score(Holding_cards,Cards_score)
print(f"your score is {Player_score}")
print(f" dealer card is {Dealer_card[0]}")
card3=Player_Turn()
Holding_cards.append(card3)
Player_score=calculate_score(Holding_cards,Cards_score)
if(dealer_Score!=0 and dealer_score<17):
    dealer_card3 = Dealer_Turn()

if(dealer_card3 != None):
    Dealer_card.append(dealer_card3)

dealer_score=calculate_score(Dealer_card,Cards_score)
status=Check_result(Player_score,dealer_score)
if(status):
    print(f"Player win with: {Player_score} scores  \n Dealer score was {dealer_score}")
else:
    print(f"Dealer win with {dealer_score} score")
#now it is a bot turn
#card3=( player_Turn())
