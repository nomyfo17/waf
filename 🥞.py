import time
import random
import os

#say = print
#ask = input
#run = break/start(run)

print("Welcome to WAF/🥞")

loc = []

def clear():
    print(".  ")
    time.sleep(0.1)
    print(".. ")
    time.sleep(0.1)
    print("...")
    time.sleep(0.1)
    print(".  ")
    time.sleep(0.1)
    print(".. ")
    time.sleep(0.1)
    print("...")
    time.sleep(0.1)

def search():
    print("</>  " + "txt = what you type will type back")
    time.sleep(0.2)
    print("</>  " + "hw = print Hello World")
    time.sleep(0.2)
    print("</>  " + "clear = clear past commands")
    time.sleep(0.2)
    print("</>  " + "search = command vocab")
    time.sleep(0.2)
    print("</>  " + "name = file a new file")
    time.sleep(0.2)
    print("</>  " + "save = save a file must be under name")
    time.sleep(0.2)

def name():
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

def txt():
    for cmnd in loc:
        print("</>  " + cmnd)

def hw():
    print("</>  " + "Hello World!")

def clear():
    loc.clear()
    os.system('clear')
    print("</>  " + "history cleared")

def run():
    print("</> (🥞) -1/2-")

def name():
    print("code or txt")
    time.sleep(0.2)
    fullcode = []
    def names2():
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
    names2()


while True:
    while True:
        cmnd = input("🥞 </> (  ")
        if cmnd == "run":
            run()
            break
        else:
            loc.append(cmnd)
    print("</> (🥞) -  ")
    for cmnd in loc:
        if loc.__contains__("txt"):
            txt()
        if loc.__contains__("hw"):
            hw()
        if loc.__contains__("clear"):
            loc.clear()
            clear()
        if loc.__contains__("search"):
            search()
        
        if loc.__contains__("name"):
            name()
