import datetime
from typing import List
from pythonosc import dispatcher
from pythonosc import osc_server

# Define
class Network:
    IP_ADDRESS:str = "127.0.0.1"
    SEND_PORT:int = 39570
    RECEIVE_PORT:int = 39571

Addresses = [
    "/VMT/Out/Log",
    # "/VMT/Out/Alive",
    "/VMT/Out/Haptic",
    # "/VMT/Out/Unavailable",
    "/VMT/Out/Devices/List",
    "/VMT/Out/SubscribedDevice",
]

def callbackMessage(address:str, *message:List[str]) -> None:
    print(f"{datetime.datetime.now()} | add {address} \tout:{message}")

def VMT_receive(addresses:list=Addresses,network:Network=Network) -> None:
    _dispatcher = dispatcher.Dispatcher()
    for address in addresses:
        _dispatcher.map(address, callbackMessage)

    server = osc_server.ThreadingOSCUDPServer(
        (network.IP_ADDRESS, network.RECEIVE_PORT), _dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()

if __name__ == "__main__":
    VMT_receive()
