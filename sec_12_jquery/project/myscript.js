createBoard()
var buttons = $(".btn-secondary")

var p1 = prompt("Enter player 1's name")
var p2 = prompt("Enter player 2's name")

var p1Color = 'rgb(0, 0, 128)'
var p2Color = 'rgb(128, 0, 0)'
var gray = 'rgb(128, 128, 128)'
var otherGray = 'rgb(92, 99, 106)'

var turnMsg = ", it is your turn!"
$('#turn').text(p1 + turnMsg)
var p1Turn = true

function createBoard() {    
    for (var i = 0; i < 6; i += 1) {
        var row = ""
        for (var j = 0; j < 7; j += 1) {
            row += '<td><button row='+i + ' col='+j + ' type="button" class="btn btn-secondary"></button></td>'
        }
        row = "<tr>" + row + "</tr>"
        $('#board').html($('#board').html() + row)
    }    
}

$('.btn-secondary').on('click', function () {
    var bottom = findBottom($(this).attr("col"))
    if (bottom) {
        if (p1Turn) {
            changeColorOf(bottom, p1Color)
            p1Turn = false
        }
        else {
            changeColorOf(bottom, p2Color)
            p1Turn = true
        }
        changeTurnMsg()
    }

    if (checkWin()) {
        alert("Someone won!")
    }

})

function findBottom(col) {
    var bottom_row = "0"
    for (button of buttons) {
        if ($(button).attr("col") == col
            && (colorOf(button) == gray || colorOf(button) == otherGray)
            && $(button).attr("row") > bottom_row) {
            
            bottom_row = $(button).attr("row")
        }
    }

    var bottom = $('button[row$='+bottom_row+'][col$='+col+']')
    if (colorOf(bottom) == gray || colorOf(bottom) == otherGray) {
        return bottom
    }
}

function changeColorOf(button, color) {
    $(button).css('background-color', color)
}

function changeTurnMsg() {
    if (p1Turn) {
        $('#turn').text(p1 + turnMsg)
    }
    else {
        $('#turn').text(p2 + turnMsg)
    }
}

function checkWin() {
    for (button of buttons) {
        if (colorOf(button) != gray && colorOf(button) != otherGray) {
            var row = $(button).attr('row')
            var col = $(button).attr('col')

            var h_sequence = [$('button[row$='+row+'][col$='+(parseInt(col)+1)+']'),
                $('button[row$='+row+'][col$='+(parseInt(col)+2)+']'),
                $('button[row$='+row+'][col$='+(parseInt(col)+3)+']')]

            var v_sequence = [$('button[row$='+(parseInt(row)+1)+'][col$='+col+']'),
                $('button[row$='+(parseInt(row)+2)+'][col$='+col+']'),
                $('button[row$='+(parseInt(row)+3)+'][col$='+col+']')]

            var d_sequence = [$('button[row$='+(parseInt(row)+1)+'][col$='+(parseInt(col)+1)+']'),
                $('button[row$='+(parseInt(row)+2)+'][col$='+(parseInt(col)+2)+']'),
                $('button[row$='+(parseInt(row)+3)+'][col$='+(parseInt(col)+3)+']')]

            var d2_sequence = [$('button[row$='+(parseInt(row)-1)+'][col$='+(parseInt(col)+1)+']'),
                $('button[row$='+(parseInt(row)-2)+'][col$='+(parseInt(col)+2)+']'),
                $('button[row$='+(parseInt(row)-3)+'][col$='+(parseInt(col)+3)+']')]
            
            if (checkSequence(h_sequence, button)
                || checkSequence(v_sequence, button)
                || checkSequence(d_sequence, button)
                || checkSequence(d2_sequence, button)) {

                announceWinner(button)

            }
        }
    }
}

function colorOf(button) {
    return $(button).css('background-color')
}

function checkSequence(sequence, button) {
    var all_equal = true
    for (chip of sequence) {
        if (colorOf(chip) != colorOf(button)) {
            all_equal = false
        }
    }

    if (all_equal) {
        return true
    }
    
    return false
}

function announceWinner(button) {
    if (p1Color == colorOf(button)) {
        if(alert(p1 + " won! Press okay to refresh the page and play again.")){}
        else    window.location.reload(); 
    }
}

