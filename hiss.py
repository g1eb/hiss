#!/usr/bin/env python
import os
from pynput import keyboard

COMBINATION = {
    keyboard.Key.cmd,
    keyboard.Key.ctrl,
}
currently_active = set()

def hiss():
    os.system('say -v Daniel No!')

def on_press(key):
    hiss()
    if key in COMBINATION:
        currently_active.add(key)

def on_release(key):
    if key in currently_active:
        currently_active.remove(key)
    if key == keyboard.Key.esc and currently_active:
        return False

def main():
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release
        ) as listener:
        listener.join()

if __name__ == '__main__':
    main()
