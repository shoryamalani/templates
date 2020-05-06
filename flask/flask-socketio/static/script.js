const socket = io()

function submit_text() {
    socket.emit("send_data", { "data": document.getElementById("text").value })
}


socket.on("send_data_back", function(data) {
    document.getElementById("result").textContent = data["data"]
})