import numpy as np

def norm_scale(v: complex) -> complex:
    l = np.abs(v)
    n = v / l if l != 0 else 0
    s = np.complex128(complex(n.real * v.real, n.imag * v.imag))
    return s

# Пример использования
mv = np.complex128(5 + 5j)  # например, движение вверх по оси y
result_vector = norm_scale(mv)
print(result_vector)
