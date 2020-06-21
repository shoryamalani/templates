const socket = io()
var id;

socket.emit("get_id", window.location.href.split("/")[window.location.href.split("/").length - 1])

socket.on("sending_id", function(data) {
    id = data
})

socket.on("return_room", function(data) {
    alert(data["status"])
    if (data["status"] == "ok") {
        data["room_participants"].forEach(element => {
            var name = document.createElement("p")
            name.textContent = element
            document.getElementById("participants").appendChild(name)
        })
    }
})
window.onbeforeunload = function() {
        socket.emit("del_user", id)
    }
    // window.addEventListener("beforeunload", function(e) {
    //     socket.emit("del_user", id)
    // }, false);