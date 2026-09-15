class Employe:
    company = "Google"
    salary = 120000
    def employe(self):
        print(f"The name of the company is: {self.company}. The salary is: {self.salary}")

class Programmer:
    language = "Python"
    def programmar(self):
        print(f"Your language is: {self.language}")

class Coder(Employe, Programmer):
    otherLanguage = "JavaScript"
    def coder(self):
        print(f"Your other language is: {self.otherLanguage}")


P = Coder()
print(P.language, P.salary, P.company, P.otherLanguage)