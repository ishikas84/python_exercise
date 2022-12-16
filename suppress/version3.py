
import sys
import traceback
import contextlib

class suppress(contextlib.ContextDecorator):
    def __init__(self, *args):
        self.errortype = args
        self.traceback = None
        self.exception = None
    
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.traceback = exc_tb
        self.exception = exc_val
        return isinstance(exc_val, self.errortype)


with suppress(NameError):
    print("Hi!")
    print("It's nice to meet you,", name)
    print("Goodbye!")
x = 0
with suppress(ValueError):
    x = int('hello')
print(x)
with suppress(ValueError, TypeError):
    x = int('hello')
with suppress(ValueError, TypeError):
    x = int(None)

with suppress(ValueError, TypeError) as context:
    x = int('hello')
print(context.exception)
print(context.traceback)

with suppress(TypeError):
    print("Hi!")
    print("It's nice to meet you,", name)
    print("Goodbye!")