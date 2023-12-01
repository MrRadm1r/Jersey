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

l = 15
dsc = [[0j]*l]*2

def inertia(c: complex):
    global dcs
    dsc[0] = dsc[0][1:]+[c.real+c.imag*1j]
    dsc[1] = dsc[1][1:]+[sum(dsc[0])/len(dsc[0])]
    return sum(dsc[1])/len(dsc[1])