from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    data=requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blogsdata=data.json()
    #for data in blogsdata:

    return render_template("index.html",data=blogsdata)

@app.route("/blog/<int:Id>")
def GetBlog(Id):
    print(f"selected blog id {Id}")
    data=requests.get("https://api.npoint.io/c790b4d5cab58020d391")

    blogsdata=data.json()
    post=None
    for data in blogsdata:
        if Id==data['id']:
            post=data

    return render_template("post.html",post=post,number=Id)


if __name__ == "__main__":
    app.run(debug=True)
