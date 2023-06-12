from flask import Flask, redirect, url_for, request,render_template

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'welcome %s'% name

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))
   

@app.route("/")
def hello_world():
    fopen=open("test123.txt","w")
    fopen.write("something")
    fopen.close()
    return render_template("index.html", title="Hello")
