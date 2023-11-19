input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Scissors)
    basic.clearScreen()
    basic.pause(1000)
})
input.onGesture(Gesture.Shake, function () {
    if (randint(0, 2) == 0) {
        basic.showIcon(IconNames.Scissors)
    } else if (randint(0, 2) == 1) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (randint(0, 2) == 2) {
        basic.showIcon(IconNames.Square)
    }
})
input.onButtonPressed(Button.AB, function () {
    basic.showIcon(IconNames.Square)
    basic.clearScreen()
    basic.pause(1000)
})
input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.SmallSquare)
    basic.clearScreen()
    basic.pause(1000)
})
basic.showLeds(`
    . . . . .
    . . . . .
    . . # . .
    . . . . .
    . . . . .
    `)
basic.clearScreen()
basic.pause(500)
basic.showLeds(`
    . . . . .
    . . . . .
    . . # . .
    . . . . .
    . . . . .
    `)
basic.clearScreen()
basic.pause(500)
basic.forever(function () {
	
})
