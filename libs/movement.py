from math import copysign

class Vector:
    l = 15
    dsc = [[0j]*l]*2
    def __init__(self) -> None:
        super().__init__()
        self.z = complex()
    
    def __call__(self):
        return self.z

    def restriction(self):
        if self.z == 0:
            return 0
        abs_c = abs(self.z)
        r = self.z.real
        i = self.z.imag
        r_sign = copysign(1, r)
        i_sign = copysign(1, i)
        self.z = complex(r**2/abs_c*r_sign, i**2/abs_c*i_sign)

    def inertia(self):
        Vector.dsc[0] = Vector.dsc[0][1:]+[self.z.real+self.z.imag*1j]
        Vector.dsc[1] = Vector.dsc[1][1:]+[sum(Vector.dsc[0])/len(Vector.dsc[0])]
        self.z = sum(Vector.dsc[1])/len(Vector.dsc[1])

    def zero(self):
        self.z = complex()
    
    def block(self, k: list=[True, True]):
        if len(k) not in [1, 2]:  # Урбать при финальной компиляции #C11     
            raise AttributeError("The k attribute must be a list of length 2 or 1")
        self.z = complex(self.z.real * k[0], self.z.imag * k[1])
    
    def norm_speed(self):
        self.restriction()
        self.inertia()


if __name__ == "__main__":
    v = Vector()