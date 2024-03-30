import socket
import threading
from src.helpers import *
import sys 

def execute_command(command):
    try:
        cmd = command.split()[0]
        args = command.split()[1:]

        if cmd == "opengame": 
            console.log("Openning game..")
            open_game()

        if cmd == "closegame":
            console.log("Closing game..")
            close_game()

        

        if cmd == "automove":
            console.log("Start auto move thread..")
            directions = ["w","a","s","d","space"]
            while True:
                auto_move(random.choice(directions))
                time.sleep(random.randint(15,30))

        if cmd == "goisland":
            island_url = command.split()[1]
            console.log("Going to island: ", island_url)
            go_to_island(island_url)
            console.log("Go to island success")

        if cmd == "autohost":
            console.log("Start auto host game matches mode")
            time.sleep(30)
            while True:
                create_match()
                time.sleep(random.randint(600,650))

        if cmd == "autojoin":
            console.log("Start auto accept game mode.")
            time.sleep(30)
            while True:
                accept_match()
                time.sleep(random.randint(10,15))
    
    except Exception as e:
        console.log(e)


def listen_for_commands(host=HOST_IP, port=HOST_PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            command = s.recv(1024).decode()
            if not command:
                break
            print(f"Executing command: {command}")

            if command == "exit":
                console.log("Exitting client..")
                sys.exit()

            threading.Thread(target=execute_command, args=(command,)).start()


if __name__ == '__main__':
    listen_for_commands()
