import socket

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(("192.168.1.34",6666))

print("Connection establuished type exit to qyit")

while True:
    message=input("enter command:")
    client_socket.send(message.encode())

    if message.lower()=='exit':
        break

    response= client_socket.recv(1024).decode()
    print(f"server:{response}")

client_socket.close()


