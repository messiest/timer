# timer
A simple timer that can be used to track runtime.
The purpose of this is to provide a simple, and standard, way of tracking runtime.
This is very useful when testing implementations, and helpful when tracking the progress of longer-running programs.

#### Notes:
> We have structured this repository as if it were a project, with the `timer` object being defined in the [`utils`](utils/) directory, and the main program being executed in [`TEST.py`](test.py).
> If you would like to simply see the code itself, a gist is available [here](https://gist.github.com/messiest/c6c86d60dd5544783d5eb2be448cfb8a).
> Alternatively, you can find the code within this repository [here](utils/timing.py).

## Usage

To access the `timer`, you will import it using
```python
from utils import timer
```

The `timer` can be used two different ways, as a decorator and as a context manager.

To use the timer as a decorator, simply apply the decorator to a function that you want to time:
```python
@timer
def my_function():
    # do stuff
```

To use the `timer` as a context manager you simply invoke it with a `with` statement:
```python
with timer:
    # do stuff
```

When the function, or context, finishes execution, the respective runtime will be output to the console.
