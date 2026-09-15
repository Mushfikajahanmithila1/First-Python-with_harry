class Employe:
    company = "Google"
    salary = 120000
    def employe(self):
        print(f"The name of the company is: {self.company}. The salary is: {self.salary}")

class Programmer(Employe):
    language = "Python"
    def programmar(self):
        print(f"Your language is: {self.language}")


P = Programmer()
print(P.language, P.salary, P.company)