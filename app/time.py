from app import db
from models import User
import time
from sys import platform

class Time(db.Model):
	id = db.Column(db.Integer, nullable = False, primary_key = True)
	time = db.Column(TIME(), nullable=False)
	system = db.Column(platform., nullable=False)

	user_id = db.Column(db.Integer,db.ForgeignKey('user.id'))
	user = db.relationship('User', backref=backref("request", uselist=False))

'''
@app.route("/getTime",methods=['GET'])
def getTime():
	print("browser time: ", request.args.get("time"))
    print("server time : ", time.strftime('%A %B, %d %Y %H:%M:%S'));
    print("Done")
'''
