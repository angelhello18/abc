# Function to return the maximum of two numbers
def max1(a, b):
    if a > b:
        return a
    else:
        return b

# Function to display the final timestamps of events in both processes
def display(e1, e2, p1, p2):
    print()
    print("The time stamps of events in P1:")
    for i in range(0, e1):
        print(p1[i], end=" ")
    
    print()
    print("The time stamps of events in P2:")
    for i in range(0, e2):
        print(p2[i], end=" ")

# Function to calculate Lamport Logical Clocks
def lamportLogicalClock(e1, e2, m):
    # Initialize timestamps for each event in both processes
    p1 = [0]*e1
    p2 = [0]*e2

    # Set default timestamp values: 1, 2, 3,...
    for i in range(0, e1):
        p1[i] = i + 1
    for i in range(0, e2):
        p2[i] = i + 1

    # Display the message matrix
    for i in range(0, e2):
        print(end='\t')
        print("e2", end="")
        print(i + 1, end="")
    for i in range(0, e1):
        print()
        print("e1", end="")
        print(i + 1, end="\t")
        for j in range(0, e2):
            print(m[i][j], end="\t")

    # Update the logical timestamps based on message passing
    for i in range(0, e1):
        for j in range(0, e2):
            # If a message is sent from P1[i] to P2[j]
            if m[i][j] == 1:
                # Update P2[j]'s timestamp
                p2[j] = max1(p2[j], p1[i] + 1)
                # All subsequent events in P2 must follow
                for k in range(j + 1, e2):
                    p2[k] = p2[k - 1] + 1

            # If a message is received by P1[i] from P2[j]
            if m[i][j] == -1:
                # Update P1[i]'s timestamp
                p1[i] = max1(p1[i], p2[j] + 1)
                # All subsequent events in P1 must follow
                for k in range(i + 1, e1):
                    p1[k] = p1[k - 1] + 1

    # Display final logical clocks
    display(e1, e2, p1, p2)


# Driver code to set up the message passing matrix
if __name__ == "__main__":
    e1 = 5  # Number of events in process 1
    e2 = 3  # Number of events in process 2

    # Create a matrix m[e1][e2] to represent message passing
    m = [[0]*3 for i in range(0, 5)]

    # Fill the matrix with message details:
    # m[i][j] = 1 means event P1[i] sends message to P2[j]
    # m[i][j] = -1 means event P1[i] receives message from P2[j]
    # m[i][j] = 0 means no message

    # Example messages:
    m[1][2] = 1     # P1's 2nd event sends message to P2's 3rd event
    m[4][1] = -1    # P1's 5th event receives message from P2's 2nd event

    # Call the function to compute Lamport Logical Clocks
    lamportLogicalClock(e1, e2, m)
