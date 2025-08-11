import socket
import threading

def handle_recieve(conn):
    while True:
        try:
            message = conn.recv(1024).decode()
            if not message or message.lower() == "exit":
                print("\nClient disconnected.")
                conn.close()
                break
            print(f"\nClient: {message}\nYou: ", end="")
        except:
            break

def handle_send(conn):
    while True:
        message = input("You: ")
        conn.send(message.encode())
        if message.lower() == "exit":
            print("Chat ended.")
            conn.close()
            break

def main():
    host = "127.0.0.1"
    port = 5001

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"Server started on {host}:{port}, waiting for connection...")
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    threading.Thread(target=handle_recieve, args=(conn,), daemon=True).start()
    handle_send(conn)

if __name__ == "__main__":
    main()