
def life_in_weeks(Current_age):
    Weeks_Left = (90 - int(Current_age))*52

    print(f"you have {Weeks_Left} weeks left")


get_age = input("Enter you age \n")
if int(get_age) <= 90 and int(get_age) > 0:
    life_in_weeks(get_age)