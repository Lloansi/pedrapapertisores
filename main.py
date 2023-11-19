def on_button_pressed_a():
    basic.show_icon(IconNames.SCISSORS)
    basic.clear_screen()
    basic.pause(1000)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    if randint(0, 2) == 0:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif randint(0, 2) == 1:
        basic.show_icon(IconNames.SQUARE)
    elif randint(0, 2) == 2:
        basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    basic.show_icon(IconNames.SQUARE)
    basic.clear_screen()
    basic.pause(1000)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_icon(IconNames.SMALL_SQUARE)
    basic.clear_screen()
    basic.pause(1000)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_leds("""
    . . . . .
    . . . . .
    . . # . .
    . . . . .
    . . . . .
    """)
basic.clear_screen()
basic.pause(500)
basic.show_leds("""
    . . . . .
    . . . . .
    . . # . .
    . . . . .
    . . . . .
    """)
basic.clear_screen()
basic.pause(500)

def on_forever():
    pass
basic.forever(on_forever)
