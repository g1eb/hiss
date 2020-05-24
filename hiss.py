#!/usr/bin/env python
import os
import random
from pynput import keyboard, mouse

COMBINATION = {
    keyboard.Key.cmd,
    keyboard.Key.ctrl,
}
currently_active = set()
MOUSE_EVENTS = 0
THRESHOLD = 50

VOCAB = [
    'No!',
    'Noo!',
    'Stop!',
    'Go Away!',
    'Bad Kitty!',
]

def hiss():
    phrase = random.choice(VOCAB)
    os.system('say -v Daniel {}'.format(phrase))

def on_press(key):
    hiss()
    if key in COMBINATION:
        currently_active.add(key)

def on_release(key):
    if key in currently_active:
        currently_active.remove(key)
    if key == keyboard.Key.esc and currently_active:
        keyboard_listener.stop()
        mouse_listener.stop()

keyboard_listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release
)
keyboard_listener.start()

def on_move(x, y):
    global MOUSE_EVENTS
    MOUSE_EVENTS += 1
    if MOUSE_EVENTS >= THRESHOLD:
        MOUSE_EVENTS = 0
        hiss()

def on_click(x, y, button, pressed):
    hiss()

def on_scroll(x, y, dx, dy):
    global MOUSE_EVENTS
    MOUSE_EVENTS += 1
    if MOUSE_EVENTS >= THRESHOLD:
        MOUSE_EVENTS = 0
        hiss()

mouse_listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll,
)
mouse_listener.start()

def main():
    keyboard_listener.join()
    mouse_listener.join()

if __name__ == '__main__':
    main()
