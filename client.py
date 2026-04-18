import socket

HOST = '127.0.0.1'
PORT = 12345

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    print("Connected to server")

    client.close()


if __name__ == "__main__":
    start_client()