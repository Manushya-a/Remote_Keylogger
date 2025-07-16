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
    client_ip, client_port = websocket.remote_address
    print(bcolors.ORANGE + "[" + str(datetime.now()) + "]" + bcolors.MAGENTA + "[" + str(client_ip) + ":" + str(client_port) + "] " + bcolors.ENDC + message)

    
async def main():
    async with websockets.serve(server, "0.0.0.0", 8765):
        print(bcolors.ORANGE + "[" + str(datetime.now()) + "]" + bcolors.ENDC + " Websocket server started and listenig on --> " + bcolors.OKBLUE + "Your.I.P.Address : 8765" + bcolors.ENDC)
        await asyncio.Future() # Run forever


if __name__ == "__main__":
    asyncio.run(main())