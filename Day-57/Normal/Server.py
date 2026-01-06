from flask import Flask
from flask import render_template
import random
import datetime
app=Flask(__name__)
# def GetFooter(function):
#     def wrapper():
        
#         return currentyear
#     return wrapper


@app.route("/")
def HellowORLD():
    randomvalue=random.randint(1,10)
    return  render_template("index.html",value=randomvalue,footerValue=GetFooter())

def GetFooter():
    currentyear=datetime.datetime.now().year
    return int(currentyear)

if __name__=="__main__":
    app.run()