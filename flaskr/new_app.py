import HandleName

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def index():
    return "Flask App!"


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


@app.route("/testform/")
def formtest():
    return render_template('testform.html', title="templates")


@app.route("/testform/params", methods=['GET', 'POST'])
def formaction():
    username = request.form.get('username')
    password = request.form.get('password')

    return render_template('homepage.html', title="templates", **locals())


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80)


