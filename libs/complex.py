from math import copysign
def ns(c: complex):
    if c == 0:
     return 0
    abs_c = abs(c)
    r = c.real
    i = c.imag
    r_sign = copysign(1, r)
    i_sign = copysign(1, i)
    return complex(r**2/abs_c*r_sign, i**2/abs_c*i_sign)
