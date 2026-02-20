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
    print("</> (🥞) -2/2-")
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
        
        if loc.__contains__("name"):
            filename = imput("name file -  ")
            listname = []
            while True:
                uname = input("writing file -  ")
                if uname == "run":
                    break
                else:
                    listname.append(uname)
                uname = input("writing file -  ") 
            listname = []
            if loc == "name wof":
                with open(filename + '.waf', 'w') as file:
                    file.write(listname)
            else:
                with open(filename + '.py', 'w') as file:
                    file.write(listname)