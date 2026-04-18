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
     while True:
        try:
            data = client_socket.recv(1024).decode()
            if not data:
                break

            print(f"[{username}] -> {data}")

            command = data.split()

            if command[0] == "READ":
                files = os.listdir("server_files")
                client_socket.send(f"Files: {files}\n".encode())

            elif command[0] == "WRITE":
                if permission != "admin":
                    client_socket.send("Nuk ke leje për WRITE!\n".encode())
                else:
                    filename = command[1]
                    content = " ".join(command[2:])
                    with open(f"server_files/{filename}", "w") as f:
                        f.write(content)
                    client_socket.send("File u shkrua me sukses!\n".encode())

            elif command[0] == "EXEC":
                if permission != "admin":
                    client_socket.send("Nuk ke leje për EXECUTE!\n".encode())
                else:
                    result = os.listdir("server_files")
                    client_socket.send(f"Exec result: {result}\n".encode())

            elif command[0] == "EXIT":
                client_socket.send("Po shkëputesh...\n".encode())
                break

            else:
                client_socket.send("Komandë e panjohur!\n".encode())

        except:
            break
