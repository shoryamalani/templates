const socket = io()
var id;
socket.emit("get_inital_data")


function submit_text() {
    socket.emit("send_data", { "data": document.getElementById("text").value })
}


function get_room(id) {
    window.location.href = "room/" + id
}

function create_room() {
    socket.emit("create_room", { "name": prompt("Name:") })
}

socket.on("get_rooms", function(data) {
    console.log(data)
    data.forEach(element => {
        key = Object.keys(element)[0]
        var button = document.createElement("button")
        button.textContent = key
        button.onclick = function() { get_room(String(element[key])) }
        document.body.appendChild(button)
    })
})

socket.on("sending_id", function(data) {
    id = data
})