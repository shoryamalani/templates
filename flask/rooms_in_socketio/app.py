#Dependencies
from flask import Flask,render_template,session,redirect,url_for,jsonify,send_from_directory,g
from flask_socketio import SocketIO,emit,join_room,leave_room,send
import random
import json
# App stuff
app = Flask(__name__)#,template_folder="./dist/app/templates"
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,async_mode=None)


#Classes

class User:
    def __init__(self):
        global users
        self.id = create_id(users)
    def add_name(self,name):
        self.user_name = name
class Room:
    def __init__(self,name):
        global rooms
        self.name = name
        self.id = create_id(rooms)
        self.participants = []
    def add_user(self,user):
        self.participants.append(user)


#Functions
def create_id(list_of):
    while True:
        ids = []
        for item in list_of:
            ids.append(item.id)
        new_id = random.randint(10000000,10000000000)
        if new_id not in ids:
            return new_id
        
def get_room(id):
    global rooms
    for room in rooms:
        if room.id == id:
            return room
    return "no room"

def remove_user(id):
    global users
    for user in users:
        if user.id == id:
            users.remove(user)
#Routers
@app.route("/",methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/room/<id>")
def room(id):
    return render_template("room.html")

#Socket
#This receives data
# @socketio.on("send_data")
# def send_data(data):
#     #send data
#     emit("send_data_back",{"data":data["data"]})

#window.location.href.split("/")[window.location.href.split("/").length-1]
@socketio.on("get_inital_data")
def get_inital_data():
    global rooms
    emit("get_rooms",[{room.name:room.id} for room in rooms])

@socketio.on("get_id")
def get_id(data):
    global users
    user = User()
    users.append(user)
    emit("sending_id",user.id)
    try:
        int_data = int(data)
        room = get_room(int_data)
        room.add_user(user)
        if room != "no room":
            emit("return_room",{"status":"ok","room_participants":[participant.id for participant in room.participants]})
        else:   
            emit("return_room",{"status":"no room"})
    except:
        emit("return_room",{"status":"no room"})
        

@socketio.on("create_room")
def create_room(data):
    global rooms
    room = Room(data["name"])
    rooms.append(room)
    redirect(url_for("room",id=room.id))
    return emit("get_rooms",[{room.name:room.id}])
    # emit("join_room")
    

@socketio.on("del_user")
def remove_from_room(data):
    print(data)
#Run
if __name__ == "__main__":
    #Globals

    users = []
    rooms = []
    rooms.append(Room("test"))
    socketio.run(app,host="0.0.0.0",port=5000,debug=True)
    
    #  app.run(host="0.0.0.0",port=5000)