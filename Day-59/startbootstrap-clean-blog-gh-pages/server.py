from flask import Flask
from flask import render_template
import requests
app=Flask(__name__)

@app.route("/")
def get_all_posts():
    return getData()
listdata=None    
@app.route("/about")
def EnableAbout():
    return  render_template("about.html")
@app.route("/contact")
def Enbalecontact():
    return  render_template("contact.html")
@app.route("/post/<int:id>")
def ShowPost(id):
    url="https://api.npoint.io/7eef2dcb226e06313c6d"
    data=requests.get(url)
    listdata=data.json()
    for item in listdata:
        if id==item['id']:
              return render_template("post.html",item=item)

  

def getData():
    url="https://api.npoint.io/7eef2dcb226e06313c6d"
    data=requests.get(url)
    listdata=data.json()
    return render_template("index.html",data=listdata)


if __name__=="__main__":
    app.run()