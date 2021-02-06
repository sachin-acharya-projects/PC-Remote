import socket, os, launch, pickle, subprocess, datetime

socketStd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketStd.bind((socket.gethostname(), 1234))
socketStd.listen(5)
clientsocket, address = socketStd.accept()
print("Connnected to {}".format(address))
clientsocket.send(bytes("no Please Provide Command", "utf-8"))

def sendMessage(result):
    if result == False:
        clientsocket.send(bytes("Sorry Error Occured\nMaybe Given Command is not available", "utf-8"))
    else:
        clientsocket.send(bytes(result, "utf-8"))
    return "Sent: {}".format(result)
while True:
    data = clientsocket.recv(500).decode('utf-8')
    if data == 'quit server':
        sendMessage("Closing Connection")
        break
    elif data == 'clear screen':
        sendMessage("Please Provide Command")
        os.system("cls")
    elif data.startswith('play youtube'):
        result = launch.youtube(data.replace('play youtube', '', 1))
        print(sendMessage(result))
    elif data == 'Empty Command':
        print("Empty Command")
        sendMessage('Use "Help" to See Usage')
    elif data == 'play musics -r':
        output = launch.PlayMusics()
        sendMessage("Playing {}".format(output.split('\\')[len(output.split('\\'))-1]))
    elif "get musics list" in data:
        if data == "get musics list":
            data = "null"
        else:
            data = data.replace('get musics list ', '', 1)
            print(data)
        sendMessage(launch.generateMusicDirectory(data))
    elif data == "test":
        sendMessage('''\
                    ____====-_____-====_____
               _--^^^#####//      \\#####^^^--_
            _-^##########// (    ) \\##########^-_
           -############//  |\\^^/|  \\############-
         _/############//   (@::@)   \\############\\_
         /#############((    \\  /     ))#############\\
        -###############\\    (oo)    //###############-
       -#################\\  / VV \\  //#################-
      -###################\\/      \\//###################-
    _#/|##########/\\######(   /\\   )######/\\##########|\\#_
    |/ |#/\\#/\\#/\\/  \\#/\\##\\  |  |  /##/\\#/  \\/\\#/\\#/\\#| \\|
    `  |/  V  V  `   V  \\#\\| |  | |/#/  V    V V |
       '   '  '      '   / | |  | | \\   '      '  '   '
                        (  | |  | |  )
                       __\\ | |  | | /__
                      (vvv(VVV)(VVV)vvv)

  --------------------------------------------------------------
                        SACHIN ACHARYA
        ''')
    elif data == 'version':
        sendMessage("Version: 0.1.1\nName: Remote PC\nUser: Root@Sachin Acharya")
    elif data.startswith('print("') and data.endswith('")'):
        get = data.replace("print", "", 1).replace('("', '', 1).replace('")', '', 1)
        if get != '':
            sendMessage(get)
        else:
            sendMessage("danger Empty Parameter not allowed")
    elif data.startswith('echo'):
        get = data.replace('echo ', '', 1)
        if get != '':
            sendMessage(f"danger {get}")
        else:
            sendMessage("danger Empty Parameter not allowed")
    elif data.startswith("start "):
        get = data.replace("start ", '', 1)
        try:
            os.startfile(get)
            sendMessage("Openning {}".format(get))
        except FileNotFoundError:
            sendMessage("danger File is not found")
    elif data == 'date' or data == 'datetime':
        sendMessage(launch.dateandtime())
    else:
        print(data)
        sendMessage("danger Command Line Error\n'{}' isn't Recognized ERROR: 100".format(data))
clientsocket.close()