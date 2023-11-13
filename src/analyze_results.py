def display_results(processes, waiting_time, turnaround_time) -> None:
    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)
    n = len(processes)
    
    print("Process ID\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    for i in range(n):
        print(f"{processes[i].pid}\t\t{processes[i].arrival_time}\t\t{processes[i].burst_time}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")
    
    print("\nAverage Waiting Time:", total_waiting_time / n)
    print("Average Turnaround Time:", total_turnaround_time / n)
    efficiency = total_turnaround_time / n
    print("Overall Efficiency:", efficiency)
    total_waiting_time = sum(waiting_time)
    print("Total Waiting Time:", total_waiting_time)