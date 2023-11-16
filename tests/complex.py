import math

def projection(c: complex) -> complex:
    deg = math.degrees(math.atan2(c.real, c.imag))
    rad = math.radians(deg)
    return complex(c.real * math.cos(rad), c.imag * math.sin(rad))


print(projection(3j+3))

def func(name: str, age: int, height: int|float) -> None:
    pass