import random

class Process:
    def __init__(self, pid : int, arrival_time : int, burst_time : int) -> None:
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time

    @staticmethod
    def create_random_process(pid):
        arrival_time = random.randint(0, 10)  # Set arrival time randomly between 0 and 10 for example
        burst_time = random.randint(1, 10)    # Set burst time randomly between 1 and 10 for example
        return Process(pid, arrival_time, burst_time)
