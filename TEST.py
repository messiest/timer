import time

from utils import timer

@timer
def test():
    print("test")
    time.sleep(1.8)

def main():
    print("main")
    time.sleep(2.3)

if __name__ == "__main__":
    test()  # decorated function

    with timer:
        main()
