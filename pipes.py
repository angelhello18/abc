from multiprocessing import Process, Pipe  # Import Process and Pipe for creating child processes and communication

# Function to be run by the child process
def child_process(conn):
    msg = conn.recv()  # Receive message from the parent process
    print("Child received:", msg)
    
    conn.send("Hello from child!")  # Send a message back to the parent
    conn.close()  # Close the connection once done

# Main block - runs only when script is run directly
if __name__ == '__main__':
    # Create a two-way Pipe (returns two connection objects)
    parent_conn, child_conn = Pipe()  
    
    # Create a child process, giving it the child's end of the Pipe
    p = Process(target=child_process, args=(child_conn,))
    
    p.start()  # Start the child process
    
    parent_conn.send("Hello from parent!")  # Send a message to the child through the pipe
    
    print("Parent received:", parent_conn.recv())  # Receive a message from the child and print it
    
    p.join()  # Wait for the child process to finish

'''
Conclusion:
This program demonstrates inter-process communication (IPC) using Python’s multiprocessing module and a Pipe. 
It shows how a parent and child process can send and receive messages through a communication channel.
This simple example helps understand how processes can safely exchange data in parallel execution environments, 
making it a key concept in concurrent programming.
'''
