import time
from contextlib import ContextDecorator


class Timer(ContextDecorator):
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *exc):
        print("RUNTIME: ", self.format_runtime(time.time() - self.start))
        return False

    def format_runtime(self, runtime):
        if runtime > 60:
            mins = runtime // 60
            secs = runtime % 60
            return f"{mins} minutes, {secs} seconds"
        else:
            return f"{runtime:.1f} seconds"
