from flask import Flask
#Creatinh bold, emphasis and underline tags decorators 
def MakeBold(function):
    def wrapper():
        text=function()
        updatedText= "<b>"+text+"</b>"
        return updatedText
    return wrapper
def MakeItalic(function):
    def wrapper():
        text=function()
        updated="<em>"+text+"</em>"
        return updated
    return wrapper
def MakeUnderLine(function):
    def wrapper():
        text=function()
        updated="<u>"+text+"</u>"
        return updated
    return wrapper

app=Flask(__name__)

@app.route("/")
@MakeBold
@MakeItalic
@MakeUnderLine
def PrintHello():
    return "Hello Babe"

@app.route("/bye")
def Bye():
    return "you are leave the site bye...."
    #print("you are leave the site bye....")
@app.route("/<username>")
def greet(username):
    return f"hello uou cutie {username}"

if(__name__=="__main__" ):
    app.run(debug=True) 

