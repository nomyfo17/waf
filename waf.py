import time
import random
import os
import socket
import threading
import sys

print("Welcome to waf, commandline")

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
    print("</>  " + "txt = replay the saved command history; it prints every previous input except the literal 'txt' command itself")
    time.sleep(0.2)
    print("</>  " + "hw = print Hello World")
    time.sleep(0.2)
    print("</>  " + "clear = clear command history")
    time.sleep(0.2)
    print("</>  " + "search = show this help menu")
    time.sleep(0.2)
    print("</>  " + "name = save text to a file")
    time.sleep(0.2)
    print("</>  " + "random = generate a random number")
    time.sleep(0.2)
    print("</>  " + "editor = text editor")
    time.sleep(0.2)
    print("</>  " + "passgen = generate a random password by length")
    time.sleep(0.2)
    print("</>  " + "tchat connect = connect to chat server")
    time.sleep(0.2)
    print("</>  " + "tchat host = host a chat server")

def texteditor():
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
            file.write(item + "\n")
    print("file successfully saved!")

def name():
    print("code or type")
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
    filetype = input("Add to file, or write a new file? [a/w]")
    with open(filename, filetype) as file:
        for item in fullcode:
            file.write(item + "\n")
    print("file successfully saved!")

def history():
    for item in loc:
        if item == "*args*":
            print(item)
        else:
            print("No history found.")

def clientchat():
    hoster = input("Host IP -  ")
    HOST = int(hoster)
    PORT = 6543, int(input("Port ID -  "))

    def receive_messages(client_socket):
        """Background thread function: continually listens for data from the server."""
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    print("\nConnection closed by server.")
                    break
                # Clear line and print incoming text, then refresh prompt
                print(f"\r{message}")
                print("You: ", end="", flush=True)
            except:
                print("\nAn error occurred while receiving data.")
                break
            client_socket.close()
            sys.exit()

    def start_client():
        name = input("Enter your username: ")
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client_socket.connect((HOST, PORT))
        except ConnectionRefusedError:
            print("Could not connect to server. Is server.py running?")
            return

        print(f"Connected to chat! Type anything and hit Enter.\n")

        # Start the receiving thread
        # Setting daemon=True means this thread automatically dies when the main program exits
        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.daemon = True
        receive_thread.start()

        # Main thread handles sending inputs
        while True:
            try:
                user_input = input("You: ")
                if user_input.strip():
                    formatted_message = f"{name}: {user_input}"
                    client_socket.send(formatted_message.encode('utf-8'))
            except (KeyboardInterrupt, EOFError):
                print("\nExiting chat.")
                client_socket.close()
                break

    if __name__ == "__main__":
        start_client()

def serverchat():
    # Server configuration
    HOST = 'localhost'
    print("Host IP is, ", 'localhost')
    input("Port ID -  ")
    PORT = 6543, int(input("Port ID -  "))

    clients = []

    def broadcast(message, current_client):
        """Sends a message to all clients except the sender."""
        for client in clients:
            if client != current_client:
                try:
                    client.send(message)
                except:
                    # If sending fails, the client likely disconnected
                    remove_client(client)

    def handle_client(client):
        """Handles the continuous stream of data from a single client."""
        while True:
            try:
                # Receive data (up to 1024 bytes) and decode it
                message = client.recv(1024)
                if not message:
                    break
                broadcast(message, client)
            except:
                break
            remove_client(client)

    def remove_client(client):
        """Safely cleans up a disconnected client."""
        if client in clients:
            clients.remove(client)
            client.close()
            print(f"A client disconnected. Total clients: {len(clients)}")

    def start_server():
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # allow immediate reuse of the port after stopping the server
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()
        print(f"Server is listening on {HOST}:{PORT}...")
        while True:
            client_socket, address = server.accept()
            print(f"Connected with {str(address)}")
            clients.append(client_socket)
            # Start a thread to handle this specific client concurrently
            thread = threading.Thread(target=handle_client, args=(client_socket,))
            thread.daemon = True # Allows server to exit cleanly on Ctrl+C
            thread.start()

    if __name__ == "__main__":
        try:
            start_server()
        except KeyboardInterrupt:
            print("\nServer shutting down.")

def helloworld():
    print("</>  " + "Hello World!")

def clear():
    loc.clear()
    os.system('clear' if os.name == 'posix' else 'cls')
    print("</>  " + "history cleared")

def randomnumber():
    print(random.randint(1, 100))

def clienttchat():
    client = socket.socket()
    ipa = input("ip -  ")
    client.connect((ipa, 7924))
    print("Connected to Chat")
    while True:
        message = input(" -  ")
        if message == "exit":
            break
        client.send(message.encode())
        data = client.recv(1024)
        message = data.decode()
        print(ipa + ": " + message)

def servertchat():
    server = socket.socket()
    ipa = input("ip -  ")
    server.bind((ipa, 7924))
    server.listen(1)
    client, address = server.accept()
    print("User Connected: " + str(address))
    while True:
        data = client.recv(1024)
        message = data.decode()
        print(str(address) + ": " + message)
        response = input(" -  ")
        if response == "exit":
            break
        client.send(response.encode())


def passgen(arg_str=None):
    def parse_args(text):
        if not text:
            return None
        text = text.strip()
        if text.startswith("(") and text.endswith(")"):
            text = text[1:-1].strip()
        if text.isdigit():
            value = int(text)
            return value, value

        if "," in text:
            parts = [part.strip() for part in text.split(",", 1)]
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                return int(parts[0]), int(parts[1])

        if "from" in text:
            parts = [part.strip() for part in text.split("from", 1)]
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                return int(parts[0]), int(parts[1])
            if parts[0] == "" and parts[1].isdigit():
                value = int(parts[1])
                return value, value

        return None

    parsed = parse_args(arg_str)
    if parsed is None:
        while True:
            try:
                count = int(input("Number of characters: "))
                if count <= 0:
                    print("Please enter a positive number.")
                    continue
                parsed = (count, count)
                break
            except ValueError:
                print("Please enter a valid integer.")

    min_length, max_length = parsed
    if min_length <= 0 or max_length <= 0:
        print("Length values must be positive.")
        return
    if min_length > max_length:
        min_length, max_length = max_length, min_length

    length = random.randint(min_length, max_length)
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:,.<>?"
    password = "".join(random.choice(alphabet) for _ in range(length))
    print(f"Generated password ({length} chars): {password}")


commandsHashtable = {
    "hw": helloworld,
    "history": history,
    "clear": clear,
    "search": search,
    "name": name,
    "random": randomnumber,
    "editor": texteditor,
    "password": passgen,
    "tchat -connect": clienttchat,
    "tchat -host": servertchat,
    "chat -start": serverchat,
    "chat -reach": clientchat
}

while True:
    cmnd = input(" -  ")
    try:    
        loc.append(cmnd)
        if cmnd.startswith("passgen"):
            args = cmnd[len("passgen"):].strip()
            passgen(args if args else None)
        elif cmnd.startswith("password"):
            args = cmnd[len("password"):].strip()
            if args.startswith("-"):
                args = args[1:].strip()
                passgen(args if args else None)
        elif cmnd in commandsHashtable:
            commandsHashtable[cmnd]()
        else:
            print("Invalid Command")
        if cmnd == "quit":
            break
        if not loc.__contains__("clear") and not loc.__contains__("history"):
            loc = []
    except KeyboardInterrupt:
        print("Try again, type 'quit' to exit, or 'search' for help.")
