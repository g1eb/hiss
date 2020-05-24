#!/usr/bin/env python
import os
import random
from pynput import keyboard, mouse

COMBINATION = {
    keyboard.Key.cmd,
    keyboard.Key.ctrl,
}
currently_active = set()

VOCAB = [
    'No!',
    'Noo!',
    'Stop!',
    'Go Away!',
    'Bad Kitty!',
]

def hiss(*args):
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

keyboard_listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release
)
keyboard_listener.start()

mouse_listener = mouse.Listener(
    on_move=hiss,
    on_click=hiss,
    on_scroll=hiss,
)
mouse_listener.start()

def main():
    keyboard_listener.join()
    mouse_listener.join()

if __name__ == '__main__':
    main()
