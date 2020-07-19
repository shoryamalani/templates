function mySearch() {
    // Declare variables
    var input, filter, ul, li, a, i, txtValue;
    input = document.getElementById('myInput');
    filter = input.value.toUpperCase()
    ul = document.getElementById("myUL");
    li = ul.getElementsByTagName('li');

    // Loop through all list items, and hide those who don't match the search query
    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("label")[0];
        txtValue = a.textContent || a.innerText;
        var filter_words = filter.split(" ")
        var final_num = true
        console.log(filter_words)
        filter_words.forEach(word => {
            if (txtValue.toUpperCase().indexOf(word) < 0) {
                final_num = false
            }
        });



        if (final_num) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}

function send() {
    inputs = document.getElementsByTagName("input")
    final_chats = []
    for (var i = 0; i < inputs.length; i++) {
        if (inputs[i].checked) {
            final_chats.push(inputs[i].id)
        }
    }
    data = { "chats": final_chats, "text": document.getElementById("textbox").value }
    fetch("/submit_message", {
        method: "POST",
        body: JSON.stringify(data)
    })
}
