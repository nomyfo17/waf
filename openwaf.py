import time
import random

#say = print
#run = break/start(run)

loc = []

while True:
    while True:
        cmnd = input("Open 🥞 -  ")
        if cmnd == "run":
            break
        elif cmnd == "clear":
            loc.append(cmnd)
            break
        else:
            loc.append(cmnd)
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
            time.sleep(5)
            print("</>  " + "hw = print Hello World")
            time.sleep(5)
            print("</>  " + "clear = clear past commands")
            time.sleep(5)
            print("</>  " + "option = command vocab")
            time.sleep(5)
