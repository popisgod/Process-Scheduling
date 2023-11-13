from analyze_results import display_results

def calculate_times_FCFS(processes):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Calculate waiting time for the first process
    waiting_time[0] = 0

    # Calculate waiting time for each process
    for i in range(1, n):
        waiting_time[i] = processes[i - 1].burst_time + waiting_time[i - 1]

    # Calculate turnaround time for each process
    for i in range(n):
        turnaround_time[i] = processes[i].burst_time + waiting_time[i]

    return waiting_time, turnaround_time

def FCFS(processes):
    # Sort processes based on arrival time (FCFS)
    processes.sort(key=lambda x: x.arrival_time)

    waiting_time, turnaround_time = calculate_times_FCFS(processes)
    display_results(processes, waiting_time, turnaround_time)

def calculate_times_SJF(processes):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Create a list to track remaining burst time for each process
    remaining_time = [processes[i].burst_time for i in range(n)]
    complete = 0
    time = 0
    min_burst = float('inf')
    shortest = 0
    check = False

    while complete != n:
        for j in range(n):
            if (processes[j].arrival_time <= time) and (remaining_time[j] < min_burst) and remaining_time[j] > 0:
                min_burst = remaining_time[j]
                shortest = j
                check = True

        if not check:
            time += 1
            continue

        remaining_time[shortest] -= 1
        min_burst = remaining_time[shortest]

        if min_burst == 0:
            min_burst = float('inf')

        if remaining_time[shortest] == 0:
            complete += 1
            check = False
            end_time = time + 1
            waiting_time[shortest] = end_time - processes[shortest].burst_time - processes[shortest].arrival_time
            if waiting_time[shortest] < 0:
                waiting_time[shortest] = 0

        time += 1

    for i in range(n):
        turnaround_time[i] = processes[i].burst_time + waiting_time[i]

    return waiting_time, turnaround_time

def SJF(processes):
    waiting_time, turnaround_time = calculate_times_SJF(processes)
    display_results(processes, waiting_time, turnaround_time)
    
