import socket, os, colorama
from colorama import Fore
colorama.init(autoreset=True)
socketStd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketStd.connect((socket.gethostname(), 1234))
while True:
    msg = socketStd.recv(1000).decode("utf-8")
    if msg.startswith("no"):
        print(f"{Fore.WHITE}{msg.replace('no ', '', 1)}")
    elif msg.startswith('danger'):
        print(f"{Fore.RED}{msg.replace('danger ', '', 1)}")
    elif msg.startswith('success'):
        print(f"{Fore.BLUE}{msg.replace('success ', '', 1)}")
    else:
        print(msg)
    message = input("Command@root:~ ")
    if message == "quit" or message == 'exit' or message == 'shutdown':
        socketStd.send(bytes("quit server", "utf-8"))
        print("Closing Connection")
        break
    if message == 'quit this':
        print("Closing Client Side System")
        break
    elif message == 'clear screen' or message == 'clear' or message == 'cls':
        socketStd.send(bytes("clear screen", "utf-8"))
        os.system("cls")
    elif message == '':
        socketStd.send(bytes("Empty Command", "utf-8"))
    else:
        socketStd.send(bytes(message, "utf-8"))
socketStd.close()