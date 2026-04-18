import socket

HOST = '127.0.0.1'
PORT = 12345

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    print("Connected to server")
 #a+
    msg = client.recv(1024).decode()
    print(msg, end="")

    username = input()
    client.send(username.encode())

    msg = client.recv(1024).decode()
    print(msg)

    while True:
        cmd = input(">> ")
        client.send(cmd.encode())

        if cmd.upper() == "EXIT":
            break

        try:
            response = client.recv(1024).decode()
            print(response)
        except:
            print("Server disconnected.")
            break
#a++
    client.close()


if __name__ == "__main__":
    start_client()