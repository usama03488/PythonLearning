from flask import Flask
from flask import render_template
import random
import datetime
import requests
app=Flask(__name__)
# def GetFooter(function):
#     def wrapper():
        
#         return currentyear
#     return wrapper


@app.route("/")
def HellowORLD():
    randomvalue=random.randint(1,10)
    return  render_template("index.html",value=randomvalue,footerValue=GetFooter())


@app.route("/name/<username>")
def sendNameRequest(username):
    return SendApiRequest(username)
    


def GetFooter():
    currentyear=datetime.datetime.now().year
    return int(currentyear)


def SendApiRequest(name):
    data=requests.get(f"https://api.agify.io?name={name}")
    data.raise_for_status()
    jsondata=data.json()
    print(f"here is json data {jsondata}")
    return render_template("NameResult.html",username=jsondata['name'],Age=jsondata['age'])


@app.route("/blog/<num>")
def GetBlog(num):
    data=requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blogsdata=data.json()
    return render_template("Blog.html",post=blogsdata,number=num)


if __name__=="__main__":
    app.run()