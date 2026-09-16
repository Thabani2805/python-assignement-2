import socket

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 5000))
    server.listen(1)

    print("Server is waiting for a connection...")

    connection, address = server.accept()
    print("Client connected.")

    message = connection.recv(1024).decode()
    print("Message received:", message)

    connection.close()
    server.close()

except socket.error as e:
    print("Network error:", e)
    \
    