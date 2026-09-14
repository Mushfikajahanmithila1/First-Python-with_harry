class Employe:
    language = "Python, JavaScript",
    experience = f"{1}year" ,
    salary = 1000

    def getInfo(self):
        print(f"The language is: {self.language}. The experience is: {self.experience}. The salary is: {self.salary}")

mushfika = Employe()

mushfika.getInfo()