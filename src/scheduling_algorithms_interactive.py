from analyze_results import display_results

def RR(processes):
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