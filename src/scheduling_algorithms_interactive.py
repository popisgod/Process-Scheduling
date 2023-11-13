from analyze_results import display_results

def RR(processes) -> None:
    waiting_time, turnaround_time = calculate_times_RR(processes, 4)
    display_results(processes, waiting_time, turnaround_time)
    
def calculate_times_RR(processes, time_slice : int):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n
    
    # Create a list to track remaining burst time for each process
    remaining_time = [processes[i].burst_time for i in range(n)]
    complete = 0
    current_process = 0

    while complete != n:
        remaining_time[current_process] -= time_slice

        if remaining_time[current_process] <= 0:
            complete += 1
        
        for j in range(n):
            if j != current_process and remaining_time[j] > 0:
                waiting_time[j] += time_slice
                
        if complete == n:
            break
    
    for i in range(n):
        turnaround_time[i] = processes[i].burst_time + waiting_time[i]
 
    return waiting_time, turnaround_time          

   
def calculate_times_PQ(processes):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n
    aging_factor = 1  # You can adjust the aging factor based on your preference

    # Sort processes based on priority (lower priority value means higher priority)
    processes.sort(key=lambda x: x.priority)

    # Calculate waiting time and turnaround time for each process
    for i in range(n):
        if i > 0:
            # Aging: Increase the priority of waiting processes over time
            processes[i].priority += aging_factor

        # Preemption: Check if a higher-priority process arrived and preempt the current process
        higher_priority_processes = [p for p in processes[i + 1:] if p.arrival_time <= turnaround_time[i]]
        if higher_priority_processes:
            highest_priority_process = min(higher_priority_processes, key=lambda x: x.priority)
            waiting_time[i + 1] = turnaround_time[i]
            turnaround_time[i + 1] = waiting_time[i + 1] + highest_priority_process.burst_time

        else:
            waiting_time[i] = turnaround_time[i - 1] if i > 0 else 0
            turnaround_time[i] = waiting_time[i] + processes[i].burst_time

    return waiting_time, turnaround_time

def PQ(processes) -> None:
    waiting_time, turnaround_time = calculate_times_PQ(processes)
    display_results(processes, waiting_time, turnaround_time)
    
def calculate_times_SJN(processes):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n
    remaining_time = [processes[i].burst_time for i in range(n)]

    current_time = 0
    completed_processes = 0

    while completed_processes < n:
        shortest_burst_time = float('inf')
        current_process = None

        # Check for processes that have arrived and find the one with the shortest burst time
        for i in range(n):
            if processes[i].arrival_time <= current_time and remaining_time[i] > 0:
                if remaining_time[i] < shortest_burst_time:
                    shortest_burst_time = remaining_time[i]
                    current_process = i

        if current_process is not None:
            waiting_time[current_process] = current_time - processes[current_process].arrival_time
            current_time += remaining_time[current_process]
            remaining_time[current_process] = 0
            completed_processes += 1
        else:
            current_time += 1  # No process is ready, move to the next time unit

    for i in range(n):
        turnaround_time[i] = processes[i].burst_time + waiting_time[i]

    return waiting_time, turnaround_time

def SJN(processes) -> None:
    waiting_time, turnaround_time = calculate_times_SJN(processes)
    display_results(processes, waiting_time, turnaround_time)