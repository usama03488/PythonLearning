from flask import Flask
app=Flask(__name__)
#this decorator will take input and send it to the function which will show the correct picture
def TakeInput(function):
    def wrapper(*args):
        return function(args[0])
    return wrapper

@app.route("/")
def PrintStatement():
    return "<h1>Guess a number between 0 and 9</h1>"

@app.route("/<int:index>")
def CheckInput(index):
    if index <6:
        return """
        <h1>Your value is very low</h1>
        <img src="https://i.giphy.com/YWB6Hi29vA3jG.gif">
        """
    elif index>6:
        #https://giphy.com/embed/9az09tlYyYNfq
        return """
        <h1>Your value is High</h1>
        <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExYnNoY3BrNWIyM2tidTMyMnBjNXp1MWVybGV0ZDAzYWQwNzllYXJqayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/9az09tlYyYNfq/giphy.gif">
        """
    else:
        return """
        <h1>You have the Right value</h1>
        <img src="https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3b3J1dzhjdXFkNGM4cXo3N3pieDU4cXU2MXd4NmFucWZxY3oxeGxnbSZlcD12MV9naWZzX3JlbGF0ZWQmY3Q9Zw/1qGaYAEAk7eOA/giphy.gif">
        """
