import socket
import threading

def handle_recieve(sock):
    while True:
        try:
            message = sock.recv(1024).decode()
            if not message or message.lower() == "exit":
                print("\nServer disconnected.")
                sock.close()
                break
            print(f"\nServer: {message}\nYou: ", end="")
        except:
            break

def handle_send(sock):
    while True:
        message = input("You: ")
        sock.send(message.encode())
        if message.lower() == "exit":
            print("Chat ended.")
            sock.close()
            break

def main():
    host = "127.0.0.1"
    port = 5001

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print("Connected to server. Type 'exit' to quit.")

    threading.Thread(target=handle_recieve, args=(client_socket,), daemon=True).start()
    handle_send(client_socket)

if __name__ == "__main__":
    main()