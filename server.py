import socket
import threading
import sys
from src.settings import *


class ClientHandler:
    def __init__(self, conn, addr, id):
        self.conn = conn
        self.addr = addr
        self.id = id
        self.name = self.regconize(addr)

    def regconize(self, addr):
        for k, v in VPS.items():
            if v == addr[0]: 
                return k
        return "unknown"

    def listen_for_commands(self):
        while True:
            try:
                data = self.conn.recv(1024)
                if data:
                    print(f"Message from {self.id}: {data.decode()}")
            except:
                break

clients = {}
client_id_counter = 1

def accept_connections(s):
    global client_id_counter
    while True:
        conn, addr = s.accept()
        client_handler = ClientHandler(conn, addr, client_id_counter)
        clients[client_id_counter] = client_handler
        threading.Thread(target=client_handler.listen_for_commands).start()
        print(f"Client {client_id_counter} connected from {addr}")
        client_id_counter += 1

def server_menu():
    while True:
        print("\nServer Menu:")
        print("1. List connected clients")
        print("2. Send command to a client")
        print("3. Send command to ALL clients")
        print("4. Exit")
        print("5. Start auto farm bloom.")

        choice = input("Enter your choice: ")
        if choice == '1':
            for id in clients:
                print(f"Client ID: {id}, Name: {clients[id].name} Address: {clients[id].addr}")
        elif choice == '2':
            client_ids = int(input("Enter client ID (1 2 3): "))
            command = input("Enter command to send: ")
            for client_id in client_ids.split(): 
                if client_id in clients: 
                    try:
                        print(f"Send command {command} to client {client_id}")
                        clients[client_id].conn.sendall(command.encode())
                    except Exception as e:
                        print(e)
                        print("Client disconnected")
                else:
                    print("Client not found.")

        elif choice == '3':
            command = input("Enter command to send: ")
            for id in clients:  
                try:
                    clients[id].conn.sendall(command.encode())
                except Exception as e:
                    print(e)
                    print("Client disconnected")

            print("Success send command to all servers.")

        elif choice == '4':
            for id in clients:
                clients[id].conn.close()
            sys.exit("Shutting down server.")

        elif choice == '5':
            print("Start auto farm bloom..")
            """Game should opened, Go to Island, Start mode, Accept mode, Auto Move"""
            # start game
            commands = [
                f"autofarm {ISLANDS[0]} autohost",
                f"autofarm {ISLANDS[0]} autojoin",
                f"autofarm {ISLANDS[2]} autohost",
                f"autofarm {ISLANDS[2]} autojoin",
                f"autofarm {ISLANDS[4]} autohost",
                f"autofarm {ISLANDS[4]} autojoin",
                f"autofarm {ISLANDS[6]} autohost",
                f"autofarm {ISLANDS[6]} autojoin",
                f"autofarm {ISLANDS[8]} autohost",
                f"autofarm {ISLANDS[8]} autojoin",
            ]
            index = 0
            for id in clients:  
                clients[id].conn.sendall(commands[index].encode())
                index+=1

            print("Completed auto farm bloom..")    

        else:
            print("Invalid choice.")

def start_server(host='0.0.0.0', port=HOST_PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server started. Listening on {host}:{port}")
        threading.Thread(target=accept_connections, args=(s,)).start()
        server_menu()

if __name__ == '__main__':
    start_server()
