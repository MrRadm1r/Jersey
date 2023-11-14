import math


class taneq:
    def __init__(self, equation: str):
        self.eq = equation
        self.__fcheck()
        self.__sorteq()

    def __repr__(self):
        return f"y={''.join(self.eq)}"

    def __fcheck(self):
        if self.eq[0] not in ["+", "-"]:
            self.eq = "+" + self.eq

    def __sorteq(self):
        temp = self.eq[0]
        result = []
        for i in range(1, len(self.eq)):
            if self.eq[i] in ("+", "-"):
                result.append(temp)
                temp = ""
                temp = temp + self.eq[i]
            else:
                temp = temp + self.eq[i]
        result.append(temp)
        self.eq = result

    @staticmethod
    def isvar(el):
        try:
            int(el)
            return False
        except ValueError:
            var_name = ""
            for i in list(el)[1:]:
                try:
                    int(i)
                except ValueError:
                    var_name += i
        return var_name


    def derived(self, x0):
        # y=f(x0)+f'(x0)(x-x0)
        f = 0
        fd = ""
        result = 0
        for i in self.eq:
            if self.isvar(""):
                result += eval(self.eq.replace(""))






print(taneq("-x+3c+21f+(-1)-2").isvar(""))
