import time
import asyncio

import websockets


class DanmakuServer:

    def __init__(self):
        self.clients = []
        self.connected = []
        self.history = []

    async def reply(self, websocket):
        ticks = int(time.time() % 10086)
        name = "user" + str(ticks)
        self.clients.append(name)
        self.connected.append(websocket)
        for msg in self.history:
            await websocket.send(msg)

        try:
            while True:
                msg = await websocket.recv()
                self.history.append(msg)
                websockets.broadcast(self.connected, msg)

        except websockets.exceptions.ConnectionClosedOK:
            print("Bye{}".format(name))
        finally:
            self.clients.remove(name)
            self.connected.remove(websocket)
            websocket.close()
            print(len(self.connected))
            print("{} has been removed".format(name))


if __name__ == "__main__":
    server = DanmakuServer()
    asyncio.get_event_loop().run_until_complete(
        websockets.serve(server.reply, 'localhost', 8765))
    asyncio.get_event_loop().run_forever()
