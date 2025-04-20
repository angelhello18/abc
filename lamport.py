# Function to return the maximum of two values
def max1(a, b):
    return a if a > b else b


# Function to print the dependency matrix (communication between events)
def printMatrix(m, e1, e2):
    print("Lamport Clock Assignments:")
    print("\t", end="")  # Header spacing for P2 events
    for j in range(e2):
        print(f"e2{j+1}", end="\t")  # Column headers for P2 events
    for i in range(e1):
        print(f"\ne1{i+1}", end="\t")  # Row headers for P1 events
        for j in range(e2):
            print(m[i][j], end="\t")  # Print the matrix values (0, 1, -1)


# Function to visualize the event timeline and message flow between processes
def printFlow(p1, p2, m, e1, e2):
    print("\n\nEvent timeline with message flow:")
    for i in range(e1):
        print(f"P1: e1{i+1}({p1[i]})", end="")  # Print event and timestamp from P1
        for j in range(e2):
            if m[i][j] == 1:
                # If there's a message from P1[i] to P2[j]
                print(f" ───> e2{j+1}({p2[j]}) [P2]", end="")
        print()
    
    for j in range(e2):
        found = False
        for i in range(e1):
            if m[i][j] == -1:
                # If there's a message from P2[j] to P1[i]
                print(f"P2: e2{j+1}({p2[j]}) ───> e1{i+1}({p1[i]}) [P1]")
                found = True
        if not found:
            # If no message is sent from this P2 event
            print(f"P2: e2{j+1}({p2[j]})")


# Main function implementing Lamport Logical Clock algorithm
def lamportLogicalClock(e1, e2, m):
    # Initialize timestamps for events in both processes with simple incrementing values
    p1 = [i + 1 for i in range(e1)]  # Timestamps for P1 events
    p2 = [i + 1 for i in range(e2)]  # Timestamps for P2 events

    # Display the initial dependency matrix
    printMatrix(m, e1, e2)

    # Apply Lamport Clock rules based on message passing
    for i in range(e1):
        for j in range(e2):
            if m[i][j] == 1:  # Message from P1[i] to P2[j]
                # Ensure P2[j] is at least one more than P1[i]
                p2[j] = max1(p2[j], p1[i] + 1)
                # Increment timestamps of subsequent events in P2
                for k in range(j + 1, e2):
                    p2[k] = p2[k - 1] + 1
            elif m[i][j] == -1:  # Message from P2[j] to P1[i]
                # Ensure P1[i] is at least one more than P2[j]
                p1[i] = max1(p1[i], p2[j] + 1)
                # Increment timestamps of subsequent events in P1
                for k in range(i + 1, e1):
                    p1[k] = p1[k - 1] + 1

    # Display final timestamps and message flows
    printFlow(p1, p2, m, e1, e2)


# Driver code to test the Lamport Logical Clock implementation
if __name__ == "__main__":
    e1 = 5  # Number of events in process P1
    e2 = 3  # Number of events in process P2

    # Initialize dependency matrix with all 0s (no communication)
    m = [[0] * e2 for _ in range(e1)]

    # Define communication: 
    m[1][2] = 1    # P1 event e12 sends message to P2 event e23
    m[4][1] = -1   # P2 event e22 sends message to P1 event e15

    # Call the Lamport clock function
    lamportLogicalClock(e1, e2, m)


'''
Conclusion:
This program implements Lamport Logical Clocks to assign logical timestamps to events occurring 
in two separate processes in a distributed system. By analyzing message dependencies, it ensures 
that the causal ordering of events is preserved without requiring synchronized physical clocks. 
The timestamps help identify the sequence and causality between distributed events, which is 
essential for debugging, event tracing, or consistency checks in distributed computing.
'''
