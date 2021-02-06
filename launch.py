"""""""""""""""""""""""""""""""""""""""""
DEFINATIONS OF FUNTIONS
"""""""""""""""""""""""""""""""""""""""""
import random, os, pywhatkit, datetime
userprofile = os.environ.get('USERPROFILE')
def youtube(query):
    try:
        pywhatkit.playonyt(query)
        return "Playing{} in YouTube".format(query)
    except:
        return False

def chooseMusics():
    try:
        file = open("musics.txt", "r")
    except FileNotFoundError:
        print("File Not Created")
    lines = file.readlines()
    if len(lines) > 0:
        randomInt = random.randint(0, len(lines)-1)
        winnerDirectory = lines[randomInt].replace('/', '\\').replace("\n", "")
        return winnerDirectory
    else:
        return "false"
    file.close()
def PlayMusics():
    music = chooseMusics()
    if music == "false":
        return "danger Cannot Found Musics\nRun 'get musics list [directory to search in]' to List all  musics"
    else:
        try:
            os.startfile(music)
            return music
        except FileNotFoundError:
            print("File Cannot be Found, Wanna Scan Directory?")
            return "danger Listed Files cannot be found\nRun 'get musics list [directory to search in]' to Update List"
def generateMusicDirectory(data):
    if data == 'null':
        directoryMusic = os.path.join(userprofile, "Music")
    else:
        directoryMusic = os.path.join(data)
    file = open("musics.txt", "w")
    walkedDir = os.walk(directoryMusic)
    for root,_, contents in walkedDir:
        for item in contents:
            if item.endswith('.mp3') or item.endswith('.m4a'):
                file.write(root+"\\"+item+"\n")
    file.close()
    return "success Music List Updated Successfully"
def dateandtime():
    data = datetime.datetime.now()
    event = "AM"
    hour = data.hour
    if hour > 12:
        hour = hour - 12
        event = "PM"
    minute = data.minute
    if minute < 10:
        minute = "0{}".format(minute)
    second = data.second
    if second < 10:
        second = "0{}".format(second)
    year = data.year
    date = data.day
    month = ["Janaury", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][data.month-1]
    day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][data.weekday()]
    calender = "{} {}, {} {} {}:{}:{} {}".format(month, date, year, day, hour, minute, second, event)
    return calender