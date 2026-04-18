import socket
import threading
import os

HOST = '192.168.178.183'
PORT = 12345


if not os.path.exists("server_files"):
    os.mkdir("server_files")


clients_permissions = {
    "admin": "admin",
    "user1": "read",
    "user2": "read",
    "user3": "read"
}

def handle_client(client_socket, addr):
    print(f"[+] Connected: {addr}")
    client_socket.send("Shkruaj username: ".encode())
    username = client_socket.recv(1024).decode().strip()

    permission = clients_permissions.get(username, "read")

    client_socket.send(f"Je lidhur si {username} me permission: {permission}\n".encode())
