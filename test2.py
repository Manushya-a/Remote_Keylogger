from pynput.keyboard import Key, Controller

keyboard = Controller()

keyboard.type("python test.py")

keyboard.press(Key.enter)
keyboard.release(Key.enter)