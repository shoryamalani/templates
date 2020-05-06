#Dependencies
from flask import Flask,render_template,session,redirect,url_for,jsonify,send_from_directory
from flask_socketio import SocketIO,emit,join_room,leave_room,send

# App stuff
app = Flask(__name__)#,template_folder="./dist/app/templates"
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,async_mode=None)

#Routers
@app.route("/",methods=["GET"])
def home():
    return render_template("index.html")

#Socket

#This receives data
@socketio.on("send_data")
def send_data(data):
    #send data
    emit("send_data_back",{"data":data["data"]})


#Run
if __name__ == "__main__":
    socketio.run(app,host="0.0.0.0",port=5000,debug=True)
    #  app.run(host="0.0.0.0",port=5000)