from app.extensions import db, FBUser

def get_all_users() -> [dict]:
    users_dict = db.child('users').get().val()
    users = []

    for uid in users_dict:
        user_info = users_dict[uid]

        # Parsing into FBUser Python object
        fb_user = FBUser(uid, user_info)

        # Taking that Object into plain Dict
        user_dict = fb_user.get_dict()

        # append to later use in HTML Flask Rendering
        users.append(user_dict)

    return users

def get_user(username: str) -> FBUser:
    users_dict = db.child('users').get().val()
    fb_user = None
    for uid in users_dict:
        if (users_dict[uid]['email'] == username+"@uci.edu"):
            user_info = users_dict[uid]
            fb_user = FBUser(uid, user_info)
    return fb_user
