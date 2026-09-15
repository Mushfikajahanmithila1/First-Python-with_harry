class n:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n


m = n(2)
o = n(5)
print(m + o)