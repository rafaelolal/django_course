console.log("Connected", alternateColor)

var headOne = document.querySelector("#one")
var headTwo = document.querySelector("#two")
var headThree = document.querySelector("#three")

function alternateColor() {
    if (headOne.style.color == "black") {
        headOne.style.color = "red";
    } 
    else {
        headOne.style.color = "black";
    }
}

headOne.addEventListener('mouseover', alternateColor)