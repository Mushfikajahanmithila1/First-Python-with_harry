class Calculator:
    def __init__(self, n):
        self.n = n
    def squre(self):
        print(f"The squre of the number is: {self.n * self.n}")
    def cube(self):
        print(f"The cube of the number is: {self.n * self.n * self.n}")
    def squreroot(self):
        print(f"The squreroot of the number is: {self.n**1/2}")

Calc = Calculator(4)

Calc.squre()
Calc.cube()
Calc.squreroot()
