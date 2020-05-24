#!/usr/bin/env python
import os
from pynput import keyboard

def hiss():
    os.system('say -v Daniel No!')

def on_press(key):
    hiss()

def on_release(key):
    if key == keyboard.Key.esc:
        return False

def main():
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release
        ) as listener:
        listener.join()

if __name__ == '__main__':
    main()
