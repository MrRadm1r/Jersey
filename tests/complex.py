def ns(c):
    if c == 0:
     return 0
    abs_c = abs(c)
    return complex(c.real**2/abs_c, c.imag**2/abs_c)