import sys 
from flask import *
sys.path.append('./')
from DB_ADMIN import db



databaseObj = db.database()

databaseClient = databaseObj.getClient1()
db = databaseClient.login 
collection =db.logindetail

def is_exist(employee):
    for id in collection.find({},{"_id": 0}):
        print("crunt id ="+ id['userid'])
        if((employee["userid"]==id['userid'] and employee["password"]==id["password"]) and employee["role"]==id["role"]):
            print("match")
            return True
    return False

def login():
    employee = request.get_json()
    
    userid = employee["userid"]
    password = employee["password"]
    for id in collection.find({},{"_id": 0}):
        print("crunt id ="+ id['userid'])
        if(employee["userid"]==id['userid'] and employee["password"]==id["password"]):
            return redirect('http://192.168.99.100:32001/hello?userid='+userid+'&password='+password,code=307)
    return jsonify({"message": "unautherized user"})


