from bson.objectid import ObjectId


def createSession(db, authtoken, username):
    try:
        db.usersessiondata.insert_one({"username": username, "usertoken": authtoken})
        print("Data inserted in usersessiondata")
    except Exception as e:
        print("Exception occurred while inserting in usersessiondata collection---- ", e)
    try:
        sessionDetails = db.usersessiondata.find_one({"usertoken":authtoken})
        print("session details---- ", sessionDetails)
    except Exception as e:
        print("Exception occurred while reading from usersessiondata collection---- ", e)
    return username + "--" + str(sessionDetails['_id'])


def checkValidSession(db, session):
    if session.get('userToken') is not None:
        token = ObjectId(str(session.get('userToken')).split('--')[1])
        print("token is---- ", str(session.get('userToken')).split('--')[1])
    else:
        token = None
    try:
        newsessionDetails = db.usersessiondata.find_one({"_id": token})
        print("value of session details ---- ", newsessionDetails)

    except Exception as e:
        print("Authentication failed ---- ", e)
    if newsessionDetails is not None:
        return "valid"
    else:
        return "invalid"


def deleteSession(db, username, userToken):
    try:
        db.usersessiondata.delete_one({"_id": ObjectId(userToken), 'username': username})
    except Exception as e:
        print("Exception occurred while deleting user session from usersessiondata collection. ----", e)


