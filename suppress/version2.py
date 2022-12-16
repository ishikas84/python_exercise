from contextlib import contextmanager


@contextmanager
def suppress(*errortype):
    try:
        yield
    except errortype as e:
        pass



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


with suppress(TypeError):
    print("Hi!")
    print("It's nice to meet you,", name)
    print("Goodbye!")