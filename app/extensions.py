import pyrebase, os
from urllib.parse import quote

config = {
  "apiKey": os.getenv("API_KEY"),
  "authDomain": "shpe-uci-tech.firebaseapp.com",
  "databaseURL": "https://shpe-uci-tech.firebaseio.com",
  "projectId": "shpe-uci-tech",
  "storageBucket": "shpe-uci-tech.appspot.com"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

db = firebase.database()

def getBasicUserInfo(username: str) -> dict:
    user_dict = None
    u_data = db.child("users").get().val()
    for k in u_data:
        if (u_data[k]['email'] == username+"@uci.edu"):
            user_dict = u_data[k]
    print(user_dict)
    return user_dict