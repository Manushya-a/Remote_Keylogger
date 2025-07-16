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

async def handle_client(websocket):
    """Handle incoming WebSocket connections with robust error handling"""
    client_addr = websocket.remote_address
    print(f"New connection from {client_addr}")
    
    try:
        async for message in websocket:
            try:
                # Process quit command
                if message.lower() == "quit":
                    print(f"Client {client_addr} requested disconnect")
                    await websocket.send("Goodbye! Closing connection.")
                    await websocket.close()
                    break
                
                # Log and acknowledge normal messages
                print(f"Received from {client_addr}: {message}")
                await websocket.send(f"ACK: {message}")
                
            except websockets.exceptions.ConnectionClosed:
                print(f"Client {client_addr} disconnected during message processing")
                break
            except Exception as e:
                print(f"Error processing message from {client_addr}: {str(e)}")
                await websocket.send(f"ERROR: {str(e)}")
                
    except websockets.exceptions.ConnectionClosedOK:
        print(f"Client {client_addr} disconnected normally")
    except websockets.exceptions.ConnectionClosedError:
        print(f"Client {client_addr} disconnected unexpectedly")
    except Exception as e:
        print(f"Connection error with {client_addr}: {str(e)}")
    finally:
        print(f"Connection closed with {client_addr}")
        if not websocket.closed:
            await websocket.close()

async def main():
    async with websockets.serve(handle_client, "0.0.0.0", 8765) as server:
        print(bcolors.ORANGE + "[" + str(datetime.now()) + "]" + bcolors.ENDC + "Websocker Server started")
        while True:
            await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())