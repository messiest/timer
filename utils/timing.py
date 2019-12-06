from time import time
from atexit import register
from contextlib import ContextDecorator


class Timer(ContextDecorator):
    start = time()  # global start time

    @staticmethod
    @register
    def on_end(): # will run on interpreter shutdown
        print("GLOBAL RUNTIME: ", Timer.format_time(time() - Timer.start))

    @staticmethod
    def format_time(runtime):
        if runtime > 60:
            mins = runtime // 60
            secs = runtime % 60
            return f"{mins} minutes, {secs} seconds"
        else:
            return f"{runtime:.1f} seconds"

    def __init__(self, tag=""):
        self.tag = tag

    def __enter__(self):
        self.start = time()  # instance start time
        return self

    def __exit__(self, *exc):
        print(self)
        return False

    def __str__(self):
        return self.tag + f"RUNTIME: {self.format_time(time() - self.start)}"
