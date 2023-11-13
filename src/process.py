import random

class Process:
    def __init__(self, pid: int, arrival_time: int, burst_time: int, priority: int) -> None:
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority

    @staticmethod
    def create_random_process(pid):
        arrival_time = random.randint(0, 10)
        burst_time = random.randint(1, 10)
        priority = random.randint(1, 20)  # Adjust the range based on your priority scale
        return Process(pid, arrival_time, burst_time, priority)

