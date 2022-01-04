function onClick() {
    console.log("h1 clicked")
    $(this).text($(this).text() + "I")
}

$('h1').click(onClick)

$('input').eq(0).keypress(function() {
    $('h3').toggleClass("turnBlue")
})