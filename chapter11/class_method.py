class Employe:
    a = 12
    @classmethod   # This not change the class attr with instance attr
    def show(cls):
        print(f"The value of the class attribute is: {cls.a}")

e = Employe()
e.a = 15
e.show()
3