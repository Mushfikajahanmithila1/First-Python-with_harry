class Employe:
    language = "Python, JavaScript",
    experience = "2 years" ,
    salary = 1000

    def __init__(self, name, experience, language, salary): # dunder method which is called automaticly
        self.name = name
        self.experience = experience
        self.language = language
        self.salary = salary

    def getInfo(self):
        print(f"The language is: {self.language}. The experience is: {self.experience}. The salary is: {self.salary}")

mushfika = Employe("Mushfika", "3 years", "Python", 12000)

print(mushfika.name, mushfika.language)

mushfika.getInfo()
