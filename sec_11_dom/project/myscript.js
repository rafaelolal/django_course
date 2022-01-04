var boxes = document.querySelectorAll("#box")

function changeImg(box) {
    if (box.src.includes("empty.png")) {
        box.src = "x.png"
    }
    else if (box.src.includes("x.png")) {
        box.src = "o.png"
    }

    else {
        box.src = "empty.png"
    }
}

for (var i = 0; i < boxes.length; i += 1) {
    (function () {
        var myBox = boxes[i]
        myBox.addEventListener("click", function() {changeImg(myBox)})
    }())
}

function resetBoard() {
    for (box of boxes) {
        box.src = "empty.png"
    }
}

var reset = document.querySelector("#reset")
reset.addEventListener("click", resetBoard)