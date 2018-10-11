from random import randint


def hellothere( name):
    quotes = ["'If people do not believe that mathematics is simple, it is only because "
              "they do not realize how complicated life is.' -- John Louis von Neumann ",
               "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
               "'To understand recursion you must first understand recursion..' -- Unknown",
               "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
               "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
               "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"  ]
    randomnumber = randint(0, len(quotes)-1)
    name = name + "\t see this also works"
    vals = {"quote": quotes[randomnumber],
            "xyz": name}

    #   return render_template('test.html', name=name)
    #   return render_template('test.html', **locals())
    return vals


def userAuthentication(db, request):
    username = request.form.get('username')
    password = request.form.get('password')
    try:
        userdetail = db.userlogindata.find_one({"username": username})
        print("value for user details ---- ", userdetail)
        print(userdetail['username'] + "----" + userdetail['password'])
    except Exception as e:
        userdetail = None
        print("Authentication failed ---- ", e)

    if (userdetail is not None and
            username == userdetail['username'] and
            password == userdetail['password']):
        userAuthToken = "pass"
    else:
        userAuthToken = "fail"

    return userAuthToken

def userRegistration(db, request):
    username = request.form.get('username')
    password = request.form.get('password')
    confirmPassword = request.form.get('confirm_password')
    userdetail = db.userlogindata.find_one({"username": username})
    if userdetail is not None:
        status = "Existing"
    else:
        if password != confirmPassword:
            status = "Error"
        else:
            db.userlogindata.insert_one({"username": username, "password": password})
            status = "New"
    return status
