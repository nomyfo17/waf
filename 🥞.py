import time
import random
import os

#say = print
#ask = input
#run = break/start(run)

loc = []

while True:
    while True:
        cmnd = input("🥞 </> (  ")
        if cmnd == "run":
            print("</> (🥞) -1/2-")
            break
        elif cmnd.__contains__("name"):
            loc.append(cmnd)
            break
        elif cmnd == "clear":
            print(".  ")
            time.sleep(0.5)
            print(".. ")
            time.sleep(0.5)
            print("...")
            time.sleep(0.5)
            print(".  ")
            time.sleep(0.5)
            print(".. ")
            time.sleep(0.5)
            print("...")
            time.sleep(0.5)
            loc.append(cmnd)
            break
        else:
            loc.append(cmnd)
    print("</> (🥞) -  ")
    for cmnd in loc:
        if loc.__contains__("txt"):
            print("</>  " + cmnd)
        if loc.__contains__("hw"):
            print("</>  " + "Hello World!")
        if loc.__contains__("clear"):
            loc.clear()
            os.system('clear')
            print("</>  " + "history cleared")
        if loc.__contains__("option"):
            loc.clear()
            print("</>  " + "txt = what you type will type back")
            time.sleep(3)
            print("</>  " + "hw = print Hello World")
            time.sleep(3)
            print("</>  " + "clear = clear past commands")
            time.sleep(3)
            print("</>  " + "search = command vocab")
            time.sleep(3)
            print("</>  " + "name = file a new file")
            time.sleep(3)
            print("</>  " + "save = save a file must be under name")
            time.sleep(3)
        
        if loc.__contains__("name"):
            print("code or txt")
    time.sleep(0.2)
    fullcode = []
    while True:
        time.sleep(0.5)
        code = input(" -  ")
        if code == "save":
            break
        else:
            fullcode.append(code)
    time.sleep(0.2)
    filename = input("file name -  ")
    with open(filename, "a") as file:
        for item in fullcode:
            file.write(str(item) + "\n")
    print("file sussecfullly saved!")
