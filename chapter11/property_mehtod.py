class Employe:
    a = 23
    def show(self):
        print(f"The value of the a attr is: {self.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


e = Employe()
e.name = "Mushfika Jahan"
print(e.name)
# print(e.fname, e.lname)
