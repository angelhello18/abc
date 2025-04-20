import socket  # Importing the socket module to enable network communication

# Create a TCP/IP socket using IPv4 addressing
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server using its IP address and port number
client_socket.connect(("192.168.1.34", 6666))

print("Connection established. Type 'exit' to quit.")

# Start a loop to continuously send and receive messages
while True:
    # Take input from the user
    message = input("Enter command: ")
    
    # Send the message to the server after encoding it to bytes
    client_socket.send(message.encode())

    # If the user types 'exit', break the loop and close the connection
    if message.lower() == 'exit':
        break

    # Receive response from the server (up to 1024 bytes), then decode it
    response = client_socket.recv(1024).decode()
    
    # Display the server's response
    print(f"Server: {response}")

# Close the socket connection after exiting the loop
client_socket.close()


'''
Conclusion:
This Python client-server program demonstrates basic TCP communication using sockets. 
The server listens for connections and responds to messages, while the client sends commands and receives responses. 
Communication continues until "exit" is typed, showing a simple yet effective model for interactive two-way messaging.
'''
