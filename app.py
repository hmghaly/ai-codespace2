from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    fopen=open("test123.txt","w")
    fopen.write("something")
    fopen.close()
    return render_template("index.html", title="Hello")
