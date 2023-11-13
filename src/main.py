from scheduling_algorithms_batch import FCFS, SJF
from scheduling_algorithms_interactive import RR
from process import Process

if __name__ == "__main__":
    
    # Create some processes
    processes = [Process.create_random_process(i) for i in range(15)]

    # Execute the FCFS algorithm
    FCFS(processes)
    
    # Execute the SJF algorithm
    SJF(processes)
    
    # Execute the RR 
    RR(processes)
