class Temper:
    def __init__(self, t, unit='C'):
        self.__set_temp(t, unit)

    def __set_temp(self, t, unit='C'):
        if unit == 'C':
            Temper._set_c(self, t)
        elif unit == 'F':
            Temper._set_f(self, t)
        elif unit == 'K':
            Temper._set_k(self, t)

    def get_temp(self, unit='C'):
        if unit == 'C':
            return self.tc
        elif unit == 'F':
            return self.tf
        elif unit == 'K':
            return self.tk

    def _set_c(self, t):
        self.tc = t
        self.tf = t * 9 / 5 + 32
        self.tk = t + 273

    def _set_k(self, t):
        self.tc = t - 273
        self.tf = (t - 273) * 9 / 5 + 32
        self.tk = t

    def _set_f(self, t):
        self.tc = (t - 32) * 5 / 9
        self.tf = t
        self.tk = (t - 32) * 5 / 9 + 273

    def __str__(self):
        return f'Temperature is: {self.tc} C, {self.tk} K, {self.tf} F'


tm = Temper(36)
print(tm.get_temp())
print(tm.get_temp('K'))
print(tm.get_temp('F'))
tm.tk = 2000
print(tm)
