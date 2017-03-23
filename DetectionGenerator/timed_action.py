import sched
import time


class TimedAction:
    def __init__(self):
        self.scheduler = sched.scheduler(time.time, time.sleep)

    def run_in_a_sec(self, calls_per_second, callback, *args, **kwargs):
        period = 1.0 / calls_per_second

        def reload():
            callback(*args, **kwargs)
            self.scheduler.enter(period, 0, reload, ())
        self.scheduler.enter(period, 0, reload, ())
