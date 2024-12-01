from time import sleep, time

class Clock():
    def __init__(self, tps: float = 30):
        self.set_tps(tps)
        
        self.last_tick_time = time()
        
    def tick(self):
        self.processes_end_time = time()
        
        wait_time = self.tick_speed - (self.processes_end_time - self.last_tick_time)
        sleep(wait_time) if wait_time >= 0 else print("Overloading!")
        
        self.last_tick_time = time()

    def set_tps(self, tps: float):
        self.tps = tps
        self.tick_speed = 1 / tps