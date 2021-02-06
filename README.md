# PC REMOTE
This is a Simple program use to Control your PC from anyother devices like Mobile and PC from
anywhere with internet connection.
It is like, using Command Prompt, which have only feature and command line created by me.
## INSTALLATION
__For Server Side__:
_Server Side: Your computer to be controlled_
_Install all the requirements using PIP. _
````
pip install -r requirements.txt
````
_For Linux_:
````
pip3 install -r requirements.txt
````
_Once completion of Installation run the script **Server.py**"_
````
python Server.py
````
*For Linux*
````
python3 Server.py
````
_Now everything is setup and fine_
__Now For Client side__
_Client Side: Device controlling from_
_Install requirents with PIP just like above Installation but replace requirements.txt file with_
_reqClient.txt_
_Not Afterward run script *Client like above*_

## NOTE
__For Client side Script *launch.py* in not necessary but for server side it is mandatory__

## COMMAND LINE
````
quit / exit / close
````
_Use to close current session of both client and server. It close connection between client and server_
````
clear / cls / clear screen
````
_Use to Clear the Screen of both Client and Server_
````
play youtube [title]
````
_Search and Open the video with given title on YouTube_
_Selection of video is done on the basis of Number of times video played or Popularity_
````
play musics -r
````
_Randomly plays music_
````
get musics list [data]
````
_Data: Directory of Musics_
_It scans the directory given (data e.g. C:\Users\Name\Music) for musics and data is not given than it will scan Music library_
_I.e. C:\Users\username\Music_
````
Version
````
_Displays version of product_
````
print("data") or echo data
````
_These are use to print (data) on the screen. Difference between them is echo print in red colour where print prints in terminal default colour_
````
start data
````
_It opens (data). If it is a File or executable it will be opened and if it is directory, directory will be opened_
````
date or datetime
````
_It displays current date and time_
