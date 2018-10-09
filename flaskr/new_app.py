import HandleName

from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
from pymongo import MongoClient

app = Flask(__name__)
app.debug = True

client = MongoClient('localhost', 27017)
db = client.APP_USERS


op = None


@app.before_first_request
def setupconnection():
    users = db.userlogindata.find()
    data = 'Name of Users:'
    creds = {}
    for user in users:
        data = data + user['username']
        creds = {"username": user['username'], "password": user['password']}
    global op
    op = creds
    return data


@app.route("/")
@app.route("/redirect")
@app.route("/redirect/login")
def index():
    return render_template("login.html", title='templates')
    # return op['username'] + "----" + op['password']


@app.route("/*/params", methods=['GET'])
def dosomething():
    abc = request.args.get('name', None)
    defe = request.args.get('place', None)
    return render_template('test.html', **locals())


@app.route("/hello/<string:name>/")
def hello(name):
    vals = HandleName.hellothere(name=name)
    vals['name'] = name
    print("printed something below \n" + vals['quote'] + "----" + vals['xyz'] + "----" + vals['name'])
    #   return render_template('test.html', name=name)
    return render_template('test.html', **locals())


@app.route("/redirect/userhome", methods=['GET', 'POST'])
def formaction():
    username = request.form.get('username')
    password = request.form.get('password')
    try:
        userdetail = db.userlogindata.find_one({"username": username})
        print("value for user details ---- ", userdetail)
        print(userdetail['username'] + "----" + userdetail['password'])
    except Exception as e:
        userdetail = None

    if (userdetail is not None and
            username == userdetail['username'] and
            password == userdetail['password']):
        print("username is ", username)
        return render_template('homepage.html', title="templates", **locals())
    else:
        errormessage = "Invalid username and password"
        return render_template('login.html', title="templates", **locals())


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80)

