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
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            for id in clients:
                print(f"Client ID: {id}, Name: {clients[id].name} Address: {clients[id].addr}")
        elif choice == '2':
            client_id = int(input("Enter client ID: "))
            if client_id in clients:
                command = input("Enter command to send: ")
                clients[client_id].conn.sendall(command.encode())
            else:
                print("Client not found.")
        elif choice == '3':
            for id in clients:
                clients[id].conn.close()
            sys.exit("Shutting down server.")
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
