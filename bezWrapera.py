import time
from functools import wraps


def dekorator(func):
    @wraps(func)
    def nova(*args, **kwargs):
        """Ovo je doc za f-ju nova"""
        print(f"Ime za f-ju je :{func.__name__}")
        print(f"Docstring za f-ju je :{func.__doc__}")
        print(f"Vrednosti za f-ju su :{func.__annotations__}")
        start = time.time()
        func(*args)
        end = time.time()
        print(f"Time for execution is: {end - start}")

    return nova


@dekorator
def add(a: int, b: int):
    """Adding"""
    time.sleep(1.1)
    return a + b


@dekorator
def sub(a: int, b: int):
    """Subtracting"""
    time.sleep(1.1)
    return a - b


add(2, 3)
sub(3, 2)
print("--------------------------------------------------\n")
print(f"Ime za f-ju add je :{add.__name__}")
print(f"Docstring za f-ju add je :{add.__doc__}")
print(f"Vrednosti za f-ju add su :{add.__annotations__}")

print(f"Ime za f-ju sub je :{sub.__name__}")
print(f"Docstring za f-ju sub je :{sub.__doc__}")
print(f"Vrednosti za f-ju sub su :{sub.__annotations__}")
