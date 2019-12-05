# timer
A simple timer decoration for functions.

We have structured this repository as if it were a project, with the `timer` function being found in the `utils` directory.

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
    # Do stuff
```

To use the `timer` as a context manager you simply invoke it with a `with` statement:
```python
with timer:
    # Do stuff
```
