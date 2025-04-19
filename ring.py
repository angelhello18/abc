# Class representing an individual process
class Process:
    def __init__(self, pid):
        self.pid = pid        # Store the process ID
        self.active = True    # Set the process as active (alive) by default

# Class to simulate the Ring Election Algorithm
class RingElection:
    def __init__(self, total_processes):
        # Initialize a list of processes with IDs from 0 to total_processes - 1
        self.processes = [Process(i) for i in range(total_processes)]
        self.total_processes = total_processes  # Store the number of processes

    # Function to simulate failure of a process
    def deactivate_process(self, pid):
        self.processes[pid].active = False  # Mark the process as inactive
        print(f"Process {pid} has failed.")

    # Function to simulate recovery of a process
    def activate_process(self, pid):
        self.processes[pid].active = True  # Mark the process as active
        print(f"Process {pid} is back online.")

    # Function to find the next alive (active) process in the ring
    def find_next_alive(self, start):
        next_pid = (start + 1) % self.total_processes  # Move to the next process in the ring
        while not self.processes[next_pid].active:     # Loop until an active process is found
            next_pid = (next_pid + 1) % self.total_processes  # Continue in the ring
        return next_pid  # Return the ID of the next active process

    # Function to start the election process
    def start_election(self, initiator_pid):
        print(f"\nElection started by process {initiator_pid}")

        # If the initiator is not active, the election cannot proceed
        if not self.processes[initiator_pid].active:
            print(f"Process {initiator_pid} is not active!")
            return

        message = [initiator_pid]  # Initialize message list with the initiator
        current = self.find_next_alive(initiator_pid)  # Find next active process in the ring

        # Loop to circulate election message around the ring
        while current != initiator_pid:  # Continue until the message returns to the initiator
            print(f"Process {message[-1]} passes election message to {current}")
            if self.processes[current].active:
                message.append(current)  # Add current process to the election message
            current = self.find_next_alive(current)  # Move to the next active process

        # Election is complete; highest ID in message wins
        coordinator = max(message)
        print(f"Process {coordinator} is elected as coordinator.")

        # Notify all active processes about the new coordinator
        current = coordinator  # Start from coordinator
        next_proc = self.find_next_alive(current)  # Find the next process in the ring

        while next_proc != coordinator:  # Loop until coordinator receives its own message
            print(f"Coordinator({coordinator}) message sent to process {next_proc}")
            current = next_proc
            next_proc = self.find_next_alive(current)

        print("Election completed.\n")  # Final confirmation of election end


# ---------------- Example usage ----------------

if __name__ == "__main__":
    ring = RingElection(6)  # Create a ring of 6 processes (IDs 0 to 5)

    ring.deactivate_process(5)  # Simulate failure of highest process (5)
    ring.start_election(2)      # Start election from process 2

    ring.activate_process(5)    # Simulate that process 5 comes back
    ring.start_election(3)      # Start a new election from process 3
