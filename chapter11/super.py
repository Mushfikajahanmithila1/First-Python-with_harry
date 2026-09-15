class Employe:
    def __init__(self):
        print("This Employe constructor")
    company = "Google"
    salary = 120000
    def employe(self):
        print(f"The name of the company is: {self.company}. The salary is: {self.salary}")

class Programmer(Employe):
    def __init__(self):
            super().__init__()
            print("This Programmer constructor")
    language = "Python"
    def programmar(self):
        print(f"Your language is: {self.language}")

class Coder(Programmer):
    def __init__(self):
        super().__init__()
        print("This Coder constructor")
    otherLanguage = "JavaScript"
    def coder(self):
        print(f"Your other language is: {self.otherLanguage}")

o = Coder()
print(o.language)

# print(o.language, o.salary, o.otherLanguage, o.company)